import shutil
from time import sleep
from tqdm import tqdm


class Img:

    def __init__(self, Cfg, Db):
        self.cfg = Cfg
        self.db = Db
        self.path = ""

    def get_by_id(self, id_):
        cr = self.db.get_cursor()
        _query = "SELECT I.path FROM img I INNER JOIN annotation A ON I.id = A.id WHERE A.id = %s;"
        cr.execute(_query, (id_,))
        self.path, = cr.fetchone()
        return self.path,

    def copy(self):
        output = self.cfg.get_data("PATH_VARIABLE", "temp_copy", "")
        for i in tqdm(range(10)):
            sleep(0.2)
        shutil.copy(self.path, output)


