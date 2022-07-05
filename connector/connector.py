import shutil
from pathlib import PurePath
import json
import os


# This class is used to execute a program that will create a new image from a source image
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
        s  = data[0][1]
        i = s.rfind('\\')
        if(i<0):
            i = s.rfind('/')
        if(i>=0):
            s = s[i+1:]
        self.exec = s

        return self.idK

    # mode : 1:copy, 2:MD, 3:stamp
    def checkExec(self, mode):
        path = self.cfg.get_data("PATH", "connector", "")
        i = self.exec.rfind('.exe')
        if(i>0):
            prg = self.exec[:i+4]
            cmpl = self.exec[i+5:]
        else:
            prg = self.exec
            cmpl = r""

        self.fullPath = path + "\\" + prg
        if os.path.exists(self.fullPath):
            if(cmpl==""):
                if mode == 1:
                    cmpl = r" -copy "
                elif mode == 2 :
                    cmpl = r" -md "
                else:
                    cmpl = r" -stamp "
            self.fullPath += cmpl
            return True

        if mode == 2:
            exec = 'md' + prg
        else:
            exec = 'img' + prg

        self.fullPath = path + "\\" + exec
        if os.path.exists(self.fullPath):
            self.fullPath += cmpl
            return True

        return False

    def execK(self, src, idxImg, nuStack):
        tmpPath = self.cfg.get_data("PATH", "path_temp", "")
        cmd = self.fullPath + ' "' + src + '" "' + tmpPath + '" ' + str(idxImg) + ' '+ str(nuStack)
        print(cmd)
        resu = 'x'
        #resu = os.system(cmd)


        return resu
