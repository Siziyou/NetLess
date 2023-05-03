import orjson
import numpy as np
import requests
import os
os.chdir(os.path.dirname(__file__))


with open('configure.json', "rb") as profile:
    profile = orjson.loads(profile.read())
funcdict = profile['f']
async_addr = "http://gateway.openfaas.svc.cluster.local:8080/async-function/"
sync_addr = "http://gateway.openfaas.svc.cluster.local:8080/function/"


def handle(req):
    input = orjson.loads(req)
    # 分支判断
    if(input['s'] == 0):
        if(input['d'] != "warm"):
            for key in funcdict:
                data = requests.post(sync_addr+key, data=req)
            return data.text
        else:
            data = orjson.dumps({"s": 0, "d": "warmup"})
            for key in funcdict:
                requests.post(async_addr+key, data=data)
            return {"s": 0, "d": "warmup"}
    # 进入req循环
    data = req
    for key in funcdict:
        if(funcdict[key] == 1):
            data = requests.post(sync_addr+key, data=data).text[2:-2]
        elif(funcdict[key] == 2):
            with open('labels.json', "rb") as labels_file:
                labels = orjson.loads(labels_file.read())
            data = requests.post(sync_addr+key, data=data).text[2:-2]
            data=orjson.loads(data)
            x = np.array(data['d'], dtype=np.float32)
            x = np.argmax(x)
            classify_res = labels[str(x.item())]
            data = {"s": 1, "d": classify_res}
    return data
