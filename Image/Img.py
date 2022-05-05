import shutil
from pathlib import PurePath
from time import sleep
from tqdm import tqdm
from OBJSystem.Database.Database import Database
import json
import os

class Img:

    def __init__(self, Cfg, Db):
        self.cfg = Cfg
        self.db = Db
        self.fullPathFile=""
        self.path = ""
        self.data = {}
        self.verbose = 0


    def info(self,id):
        cursor = self.db.get_cursor()
        query = "SELECT  id_img, texte as path, szx, szy, text as filename, nbimgcmpl as filesize  " \
                " FROM img INNER JOIN annotation " \
                "WHERE img.id_exp = annotation.idelt and img.nu_path = annotation.v1 and id_img = {};".format(id)
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            self.data = dict(id_img=row[0], path=row[1], szy=row[2], szx=row[3], filename=row[4])
        if self.verbose:print(self.data['filename'])
        return self.data


    def get_ext(self):
        info = self.data["filename"]
        ext = info.split(".")[-1]
        if self.verbose: print(ext)
        return ext

    def getFullPath(self, mode):
        if mode == 0:
            hot_storage = self.cfg.get_data("PATH_VARIABLE", "path_hot","")
            exp = self.data['path'].split("\\")[-1]+"\\"
            self.fullPathFile = hot_storage + exp + str(self.data["id_img"]) +"_" + self.data["filename"]
            try:
                if os.path.exists(self.fullPathFile):
                    return self.fullPathFile
            except IOError as e:
                if self.verbose: print(e)
        elif mode == 1:
            return self.fullPathFile
        elif mode == 2:
            cr = self.db.get_cursor()
            query = "SELECT texte FROM annotation WHERE type=14 and id={}".format(id)
            cr.execute(query)
            res, = cr.fetchone()
            return res,

    def getK(self, extension):


    def copy_imgTo(self):
        output = self.cfg.get_data("PATH_VARIABLE", "temp_copy", "")
        for i in tqdm(range(10)):
            sleep(0.2)
        shutil.copy(self.path, output)


