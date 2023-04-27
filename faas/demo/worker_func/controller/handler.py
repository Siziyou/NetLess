import orjson
import requests
import numpy
def warmup():
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func0',data=orjson.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func1',data=orjson.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func2',data=orjson.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func3',data=orjson.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func4',data=orjson.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func5',data=orjson.dumps({"s":0,"d":"warmup"}))
    return {"s":0,"d":"warmup"}


def handle(req):
    input=orjson.loads(req)
    if(input['s']==0):
        if(input['d'] != "warm"):
            return debug(req)
        else:
            return warmup()
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func0',data=req).text[2:-2]
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func1',data=x).text[2:-2]
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func2',data=x).text[2:-2]
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func3',data=x).text[2:-2]
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func4',data=x).text[2:-2]
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func5',data=x).text[2:-2]
    return x

def debug(req):
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func0',data=req).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func1',data=x).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func2',data=x).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func3',data=x).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func4',data=x).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func5',data=x).text
    return x