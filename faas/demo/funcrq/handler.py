import onnxruntime as rt
import json
import numpy as np
def handle(req):
    body=json.loads(req)
    resnet_session = rt.InferenceSession("testmodel_"+str(5)+".onnx")
    input_name = resnet_session.get_inputs()[0].name
    x2=np.array(body['data'])
    x2 = resnet_session.run([], {input_name: x2})[0]
    with open('imagenet_class_index.json') as labels_file:
        labels = json.load(labels_file)
    x2 = np.argmax(x2)
    print(f"Prediction res: {labels[str(x2.item())]}")
    return x2+" "+labels[str(x2.item())]
