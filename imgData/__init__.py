from OBJSystem.Database.Database import Database
from OBJMetier.configuration.Configuration import Configuration
from OBJMetier.connector.connector import connector
from OBJMetier.imgData.imgData import imgData

def main():
    Cfg = Configuration()
    Cfg.path = r"C:\SISNCOM\Python\Config"
    if Cfg.checkFileExistance() < 0:
        print("Reading error")
    Db = Database(Cfg)
    Db.get_connect()
    Connector = connector(Cfg, Db)
    ok = Connector.getK("nd")
    ok = Connector.checkExec(2)
    pathImg = r"c:\\sisncom\\k\\img.tif"
    #ok = Connector.execK(pathImg, 123)
    print("get K : "+Connector.fullPath)
    #print(" => "+str(ok))
    data = imgData(Cfg, Db)
    data.readMD(123)
    data.explodeData()




if __name__ == "__main__":
    main()
