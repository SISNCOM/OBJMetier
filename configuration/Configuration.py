from configparser import ConfigParser


class Configuration:

    def __init__(self):
        self.config = ConfigParser()
        self.path = r'../config'
        self.filename = r'setup.INI'
        self.status = 1
        self.verbose = 1

    def checkFileExistance(self):
        self.configFilePath = self.path + "\\" + self.filename
        if self.verbose:
            print(self.configFilePath)
        try:
            with open(self.configFilePath):
                self.config.read(self.configFilePath)
                self.status = 1
                if self.verbose:
                    print("read ok.")
                return self.status
        except IOError as e:
            if self.verbose:
                print(e)
            self.status = -1
        return self.status

    def get_data(self, main, key, default):
        if self.status != 1:
            return default
        try:
            value = self.config.get(main, key)
            return value
        except:
            return default

