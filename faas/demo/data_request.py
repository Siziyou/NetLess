import json
from torchvision.io import read_image
from torchvision.models import resnet18, ResNet18_Weights
import torchvision.models as model
import os
import base64
import numpy as np
import pickle
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
    def request_jpg(self,callback_url,pic_dir):
        x2 = np.array(self.test_load(pic_dir))
        #np.savez_compressed("test.npy",x2)
        header={"X-Callback-Url":callback_url}
        print(x2.shape)
        #x = requests.post('http://127.0.0.1:31112/async-function/fun1',files={'file': open("test.npy.npz",'rb')},headers=header)
        x = requests.post('http://127.0.0.1:31112/function/fun1',data=json.dumps({"data":x2.tolist()}),headers=header)
        return {"req":len(x2),"x.status_code":x.status_code,"x.reason":x.reason,"x.apparent_encoding":x.apparent_encoding}
        return x.text

if __name__ == "__main__":
    # resnet34 = model.resnet34(pretrained=True)
    weights = ResNet18_Weights.DEFAULT.transforms()
    src_model = model.resnet18(pretrained=True)
    new_instance = Requster(transformer=weights)
    print(new_instance.request_jpg(callback_url="https://eok91wsffo1l8jc.m.pipedream.net",pic_dir="./pictures/5.jpg"))
