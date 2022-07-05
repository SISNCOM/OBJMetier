import shutil
from pathlib import PurePath
import json
import os
from OBJMetier.commun.commun import bcolors

class imgData:

    def __init__(self, Cfg, Db):
        self.cfg = Cfg
        self.db = Db
        self.verbose = 0
        self.pathBase = self.cfg.get_data("PATH", "path_temp", "")
        self.count = 0
        self.lines = []
        self.currentLot = 0
        self.lots = []

    def readMD (self, idxImg):
        fullPath = self.pathBase + "\\INFO_"+format(int(idxImg), '06d') + ".txt"
        try:
            f = open(fullPath, "r")
            self.lines = f.readlines()
            f.close()
            msg = "MD file : " + fullPath+ ' opened !'
            bcolors.prtColor(1, msg)
            return 1
        except IOError:
            msg = "Could not read file : "+fullPath
            bcolors.prtColor(2,msg)
            return 0

    def explodeData(self):
        #ptr = self.getPtr("size")
        #ptr[0] = 128
        #
        self.count = 0
        modeAcq=0
        for line in self.lines:
            self.count += 1
            if(modeAcq==0):
                kv = self.splitKV(line)
                #print(kv)
                nu = self.kv2action(kv)
                if(nu==11):
                    modeAcq=1
            else:
                line = line.strip()
                if(line != '/ACQ'):
                    ptr = self.getLot()
                    ptr["acq"] = ptr["acq"] + line
                else:
                    modeAcq =0;

        #print(self.lots)
        return(self.count)

    def newLot(self):
        lot = {"name":'-',
               "size":[1,1,1,1],
               "scale":[1,1,1,1],
               "acq":'',
               "date":'',
               "xml":['','']
               }
        self.lots = self.lots + [lot]

    def getPtr(self, label):
        nu = self.currentLot - 1
        ptr = self.lots[nu][label]
        return ptr

    def getLot(self):
        nu = self.currentLot - 1
        ptr = self.lots[nu]
        return ptr

    def getLotNu(self, nu):
        ptr = self.lots[nu]
        return ptr

    def getNbLots(self):
        return (self.currentLot)

    #
    #   fct locale
    #
    def splitKV(self, line):
        tab = line.split(":")
        key = tab[0].strip()
        if(len(tab)>1):
            val = tab[1].strip()
        else:
            val = 0
        return {"key":key, "value":val}

    def kv2action(self, kv):

        if (kv['key'] == ""):
            return(0)
        elif (kv['key'] == "LOT"):
            self.newLot()
            self.currentLot = self.currentLot + 1
            return(1)

        elif (kv['key'] == "MODE"):
            tab = kv['value'].split(";")
            ptr = self.getPtr("size")
            ptr[2] = int(tab[1])
            return(1)

        elif (kv['key'] == "SZIMG") :
            tab = kv['value'].split(";")
            ptr = self.getPtr("size")
            ptr[0] = int(tab[0])
            ptr[1] = int(tab[1])
            return(1)

        elif  (kv['key'] == "IMG") :
            tab = kv['value'].split(",")
            ptr = self.getPtr("size")
            ptr[0] = int(tab[0])
            ptr[1] = int(tab[1])
            return(1)
        elif (kv['key'] == "SCALE"):
            tab = kv['value'].split(";")
            ptr = self.getPtr("scale")
            for x in range(4):
                ptr[x] = float(tab[x])
            return(1)

        elif ( (kv['key'] == "NAME") or (kv['key'] == "IMG_NAME") ):
            ptr = self.getLot()
            ptr["name"] = kv['value']

        elif (kv['key'] == "DATE"):
            ptr = self.getLot()
            ptr["date"] = kv['value']

        elif (kv['key'] == "XML"):
            tab = kv['value'].split(";")
            ptr = self.getPtr("xml")
            for x in range(2):
                ptr[x] = tab[x]

        elif (kv['key'] == "ACQ"):
            return(11)
        elif (kv['key'] == "/ACQ"):
            return(12)

        else:
            print(kv)
            return(0)

    def getPtrNu(self, nu, label):
        ptr = self.lots[nu][label]
        return ptr




