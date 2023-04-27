from torchvision.io import read_image
from torchvision.models import resnet18, ResNet18_Weights
import torchvision.models as model
import os
import numpy as np
import time
import orjson
os.chdir(os.path.dirname(__file__))
import requests
class Requster():
    def __init__(self,transformer) -> None:
        self.transformer = transformer

    def test_load(self, dir):
        pridata = read_image(dir)
        pridata = self.transformer(pridata)
        pridata = pridata.unsqueeze(0)
        return pridata

    def img2tensor_save(self):
        pass

    def pre_process(self):
        # process data here
        pass
    def request_jpg(self,pic_dir):
        data= np.array(self.test_load(pic_dir))
        print(data.shape)
        print(data.dtype)
        # x = requests.post('http://127.0.0.1:31112/function/cf',data=orjson.dumps({"s":1,"d":data},option=orjson.OPT_SERIALIZE_NUMPY))
        T1 = time.time()
        x = requests.post('http://127.0.0.1:31112/function/controller',data=orjson.dumps({"s":1,'d':data},option=orjson.OPT_SERIALIZE_NUMPY))
        T2 = time.time()
        print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))
        with open('t.txt', 'w') as f:
            f.write(x.text)
        return x.text

if __name__ == "__main__":
    # resnet34 = model.resnet34(pretrained=True)
    with open('imagenet_class_index.json') as labels_file:
        labels = orjson.loads(labels_file.read())
    print(type(labels))
    weights = ResNet18_Weights.DEFAULT.transforms()
    src_model = model.resnet18(pretrained=True)
    new_instance = Requster(transformer=weights)
    res=(new_instance.request_jpg(pic_dir="./pictures/8.jpg"))
    # print(res)
