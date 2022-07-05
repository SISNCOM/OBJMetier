import shutil
from pathlib import PurePath
import json
import os


class step:
    def __init__(self, Cfg, Db):
        self.cfg = Cfg
        self.db = Db
        self.verbose = 0
        self.id = 0
        self.type = 0
        self.master = 0
        self.usr = 0
        self.info = []

    def read (self, id, type):
        self.type = type
        self.id = id
        if(self.type<100):
            query = f"SELECT type as master, id_usr, path_img, folder from import_img where req={type} and id={id}"
        cursor = self.db.get_cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        self.master = data[0][0]
        self.usr = data[0][1]
        self.explode(data[0][3], data[0][2])
        return(1)

    def endProcess (self, status):
        if(self.type<100):
            query = f"update import_img set nb_vues={status} where id={self.id}"
        cursor = self.db.get_cursor()
        cursor.execute(query)
        self.db.commit()
        return 1

    def getInfo(self, type):
        if(type=='usr'):
            return(self.usr);
        if (type == 'master'):
            return (self.master);
        if(type=='id_img'):
            return(self.info[0]['id_img']);
        if(type=='src'):
            return(self.info[0]['src']);
        return(-1)

    def next(self, type, img):
        if(type==30):
            info = str(img.data['id_img'])+';'+str(self.info[0]['id_img'])+";"+str(img.data['nu_vue'])+';'
            info = info + str(img.data['szz'])+';'+str(img.data['szt'])+";1"+str(self.usr)
            sql = str(type)+',0,'+str(self.master)+",'"+info+"','',0,"+str(self.usr)+'0,0,0,0'
            print(sql)

        return(0)

    ################################
    #
    #   fonction local
    #
    ##################################
    def explode(self, info1, info2):
        if (self.type == 35):
            info = self.explodeMD(info1, info2)
            self.info = [info]
            return (1)
        return(0)


    def explodeMD(self, info1, info2):
        tab1 = info1.split('@@')
        tab2 = tab1[0].split(';')
        info = {"id_img": tab2[0],
                "mode": tab2[1],
                "nu_obj": tab2[3],
                "kw": tab1[1],
                "src": info2
                }
        return(info)