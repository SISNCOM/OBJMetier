import shutil
from pathlib import PurePath
import json
import os


class connector:

    def __init__(self, Cfg, Db):
        self.cfg = Cfg
        self.db = Db
        self.verbose = 0
        self.idK = 0
        self.exec = ""
        self.fullPath = ''

    def getK(self, extension):
        query = "SELECT id, text FROM listing WHERE type=4 and rmq like '{};%' ".format(extension)
        cursor = self.db.get_cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        # for row in data:
        self.idK = data[0][0]
        self.exec = data[0][1]
        return self.idK

    # mode : 1:copy, 2:MD, 3:stamp
    def checkExec(self, mode):
        path = self.cfg.get_data("PATH", "connector", "")
        if mode == 1:
            exec = self.exec
        elif mode == 2:
            exec = 'md' + self.exec
        else:
            exec = 'img' + self.exec

        self.fullPath = path + "\\" + exec
        if os.path.exists(self.fullPath):
            return True

        return False

    def exec(self, src, idxImg):
        tmpPath = self.cfg.get_data("PATH_TMP", "path_tmp", "")
        cmd = self.fullPath + ' ' + src + ' ' + tmpPath + ' ' + idxImg
        resu = os.system(cmd)
        return resu
