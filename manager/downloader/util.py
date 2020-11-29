import yaml
from os import path

def getConfig():
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath,"mq-config.yaml"))

    with open(filepath, "r") as f:
        s = f.read()
        d = yaml.safe_load(s)
        return d