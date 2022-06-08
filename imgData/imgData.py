import shutil
from pathlib import PurePath
import json
import os


class imgData:

    def __init__(self, Cfg, Db):
        self.cfg = Cfg
        self.db = Db
        self.verbose = 0
        self.pathBase = self.cfg.get_data("PATH", "path_temp", "")
        self.count = 0
        self.lines = []

    def readMD (self, idxImg):
        fullPath = self.pathBase + "\\INFO_"+str(idxImg) + ".txt"
        try:
            f = open(fullPath, "r")
            self.lines = f.readlines()
            f.close()
            return 1
        except IOError:
            print("Could not read file:", fullPath)
            return 0

    def explodeData(self):
        self.count = 0
        for line in self.lines:
            self.count += 1
        return(self.count)