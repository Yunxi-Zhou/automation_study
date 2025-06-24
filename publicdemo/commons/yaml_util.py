import os
import yaml

# write
def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)

# read
def read_yaml(key):
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="r") as f:
        value = yaml.load(f,yaml.FullLoader)
        return value[key]

# clear
def clear_yaml():
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="w") as f:
        f.truncate()

# read testcase
def read_testcase(path):
     with open(path,encoding="utf-8",mode="r") as f:
        value = yaml.load(f,yaml.FullLoader)
        return value