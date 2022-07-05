from OBJMetier.configuration.Configuration import Configuration
from OBJSystem.Database.Database import Database
from OBJMetier.script.script import script
from OBJMetier.step.step import step
from OBJMetier.Image.Img import Img


def main():
    Cfg = Configuration()
    Cfg.path = r"C:\SISNCOM\Python\Config"
    if Cfg.checkFileExistance() < 0:
        print("Reeading error")
    #----------------------
    Db = Database(Cfg)
    Db.get_connect()
    #---------------------
    img = Img(Cfg, Db)
    img.info(80)
    nI = img.new()
    print(img.data)
    print(nI.data)
    # ---------------------
    step1  = step(Cfg, Db)
    step1.read(240,35)
    print(step1.info)
    id_img = step1.getInfo('id_img')
    print(id_img)
    src = step1.getInfo('src')
    print(src)
    step1.next(30,nI)
    # ---------------------
    Script = script(Cfg, Db)
    # Appeler les méthodes issues de la class script
    Script.open(r"test.txt")
    Script.replace("path", r"c:\\image")
    Script.save(r"resu.txt")



if __name__ == "__main__":
    main()
