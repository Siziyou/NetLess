import onnxruntime as rt
import numpy as np
import orjson
import os
os.chdir(os.path.dirname(__file__))


class worker():
    def __init__(self, req) -> None:
        self.input = orjson.loads(req)
        self.req = req
        self.signal = input['s']
        self.mapper = {
            0: self.warmup(),
            1: self.inference(),
            2: self.classify()
        }
        pass

    def process(self):
        return self.mapper[self.signal]

    def warmup(self):
        return self.req

    def inference(self):
        session = rt.InferenceSession("model.onnx")
        input_name = session.get_inputs()[0].name
        x = np.array(self.input['d'], dtype=np.float32)
        x = session.run([], {input_name: x})[0]
        return orjson.dumps({"s": 1, "d": x}, option=orjson.OPT_SERIALIZE_NUMPY)

    def classify(self):
        with open('labels.json', "rb") as labels_file:
            labels = orjson.loads(labels_file.read())
        session = rt.InferenceSession("model.onnx")
        input_name = session.get_inputs()[0].name
        x = np.array(self.input['d'], dtype=np.float32)
        x = session.run([], {input_name: x})[0]
        x = np.argmax(x)
        classify_res = labels[str(x.item())]
        return orjson.dumps({"s": 1, "d": classify_res})


def handle(req):
    instance=worker(req)
    return instance.process()