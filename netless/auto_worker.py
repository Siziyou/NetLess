import os
import json
import shutil
import yaml
os.chdir(os.path.dirname(__file__))


class auto_worker():
    def __init__(self, MODEL_SAVE_DIR="./src/models/", CONFIG_DIR="./src/", WORKER_DIR="./worker_func/", VERSION="1.0.3", USER="boilfish", GATEWAY_ADDR="127.0.0.1:31112", TEMPLATE_DIR="./template", MEMORY_LIMIT=256*1024*1024) -> None:
        self.MEMORY_LIMIT = MEMORY_LIMIT
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
        fdict["controller"] = create_func_dict(
            "controller", "controller", self.USER, self.VERSION)["controller"]
        os.remove("controller.yml")
        ydict = create_yaml_dict(gateway=self.GATEWAY_ADDR, func_dict=fdict)
        with open("./stack.yml", "w") as f:
            yaml.dump(ydict, f)
        # create controller

        pass

    def assemble(self):
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

        def assemble_merge(memory_limit, model_list):
            # algorithm init
            lenth = len(model_list)
            assemble_config = []
            for i in range(lenth):
                assemble_config.append(0)
            # online process
            memory_total = model_list[0][0]
            counter = 1
            for i in range(1, lenth):
                if(model_list[i][0]) < memory_limit-memory_total:
                    # print(1,model_list[i],memory_total)
                    assemble_config[i] = counter
                    counter += 1
                    memory_total += model_list[i][0]
                else:
                    # print(0,model_list[i],memory_total)
                    assemble_config[i] = 0
                    counter = 1
                    memory_total = model_list[i][0]
            return assemble_config
        # asseble model file and classify source
        model_list = []
        os.chdir(os.path.dirname(__file__))
        if(os.path.isdir(self.MODEL_SAVE_DIR)):
            for i in range(self.configure['l']):
                fsize = os.path.getsize(
                    self.MODEL_SAVE_DIR+"testmodel_"+str(i) + ".onnx")
                model_list.append(
                    (fsize, self.MODEL_SAVE_DIR+"testmodel_"+str(i) + ".onnx"))
            #     shutil.copy(self.MODEL_SAVE_DIR+"testmodel_"+str(i) +
            #                 ".onnx", self.WORKER_DIR+"func"+str(i)+"/model.onnx")

            assemble_config = assemble_merge(
                model_list=model_list, memory_limit=self.MEMORY_LIMIT)
            print(model_list)
            print(assemble_config)
            func_counter = 0
            if(not os.path.isdir(self.WORKER_DIR)):
                # mkdir
                os.mkdir(self.WORKER_DIR)
            # copy template to worker_func_dir
            shutil.copytree(self.TEMPLATE_DIR, self.WORKER_DIR+"template")
            # start autocreate
            os.chdir(self.WORKER_DIR)
            fdict = {}
            init_flag = 0
            # create worker
            for i in range(len(assemble_config)):
                if(assemble_config[i] == 0):
                    if(init_flag):
                        func_counter +=1
                    else:
                        init_flag = 1
                    os.system(
                        "faas-cli new "+"func"+str(func_counter)+" --lang worker --quiet")
                    fdict["func"+str(func_counter)] = create_func_dict(
                        func_name="func"+str(func_counter), lang_name="worker", image_prefix=self.USER, version=self.VERSION)["func"+str(func_counter)]
                    os.remove("func"+str(func_counter)+".yml")
                shutil.copy("."+model_list[i][1], "./func" +
                            str(func_counter)+"/"+str(assemble_config[i])+".onnx")
            # generate stack yaml file
            os.system(
                "faas-cli new controller --lang controller --quiet")
            func_list=list(fdict.keys())
            config_dict={}
            for name in func_list:
                if name==func_list[-1]:
                    config_dict[name]=2
                else:
                    config_dict[name]=1
            with open('./controller/configure.json', 'w') as f:
                json.dump(config_dict, f)
            controller_dict=create_func_dict(
                "controller", "controller", self.USER, self.VERSION)
            fdict["controller"] = controller_dict["controller"]
            ydict = create_yaml_dict(
                gateway=self.GATEWAY_ADDR, func_dict=fdict)
            with open("./stack.yml", "w") as f:
                yaml.dump(ydict, f)
            with open("./controller.yml", "w") as f:
                yaml.dump(create_yaml_dict(gateway=self.GATEWAY_ADDR,func_dict=controller_dict), f)
            os.chdir(os.path.dirname(__file__))
            shutil.copytree(self.CONFIG_DIR+"classify_src",
                            self.WORKER_DIR+"controller/classify_src")
        pass
if __name__ == "__main__":
    version = "1.0.6"
    MEMORY_LIMIT = 128*1024*1024
    new_instance = auto_worker(VERSION=version, MEMORY_LIMIT=MEMORY_LIMIT)
    new_instance.assemble()
