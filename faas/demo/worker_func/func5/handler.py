import onnxruntime as rt
import numpy as np
import orjson
import os
os.chdir(os.path.dirname(__file__))
def handle(req):
    body = orjson.loads(req)
    if(body['s']==0):
        return req
    with open('imagenet_class_index.json') as labels_file:
        labels = orjson.loads(labels_file)
    resnet_session = rt.InferenceSession("testmodel_"+str(5)+".onnx")
    input_name = resnet_session.get_inputs()[0].name
    x = np.array(body['d'],dtype=np.float32)
    x = resnet_session.run([], {input_name: x})[0]
    x = np.argmax(x)
    classify_res=labels[str(x.item())]
    return orjson.dumps({"s":1,"d":classify_res})
