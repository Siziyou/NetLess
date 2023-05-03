import onnxruntime as rt
import numpy as np
import orjson
import os
os.chdir(os.path.dirname(__file__))


def handle(req):
    input = orjson.loads(req)
    signal = input['s']
    if signal == 1:
        session = rt.InferenceSession("model.onnx")
        input_name = session.get_inputs()[0].name
        x = np.array(input['d'], dtype=np.float32)
        x = session.run([], {input_name: x})[0]
        return orjson.dumps({"s": 1, "d": x}, option=orjson.OPT_SERIALIZE_NUMPY)
    elif signal == 0:
        return req
