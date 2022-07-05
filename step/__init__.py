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
    
    

if __name__ == "__main__":
    main()
