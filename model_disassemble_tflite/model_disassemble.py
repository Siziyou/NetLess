import json
from torchvision.io import read_image
import torch
import copy
import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights
import torchvision.models as model
import os
os.chdir(os.path.dirname(__file__))
PICTURE_DIR = "./src/pictures/"
INDEX_DIR = "./src/"
MODEL_SAVE_DIR = "./src/models/"
CONFIG_DIR = "./src/"


class Predictor():
    def __init__(self) -> None:
        self.resnet34 = model.resnet34(pretrained=True)
        self.weights = ResNet18_Weights.DEFAULT
        self.flatten = False
        self.constr_info = {}
        self.layer_container = []
        self.input=[]
        self.output=[]
        with open(INDEX_DIR+'imagenet_class_index.json') as labels_file:
            self.labels = json.load(labels_file)
        self.disassemble_mode=True
    def __str__(self) -> str:
        print("Printing model config:")
        print(self.constr_info)
        print("Printing disassembled model layers:")
        print(self.layer_container)

    def test_launch(self, dir):
        testpng = read_image(dir)
        preprocess = self.weights.transforms()
        testpng = preprocess(testpng)
        testpng = testpng.unsqueeze(0)
        self.testpng = testpng
        print(testpng)
    def img2tensor_save(self):
        pass
    def disassemble(self, flatten):
        self.flatten = flatten
        child = list(self.src_model.children())
        temp_point = nn.Sequential()
        for i in range(0, len(child)):
            item = child[i]
            if(isinstance(item, nn.Sequential)):
                if(temp_point is not None):
                    self.layer_container.append(copy.deepcopy(temp_point))
                    temp_point = None
                self.layer_container.append(item)
            else:
                if(temp_point is not None):
                    if(item == child[-1] and self.flatten):
                        temp_point.add_module(str(i)+"flatten", nn.Flatten())
                    temp_point.add_module(str(i), item)
                else:
                    temp_point = nn.Sequential(item)
        if(temp_point is not None):
            self.layer_container.append(copy.deepcopy(temp_point))
        self.layer_container = self.layer_container
        self.constr_info['lenth'] = len(self.layer_container)
    def pre_process(self):
        #process data here
        pass
    def dump_disassembled_file(self):
        counter = 0
        for model in self.layer_container:
            torch.save(model, MODEL_SAVE_DIR+"testmodel_"+str(counter)+".pth")
            counter += 1
        with open(CONFIG_DIR + "configure.json",'w') as f:
            json.dump(self.constr_info,f)
        pass
    def launch_disassembled_file(self,config_dir,model_dir):
        with open (config_dir+"configure.json") as f_1:
            self.constr_info=json.load(f_1)
        for i in range(self.constr_info['lenth']):
            self.layer_container.append(torch.load(model_dir+"testmodel_"+str(i)+".pth"))
        # tmodel = torch.load("resnet18.pth")
        pass
    def predict(self):
        x = self.testpng
        for model in self.layer_container:
            # print(model) #output model
            model.eval()
            x = model(x)
        x = x.argmax(dim=1)
        return (f"Prediction res: {self.labels[str(x.item())]}")
if __name__ == "__main__":
    new_instance = Predictor()
    new_instance.test_launch(PICTURE_DIR + "111.jpg")
    #new_instance.disassemble(flatten=True)
    #new_instance.dump_disassembled_file()
    new_instance.launch_disassembled_file(CONFIG_DIR,MODEL_SAVE_DIR)
    res=new_instance.predict()
    print(res)
