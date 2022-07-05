from OBJSystem.Database.Database import Database
from OBJMetier.configuration.Configuration import Configuration
from OBJMetier.connector.connector import connector
from OBJMetier.imgData.imgData import imgData
from OBJMetier.commun.commun import bcolors
from OBJMetier.step.step import step
from OBJMetier.Image.Img import Img

def main():
    req = 240
    pathConfig = r"C:\SISNCOM\Python\Config"
    # --------------------------------------------------
    #
    #   INITIALISATION globale
    #
    Cfg = Configuration()
    Cfg.path = pathConfig
    if Cfg.checkFileExistance() < 0:
        msg = "Reading config error : "+Cfg.path
        bcolors.prtColor(2,msg)
        return(-1)
    Db = Database(Cfg)
    ok = Db.get_connect()
    if (ok == 0):
        bcolors.prtColor(2, "Database access ERROR !")
        return (-1)
    bcolors.prtColor(1, "Database access OK !")
    # --------------------------------------------------
    #
    #   init requête
    #
    process = step(Cfg,Db)
    ok = process.read(req, 35)
    if(ok==0):
        bcolors.prtColor(2,"Acces error to request !")
        return (-1)
    idImg   = process.getInfo('id_img')
    msg = "Acces OK to request : "+str(req)+", for img id : "+str(idImg)
    bcolors.prtColor(1, msg)
    print(process.info)
    img = Img(Cfg, Db)
    img.info(idImg)
    ext = img.get_ext()
    img.getFullPath(0)
    pathImg = img.fullPathFile
    msg = "accès à l'image "+pathImg+" (extension :"+ext+")"
    print(msg);
    # --------------------------------------------------
    #
    #   validation du connecteur
    #
    Connector = connector(Cfg, Db)
    ok = Connector.getK(ext)
    ok = Connector.checkExec(2)
    if(ok == False):
        msg = "Connecteur NON trouvé : " + Connector.fullPath
        bcolors.prtColor(2, msg)
        return(-1)
    msg = "Connecteur trouvé : " + Connector.fullPath
    bcolors.prtColor(1, msg)
    ok = Connector.execK(pathImg, idImg, 1)
    if (ok == False):
        bcolors.prtColor(2, "Erreur exécution du connecteur !")
        return (-1)
    bcolors.prtColor(1, "Exécution du connecteur OK")
    #--------------------------------------------------
    #
    #   lecture de la réponse
    #
    data = imgData(Cfg, Db)
    ok = data.readMD(idImg)
    if(ok==False):
        bcolors.prtColor(2,"Erreur in reading data !")
        return(-1)
    ok = data.explodeData()
    if (ok == False):
        bcolors.prtColor(2, "Erreur in extraction of data !")
        return (-1)
    #-------------------------------------------
    nbLots = data.getNbLots()
    for x in range(nbLots):
        ptr =data.getLotNu(x)
        print(ptr)
        #------------------------------------------
        #
        #   lancement des process suivant
        #

    #--------------------------------------
    #
    #   indication fin de traitement
    #
    status=1
    process.endProcess(1)




if __name__ == "__main__":
    main()
