import orjson
import requests
import os
os.chdir(os.path.dirname(__file__))
with open('configure.json', "rb") as profile:
    profile = orjson.loads(profile.read())
funcdict=profile['f']
async_addr="http://gateway.openfaas.svc.cluster.local:8080/async-function/"
sync_addr="http://gateway.openfaas.svc.cluster.local:8080/function/"
def handle(req):
    input=orjson.loads(req)
    #分支判断
    if(input['s']==0):
        if(input['d'] != "warm"):
            for key in funcdict:
                data=requests.post(sync_addr+key,data=req)
            return data
        else:
            data=orjson.dumps({"s":0,"d":"warmup"})
            for key in funcdict:
                requests.post(async_addr+key,data=data)
            return {"s":0,"d":"warmup"}
    #进入req循环
    data=req
    for key in funcdict:
        if(funcdict[key]==2):
            data=orjson.loads(data)
            data['s']=2
            data=requests.post(sync_addr+key,data=orjson.dumps(data,option=orjson.OPT_SERIALIZE_NUMPY)).text[2:-2]
        else:
            data=requests.post(sync_addr+key,data=data).text[2:-2]
    return data

