import shutil
from pathlib import PurePath
import json
import os

class script:
    def __init__(self, Cfg, Db):
        self.cfg = Cfg
        self.db = Db
        self.verbose = 0
        self.basePath = self.cfg.get_data("PATH", "base_script", "")
        self.basefile = ""
        self.script = ""

    def open(self, filename):
        self.basefile = self.basePath+"\\"+filename
        try:
            f = open(self.basefile, "r")
            self.script = f.read()
            f.close()
            return 1
        except IOError:
            print("Could not read file:", self.basefile)
            return 0

    def replace(self, key, value):
        key2 = "<" + key + ">"
        if self.script.find(key2) == -1:
            return 0
        self.script = self.script.replace(key2, value)
        return 1

    # keys = {'key1':value, 'img':'fileXX.tif','id_img':123, ...}
    def update(self, keys):
        nb = 0
        for key in keys:
            val = keys[key]
            nb += self.script.replace(key,val)
        return nb

    def save(self, filename):
        destfile = self.basePath + "\\" + filename
        try:
            f = open(destfile, "w")
            f.write(self.script)
            f.close()
            return 1
        except IOError:
            print("Could not read file:", destfile)
            return 0





