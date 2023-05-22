import orjson
import numpy as np
import requests
import os

os.chdir(os.path.dirname(__file__))
with open('configure.json', "rb") as profile:
    funcdict = orjson.loads(profile.read())

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
    from aiohttp import ClientSession
    import asyncio
    data = req
    tasks=[]
    async_task=[]
    async def async_inference(url,data):
        async with ClientSession() as session:
            async with session.post(url,data=data) as response:
                return await response.text[2:-2]
    def sync_inference(url,data):
        return requests.post(url, data=data).text[2:-2]
    def classify(url,data):
        with open('./classify_src/labels.json', "rb") as labels_file:
            labels = orjson.loads(labels_file.read())
        # data = requests.post(sync_addr+key, data=data).text[2:-2]
        data = requests.post(url, data=data).text[2:-2]
        data=orjson.loads(data)
        x = np.array(data['d'], dtype=np.float32)
        x = np.argmax(x)
        classify_res = labels[str(x.item())]
        return {"s": 1, "d": classify_res}
    # Translate func into task
    for key in funcdict:
        if(funcdict[key] == 1):
            if(len(async_task)):
                tasks.append(("async",async_task))
                async_task=[]
            tasks.append(("sync",sync_addr+key))
        elif(funcdict[key] ==3):
            async_task.append(sync_addr+key)
        elif(funcdict[key] == 2):
            tasks.append(("classify",sync_addr+key))
    # Run task
    for task in tasks:
        if(task[0]=="sync"):
            data=sync_inference(task[1],data)
        elif(task[0]=="async"):
            atask=[]
            atask_url=task[1]
            for url in atask_url:
                atask.append(asyncio.create_task(async_inference(url=url,data=data)))
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(atask))
        elif(task[0]=="classify"):
            data=classify(task[1],data)
    return data
