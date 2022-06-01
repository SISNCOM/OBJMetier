from OBJMetier.configuration.Configuration import Configuration
from OBJSystem.Database.Database import Database
from OBJMetier.Image.Img import Img


def main():
    Cfg = Configuration()
    Cfg.path = r"C:\SISNCOM\Python\Config"
    if Cfg.checkFileExistance() < 0:
        print("Reading error")
    Db = Database(Cfg)
    Db.get_connect()
    img = Img(Cfg, Db)
    img.info(1)
    ext = img.get_ext()
    print(ext)
    #CopyImg.copy()



if __name__ == "__main__":
    main()
