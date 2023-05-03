import os
import json
import shutil
import yaml
os.chdir(os.path.dirname(__file__))
class auto_worker():
    def __init__(self, MODEL_SAVE_DIR="./src/models/", CONFIG_DIR="./src/", WORKER_DIR="./worker_func/", VERSION="1.0.3", USER="boilfish", GATEWAY_ADDR="127.0.0.1:31112") -> None:
        """_summary_

        Args:
            MODEL_SAVE_DIR (str, optional): _description_. Defaults to "./src/models/".
            CONFIG_DIR (str, optional): _description_. Defaults to "./src/".
            WORKER_DIR (str, optional): _description_. Defaults to "./worker_func/".
            VERSION (str, optional): _description_. Defaults to "1.0.3".
            USER (str, optional): _description_. Defaults to "boilfish".
            GATEWAY_ADDR (str, optional): _description_. Defaults to "127.0.0.1:31112".
        """        
        self.MODEL_SAVE_DIR = MODEL_SAVE_DIR
        self.CONFIG_DIR = CONFIG_DIR
        self.WORKER_DIR = WORKER_DIR
        self.VERSION = VERSION
        self.USER = USER
        self.GATEWAY_ADDR = GATEWAY_ADDR
        with open(self.CONFIG_DIR+'configure.json') as configure_file:
            self.configure = json.load(configure_file)

    def create_worker(self):
        if(not os.path.isdir(self.WORKER_DIR)):
            os.mkdir(self.WORKER_DIR)
        os.chdir(self.WORKER_DIR)
        fdict={}
        keys = list(self.configure['f'].keys())
        for key in self.configure['f']:
            os.system(
                "faas-cli new "+key+" --lang worker -q")
            fdict[key]=self.create_func_dict(func_name=key,lang_name="worker",image_prefix=self.USER,version=self.VERSION)[key]
            os.remove(key+".yml")
        ydict=self.create_yaml_dict(gateway=self.GATEWAY_ADDR,func_dict=fdict)
        with open("./stack.yml","w") as f:
            yaml.dump(ydict,f)
        pass

    def create_yaml_dict(self, gateway, func_dict,fass_version="1.0.0"):        
        yaml_template_dict = {
            "functions": func_dict,
            "provider":
            {"name": "openfaas",
             "gateway": gateway
             },
            "version":fass_version
        }
        return yaml_template_dict

    def create_func_dict(self,func_name, lang_name, image_prefix, version):
        func_dict = {
            func_name:
                {"lang": lang_name,
                 "handler": "./"+func_name,
                 "image": image_prefix+"/"+func_name+":"+version
                 }
        }
        return func_dict

    def assemble(self):
        os.chdir(os.path.dirname(__file__))
        if(os.path.isdir(self.MODEL_SAVE_DIR)):
            pass
        pass


if __name__ == "__main__":
    new_instance = auto_worker()
    new_instance.create_worker()
