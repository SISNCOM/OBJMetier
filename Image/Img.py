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
        self.hot_storage = ""
        self.path = ""
        self.fullPathFile = ""
        self.data = {}
        self.verbose = 0

    def info(self, id):
        cursor = self.db.get_cursor()
        query = "SELECT  i.id_img, a.texte as path, i.szx, i.szy, i.text as filename, i.nbimgcmpl as filesize  " \
                "FROM img i INNER JOIN annotation a on i.id_exp = a.idelt and i.nu_path = a.v1 and a.type=14 " \
                "WHERE id_img = {};".format(id)
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            self.data = dict(id_img=row[0], path=row[1], szy=row[2], szx=row[3], filename=row[4])
        if self.verbose: print(self.data['filename'])
        self.path = self.data['path']
        exp = self.path.split("\\")[-1] + "\\"
        self.hot_storage = self.cfg.get_data("PATH_VARIABLE", "path_hot", "") + exp
        return self.data

    def get_ext(self):
        info = self.data["filename"]
        ext = info.split(".")[-1]
        if self.verbose: print(ext)
        return ext

    # mode:0 Rd(chaud ou froid) 1: froid, 2:chaud
    def getFullPath(self, mode):
        if mode == 0:
            self.fullPathFile = self.hot_storage + "\\" + self.data["filename"]
            try:
                if os.path.exists(self.fullPathFile) == false:
                    self.fullPathFile = self.path + self.data["filename"]
                return self.fullPathFile
            except IOError as e:
                if self.verbose: print(e)
        elif mode == 1:
            self.fullPathFile = self.path + self.data["filename"]
            return self.path
        elif mode == 2:
            self.fullPathFile = self.hot_storage + self.data["filename"]
            return self.hot_storage

    def getK(self, extension):
        query = "SELECT texte FROM annotation WHERE type=14 and id={}".format(id)
        cr.execute(query)
        res, = cr.fetchone()
        return res,

    def copy_imgTo(self):
        output = self.cfg.get_data("PATH_VARIABLE", "temp_copy", "")
        for i in tqdm(range(10)):
            sleep(0.2)
        shutil.copy(self.path, output)
