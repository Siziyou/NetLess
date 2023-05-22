from torchvision.io import read_image
from torchvision.models import ResNet18_Weights
import os
import numpy as np
import time
import orjson
import asyncio
from aiohttp import ClientSession
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
        T1 = time.time()
        n=6
        for i in range(n):
            x = requests.post('http://127.0.0.1:31112/function/func0',data=orjson.dumps({"s":0,'d':data},option=orjson.OPT_SERIALIZE_NUMPY))
        T2 = time.time()
        print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))
        print(((T2 - T1)*1000)/n)
        return x.text
    def workloadtest1(self,pic_dir):
        data= np.array(self.test_load(pic_dir))
        data=orjson.dumps({"s":0,'d':data},option=orjson.OPT_SERIALIZE_NUMPY)
        T1 = time.time()
        async def func1():
            print('协程1:controller101s')
            async with ClientSession() as session:
                async with session.post('http://127.0.0.1:31112/function/controller101s',data=data) as response:
                    # print(await response.text())
                    # print(res)
                    print('协程1:controller101s end')
        async def func2():
            print('协程2:controller152s')
            async with ClientSession() as session:
                async with session.post('http://127.0.0.1:31112/function/controller152s',data=data) as response:
                    # print(await response.text())
                    # print(res)
                    print('协程2:controller152s end')
        task = [func1(), func2()]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(task))
        T2=time.time()
        print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))
        pass
    def workloadtest2(self,pic_dir):
        data= np.array(self.test_load(pic_dir))
        data=orjson.dumps({"s":0,'d':data},option=orjson.OPT_SERIALIZE_NUMPY)
        T1 = time.time()
        x = requests.post('http://127.0.0.1:31112/function/controller101s',data=data)
        # x = requests.post('http://127.0.0.1:31112/function/controller152s',data=data)
        T2=time.time()
        print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))
        pass

if __name__ == "__main__":
    weights = ResNet18_Weights.DEFAULT.transforms()
    new_instance = Requster(transformer=weights)
    # res=(new_instance.request_jpg(pic_dir="./pictures/5.jpg"))
    # print(res)
    new_instance.workloadtest1(pic_dir="./pictures/3.jpg")
    new_instance.workloadtest2(pic_dir="./pictures/3.jpg")