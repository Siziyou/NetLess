import torchvision.models as model
from torchvision.models import resnet18, ResNet18_Weights
import torch.nn as nn
import copy
import torchvision.datasets as datasets
from torchvision.io import read_image
import os
os.chdir(os.path.dirname(__file__))
import json
class Predictor():
    def __init__(self) -> None:
        self.resnet34 = model.resnet34(pretrained=True)
        self.weights = ResNet18_Weights.DEFAULT
        self.r18 = resnet18(pretrained=True)
        self.src_model=self.r18
    def test_launch(self,dir):
        testpng=read_image(dir)
        preprocess=self.weights.transforms()
        testpng=preprocess(testpng)
        testpng = testpng.unsqueeze(0) 
        self.testpng=testpng
    def disassemble(self):
        child=list(self.src_model.children())
        constr_info=[]
        layer_container=[]
        temp_point=nn.Sequential()
        for i in range(0,len(child)):
            item=child[i]
            #print(type(item))
            if(isinstance(item,nn.Sequential)):
                if(temp_point is not None):
                    layer_container.append(copy.deepcopy(temp_point))
                    temp_point=None
                layer_container.append(item)
            else:
                if(temp_point is not None):
                    temp_point.add_module(str(i),item)
                else:
                    temp_point=nn.Sequential(item)
        if(temp_point is not None):
            layer_container.append(copy.deepcopy(temp_point))
        # print(layer_container)
        # print(len(layer_container))
        self.layer_container=layer_container
    def launch_countainer(self):
        x=self.testpng
        self.r18.eval()
        res1=self.r18(self.testpng).argmax(dim=1)
        with open('imagenet_class_index.json') as labels_file:
            labels = json.load(labels_file)
        print(f"Prediction for Dog {1}: {labels[str(res1.item())]}")
        for model in self.layer_countainer:
            print(model)
            model.eval()
            x=model(x)
        print(f"Prediction for Dog {1}: {labels[str(x.item())]}")
new_instance=Predictor()
new_instance.test_launch()
new_instance.disassemble()
new_instance.launch_countainer()



