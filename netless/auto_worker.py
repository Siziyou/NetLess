import os
import json
import shutil
import yaml
os.chdir(os.path.dirname(__file__))


class auto_worker():
    def __init__(self, MODEL_SAVE_DIR="./src/models/", CONFIG_DIR="./src/", WORKER_DIR="./worker_func/", VERSION="1.0.3", USER="boilfish", GATEWAY_ADDR="127.0.0.1:31112", TEMPLATE_DIR="./template") -> None:

        self.MODEL_SAVE_DIR = MODEL_SAVE_DIR
        self.CONFIG_DIR = CONFIG_DIR
        self.WORKER_DIR = WORKER_DIR
        self.VERSION = VERSION
        self.USER = USER
        self.TEMPLATE_DIR = TEMPLATE_DIR
        self.GATEWAY_ADDR = GATEWAY_ADDR
        with open(self.CONFIG_DIR+'configure.json') as configure_file:
            self.configure = json.load(configure_file)

    def create_funcs(self):
        def create_yaml_dict(gateway, func_dict, fass_version="1.0"):
            yaml_template_dict = {
                "functions": func_dict,
                "provider":
                {"name": "openfaas",
                 "gateway": gateway
                 },
                "version": fass_version
            }
            return yaml_template_dict

        def create_func_dict(func_name, lang_name, image_prefix, version):
            func_dict = {
                func_name:
                    {"lang": lang_name,
                     "handler": "./"+func_name,
                     "image": image_prefix+"/"+func_name+":"+version
                     }
            }
            return func_dict

        if(not os.path.isdir(self.WORKER_DIR)):
            # mkdir
            os.mkdir(self.WORKER_DIR)
        # copy template to worker_func_dir
        shutil.copytree(self.TEMPLATE_DIR, self.WORKER_DIR+"template")
        # start autocreate
        os.chdir(self.WORKER_DIR)
        fdict = {}
        keys = list(self.configure['f'].keys())
        # create worker
        for key in self.configure['f']:
            os.system(
                "faas-cli new "+key+" --lang worker --quiet")
            fdict[key] = create_func_dict(
                func_name=key, lang_name="worker", image_prefix=self.USER, version=self.VERSION)[key]
            os.remove(key+".yml")
        # generate stack yaml file
        os.system(
            "faas-cli new controller --lang controller --quiet")
        fdict["controller"]=create_func_dict("controller","controller",self.USER,self.VERSION)["controller"]
        os.remove("controller.yml")
        ydict = create_yaml_dict(gateway=self.GATEWAY_ADDR, func_dict=fdict)
        with open("./stack.yml", "w") as f:
            yaml.dump(ydict, f)
        # create controller

        pass

    def assemble(self):
        # asseble model file and classify source
        os.chdir(os.path.dirname(__file__))
        if(os.path.isdir(self.MODEL_SAVE_DIR)):
            for i in range(self.configure['l']):
                shutil.copy(self.MODEL_SAVE_DIR+"testmodel_"+str(i) +
                            ".onnx", self.WORKER_DIR+"func"+str(i)+"/model.onnx")
            shutil.copytree(self.CONFIG_DIR+"classify_src", self.WORKER_DIR+"controller/classify_src")
            shutil.copy(self.CONFIG_DIR+"configure.json",self.WORKER_DIR+"controller/configure.json")
            pass
        pass


if __name__ == "__main__":
    version="1.0.4"
    new_instance = auto_worker(VERSION=version)
    new_instance.create_funcs()
    new_instance.assemble()
