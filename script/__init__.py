from OBJMetier.configuration.Configuration import Configuration
from OBJSystem.Database.Database import Database
from OBJMetier.script.script import script


def main():
    Cfg = Configuration()
    Cfg.path = r"C:\SISNCOM\Python\Config"
    if Cfg.checkFileExistance() < 0:
        print("Reeading error")
    #----------------------
    Db = Database(Cfg)
    Db.get_connect()
    #---------------------
    Script = script(Cfg, Db)
    # Appeler les méthodes issues de la class script
    Script.open(r"test.txt")
    Script.replace("path", r"c:\\image")
    Script.save(r"resu.txt")



if __name__ == "__main__":
    main()
