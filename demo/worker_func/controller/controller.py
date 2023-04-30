import orjson
import requests
import os
os.chdir(os.path.dirname(__file__))
class controller:
    def __init__(self) -> None:
        with open('configure.json', "rb") as profile:
            self.profile = orjson.loads(profile.read())
        self.len=profile['l']
        self.funcdict=profile['f']
        self.async_addr="http://gateway.openfaas.svc.cluster.local:8080/async-function/"
        self.sync_addr="http://gateway.openfaas.svc.cluster.local:8080/function/"
    def predict(self,req):
        input=orjson.loads(req)
        #分支判断
        if(input['s']==0):
            if(input['d'] != "warm"):
                return self.debug(req)
            else:
                return self.warmup()
        #进入req循环
        data=req
        for key in self.funcdict:
            if(self.funcdict[key]['s']==2):
                data=orjson.loads(data)
                data['s']=2
                data=requests.post(self.sync_addr+function[key],data=orjson.dumps(data,option=orjson.OPT_SERIALIZE_NUMPY)).text[2:-2]
            else:
                data=requests.post(self.sync_addr+function[key],data=data).text[2:-2]
        return data
    #仅支持数据流开销测试
    def debug(self,req):
        data=req
        for key in self.funcdict:
            data=requests.post(self.sync_addr+function[key],data=data)
        return data
    #预热函数
    def warmup(self):
        data=orjson.dumps({"s":0,"d":"warmup"})
        for key in self.funcdict:
            requests.post(self.async_addr+function[key],data=data)
        return {"s":0,"d":"warmup"}
