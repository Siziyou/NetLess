import json
from torchvision.io import read_image
import torch
import copy
import torch.nn as nn
from torchvision.models import resnet18, resnet34, resnet50, resnet101, resnet152, ResNet18_Weights, ResNet34_Weights, ResNet50_Weights, ResNet101_Weights, ResNet152_Weights
import torchvision.models as model
import os
import onnxruntime as rt
import numpy as np

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.m1=nn.Sequential(resnet101(pretrained=True))
        self.m2=nn.Sequential(resnet152(pretrained=True))
    def forward(self,input):
        a=self.m1(input)
        b=self.m2(input)
        return a
        
os.chdir(os.path.dirname(__file__))
PICTURE_DIR = "./pictures/"
INDEX_DIR = "./src/"
MODEL_SAVE_DIR = "./src/models/"
CONFIG_DIR = "./src/"
batch_size = 1  # 批处理大小
input_shape = (3, 224, 224)  # 输入数据,改成自己的输入shape
input = torch.randn(batch_size, *input_shape)   # 生成张量


class disassembler():
    def __init__(self, src_model, transformer, Primary_Data_DIR,flatten=False,async_flag=[]) -> None:
        self.flatten = False
        self.constr_info = {}
        self.layer_container = []
        self.input = []
        self.output = []
        self.src_model = src_model
        self.transformer = transformer
        self.disassemble_mode = True
        self.PrimaryData = self.load_pic(Primary_Data_DIR)
        self.flatten=flatten
        self.async_flag=async_flag
    def __str__(self) -> str:
        print("Printing model config:")
        print(self.constr_info)
        print("Printing disassembled model layers:")
        print(self.layer_container)

    def load_pic(self, dir):
        pridata = read_image(dir)
        pridata = self.transformer(pridata)
        pridata = pridata.unsqueeze(0)
        return pridata

    def disassemble(self):
        child = list(self.src_model.children())
        temp_point = None
        for i in range(0, len(child)):
            item = child[i]
            if (isinstance(item, nn.Sequential)):
                if (temp_point is not None):
                    self.layer_container.append(copy.deepcopy(temp_point))
                    temp_point = None
                self.layer_container.append(item)
            else:
                if (temp_point is not None):
                    if (item == child[-1] and self.flatten):
                        temp_point.add_module(str(i)+"flatten", nn.Flatten())
                    temp_point.add_module(str(i), item)
                else:
                    temp_point = nn.Sequential(item)
        if (temp_point is not None):
            self.layer_container.append(copy.deepcopy(temp_point))
        self.layer_container = self.layer_container
        self.constr_info['l'] = len(self.layer_container)
        self.constr_info['f'] = {}
        for i in range(self.constr_info['l']-1):
            self.constr_info['f']['func'+str(i)] = 1
        self.constr_info['f']['func'+str(self.constr_info['l']-1)] = 2
        self.constr_info['a'] = self.async_flag
        print(self.layer_container)
    def dump_disassembled_file(self):
        counter = 0
        if(not os.path.isdir(MODEL_SAVE_DIR)):
            os.mkdir(MODEL_SAVE_DIR)
        x = copy.deepcopy(self.PrimaryData)
        self.src_model.eval()
        shape = list(x.shape)
        input = torch.randn(1, shape[1], shape[2], shape[3])
        torch.onnx.export(self.src_model, input, MODEL_SAVE_DIR +
                              "testmodel_total.onnx", export_params=True,
                              opset_version=10,    # the ONNX version to export the model to
                              do_constant_folding=True,  # whether to execute constant folding for optimization
                              # the model's input names
                              input_names=['modelInput'],
                              # the model's output names
                              output_names=['modelOutput'],
                              dynamic_axes={'modelInput': {0: 'batch_size'},    # variable length axes
                                            'modelOutput': {0: 'batch_size'}})
        counter=0
        for model in self.layer_container:
            model.eval()
            print(counter)
            if(self.async_flag==[0,1]):
                x=copy.deepcopy(self.PrimaryData)
            shape = list(x.shape)
            input = torch.randn(1, shape[1], shape[2], shape[3])
            x = model(x)
            torch.save(model, MODEL_SAVE_DIR+"testmodel_"+str(counter)+".pth")
            torch.onnx.export(model, input, MODEL_SAVE_DIR +
                              "testmodel_"+str(counter)+".onnx", export_params=True,
                              opset_version=10,    # the ONNX version to export the model to
                              do_constant_folding=True,  # whether to execute constant folding for optimization
                              # the model's input names
                              input_names=['modelInput'],
                              # the model's output names
                              output_names=['modelOutput'],
                              dynamic_axes={'modelInput': {0: 'batch_size'},    # variable length axes
                                            'modelOutput': {0: 'batch_size'}})
            counter += 1
        with open(CONFIG_DIR + "configure.json", 'w') as f:
            json.dump(self.constr_info, f)
        pass

    def load_disassembled_file(self, config_dir, model_dir):
        with open(config_dir+"configure.json") as f_1:
            self.constr_info = json.load(f_1)
        for i in range(self.constr_info['l']):
            self.layer_container.append(torch.load(
                model_dir+"testmodel_"+str(i)+".pth"))
        pass

    def testonnx_func(self, config_dir, model_dir, data_dir):
        with open(INDEX_DIR+'classify_src/labels.json') as labels_file:
            self.labels = json.load(labels_file)
        # Loading Configuration
        self.src_model.eval()
        with open(config_dir+"configure.json") as f_1:
            self.constr_info = json.load(f_1)
        for i in range(self.constr_info['l']):
            self.layer_container.append(torch.load(
                model_dir+"testmodel_"+str(i)+".pth"))
        for i in range(1, 100):
            # Input
            self.PrimaryData = self.load_pic(data_dir+str(i+1)+".jpg")
            x2 = np.array(self.PrimaryData)
            x = self.PrimaryData
            x3 = copy.deepcopy(self.PrimaryData)
            counter = 0
            for j in range(self.constr_info['l']):
                resnet_session = rt.InferenceSession(
                    model_dir+"testmodel_"+str(j)+".onnx")
                input_name = resnet_session.get_inputs()[0].name
                x2 = resnet_session.run([], {input_name: x2})[0]
                counter += 1
                del resnet_session
                self.layer_container[j].eval()
                x = self.layer_container[j](x)
            x = x.argmax(dim=1)
            x2 = np.argmax(x2)
            x3 = self.src_model(x3)
            x3 = x3.argmax(dim=1)
            if (x.item() == x2.item()):
                if (x2.item() == x3.item()):
                    print(f"Prediction res: {self.labels[str(x.item())]}")
        pass

    def predict(self):
        with open(INDEX_DIR+'lables.json') as labels_file:
            self.labels = json.load(labels_file)
        x = self.PrimaryData
        for model in self.layer_container:
            # print(model) #output model
            model.eval()
            x = model(x)
        x = x.argmax(dim=1)
        return (f"Prediction res: {self.labels[str(x.item())]}")


if __name__ == "__main__":
    weights = ResNet34_Weights.DEFAULT.transforms()
    src_model = resnet101(pretrained=True)
    async_flag=[0,1]
    testmodel=Model()
    print(testmodel)
    new_instance = disassembler(src_model=testmodel, transformer=weights,
                             Primary_Data_DIR="./pictures/"+str(1)+".jpg",flatten=False,async_flag=async_flag)
    new_instance.disassemble()
    new_instance.dump_disassembled_file()
    

    # res = new_instance.predict()
    # print(res)
    # new_instance.src_model.eval()
    # new_instance.testonnx_func(CONFIG_DIR, MODEL_SAVE_DIR, PICTURE_DIR)
    # new_instance.load_disassembled_file(CONFIG_DIR,MODEL_SAVE_DIR)
