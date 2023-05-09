import onnxruntime as rt
import numpy as np
import orjson
import os
os.chdir(os.path.dirname(__file__))


def handle(req):
    input = orjson.loads(req)
    if input['s'] == 1:
        counter=0
        filelist=os.listdir("./")
        for name in filelist:
            if("onnx" in name):
                counter+=1
        x = np.array(input['d'], dtype=np.float32)
        for i in range(counter):
            resnet_session = rt.InferenceSession(str(i)+".onnx")
            input_name = resnet_session.get_inputs()[0].name
            x = resnet_session.run([], {input_name: x})[0]
        return orjson.dumps({"s": 1, "d": x}, option=orjson.OPT_SERIALIZE_NUMPY)
    elif input['s'] == 0:
        return req
