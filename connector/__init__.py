from OBJSystem.Database.Database import Database
from OBJMetier.configuration.Configuration import Configuration
from OBJMetier.connector.connector import connector
def main():
    Cfg = Configuration()
    Cfg.path = r"C:\SISNCOM\Python\Config"
    if Cfg.checkFileExistance() < 0:
        print("Reading error")
    Db = Database(Cfg)
    Db.get_connect()
    Connector = connector(Cfg, Db)
    Connector.getK("nd")
    Connector.checkExec(2)



if __name__ == "__main__":
    main()
