import requests
import onnxruntime as rt
import json
import numpy as np
def handle(req):
    body=json.loads(req)
    resnet_session = rt.InferenceSession("testmodel_"+str(4)+".onnx")
    input_name = resnet_session.get_inputs()[0].name
    x2=np.array(body['data'])
    x2 = resnet_session.run([], {input_name: x2})[0]
    header={"X-Callback-Url":body['callback'],
        'Content-Type': 'application/json'}
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/funcrq',data=json.dumps({"callback":body['callback'],"data":x2}),headers=header)
    return
