import json
import requests
import os
os.chdir(os.path.dirname(__file__))
def warmup():
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func0',data=json.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func1',data=json.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func2',data=json.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func3',data=json.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func4',data=json.dumps({"s":0,"d":"warmup"}))
    requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/func5',data=json.dumps({"s":0,"d":"warmup"}))
    return {"s":0,"d":"warmup"}


def handle(req):
    body=json.loads(req)
    if(body['s']==0):
        return warmup()
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func0',data=json.dumps({"s":1,"d":body['d']})).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func1',data=json.dumps({"s":1,"d":json.loads(x)['d']})).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func2',data=json.dumps({"s":1,"d":json.loads(x)['d']})).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func3',data=json.dumps({"s":1,"d":json.loads(x)['d']})).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func4',data=json.dumps({"s":1,"d":json.loads(x)['d']})).text
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/function/func5',data=json.dumps({"s":1,"d":json.loads(x)['d']})).text
    return x
