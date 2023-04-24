import onnxruntime as rt
import orjson
import numpy as np
import os
os.chdir(os.path.dirname(__file__))

def handle(req):
    body = orjson.loads(req)
    if(body['s']==0):
        return req
    resnet_session = rt.InferenceSession("testmodel_"+str(3)+".onnx")
    input_name = resnet_session.get_inputs()[0].name
    x = np.array(body['d'],dtype=np.float32)
    x = resnet_session.run([], {input_name: x})[0]
    return orjson.dumps({"s":1,"d":x},option=orjson.OPT_SERIALIZE_NUMPY)
