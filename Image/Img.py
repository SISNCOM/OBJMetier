import shutil
import copy
import json
import os
from pathlib import PurePath
from time import sleep
#from tqdm import tqdm
from OBJSystem.Database.Database import Database



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
        query = "SELECT  i.id_img, i.id_exp, i.id_scale, i.nb_slice, a.texte as path, i.szx, i.szy, " \
                "i.text as filename, i.nbimgcmpl as filesize  " \
                "FROM img i INNER JOIN annotation a on i.id_exp = a.idelt and i.nu_path = a.v1 and a.type=14 " \
                "WHERE id_img = {};".format(id)
        cursor.execute(query)
        data = cursor.fetchall()
        if(len(data) ==0):
            return(0)
        for row in data:
            self.data = dict(id_img=row[0], id_exp=row[1], scale=row[2], nb_slice=row[3], path=row[4],
                             szx=row[5],  szy=row[6], szz=1, szt=1, filename=row[7], nu_vue=1)
        if self.verbose: print(self.data['filename'])
        self.path = self.data['path']
        exp = self.path.split("\\")[-1] + "\\"
        self.hot_storage = self.cfg.get_data("PATH", "path_hot", "") + "\\"+exp
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
                if os.path.exists(self.fullPathFile) == False:
                    self.fullPathFile = self.path + "\\" + self.data["filename"]
                return self.fullPathFile
            except IOError as e:
                if self.verbose: print(e)
        elif mode == 1:
            self.fullPathFile = self.path + "\\" + self.data["filename"]
            return self.path
        elif mode == 2:
            self.fullPathFile = self.hot_storage + "\\" + self.data["filename"]
            return self.hot_storage

    def new(self):
        newId = self.db.next_id('Img','id_img')
        sql = "select max(nu_vue) from img where id_exp=(select id_exp from img where id_img="+str(self.data['id_img'])+")" \
              " and text=(select text from img where id_img="+str(self.data['id_img'])+")"
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        if (len(data) == 0):
            nuView = 1
        else:
            nuView = data[0][0] + 1
        baseTags=r""
        #--------------------------------------------------------------------------------
        sql = "insert into img (id_img,id_scale,id_sample,id_exp,nu_vue,tx_title,nb_slice,nu_path,Dim,szx,szy,tx_rmq,nb_val," \
              "is_sel,id_grp,typ_img,nbimgcmpl,text,imgcmpl,dz_slice,dt_slice,tags,type) " \
              "select  "+str(newId)+",id_scale,id_sample,id_exp,"+str(nuView)+",tx_title,0,nu_path,Dim,0,0,tx_rmq,nb_val,is_sel,id_grp," \
              "typ_img,-3,text,imgcmpl,dz_slice,dt_slice,'"+baseTags+"',type  from img where id_img="+str(self.data['id_img']);
        print(sql)
        res = cursor.execute(sql)
        self.db.commit()
        #---------------------------------------
        newImg = Img(self.cfg, self.db)
        newImg.info(newId)
        return(newImg)
