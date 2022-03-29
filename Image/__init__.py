__all__ = ['Database']

from OBJMetier.configuration.Configuration import Configuration
from OBJSystem.Database.Database import Database
from OBJMetier.Image.Img import Img


def main():
    Cfg = Configuration()
    Cfg.path = r"C:\SISNCOM\Config"
    Cfg.checkFileExistance()
    Db = Database(Cfg)
    Db.get_connect()
    CopyImg = Img(Cfg, Db)
    CopyImg.get_by_id(1)
    CopyImg.copy()



if __name__ == "__main__":
    main()
