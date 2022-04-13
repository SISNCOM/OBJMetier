import shutil
from time import sleep
from tqdm import tqdm


# It's a class that represents an image
class Img:

    def __init__(self, Cfg, Db):
        """
        The function __init__() is a constructor that initializes the class

        :param Cfg: A ConfigParser object that contains the configuration information for the program
        :param Db: The database object
        """
        self.cfg = Cfg
        self.db = Db
        self.path = ""
        self.verbose = 0

    def get_by_id(self, id):
        """
        It takes an id, and returns the path to the image

        :param id: the id of the image
        :return: The path to the image.
        """
        cr = self.db.get_cursor()
        query = "select CONCAT(a.texte,'\\\\', i.text) " \
                "from img i left join annotation " \
                "a on a.type=14 and a.idelt=i.id_img " \
                "and a.v1=i.nu_path where i.id_img={};".format(id)
        cr.execute(query)
        self.path, = cr.fetchone()
        if self.verbose:
            print("the path is : ", self.path,)
        return self.path,

    def copy(self):
        """
        It copies the file to a temporary location
        """
        output = self.cfg.get_data("PATH_VARIABLE", "temp_copy", "")
        for i in tqdm(range(5)):
            sleep(0.2)
        shutil.copy(self.path, output)
        print("copy done")


