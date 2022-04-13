from configparser import ConfigParser


# > The Configuration class is a container for the configuration of the application
class Configuration:

    def __init__(self):
        """
        The function __init__() is a constructor for the class ConfigParser
        """
        self.config = ConfigParser()
        self.path = r'../config'
        self.filename = r'setup.INI'
        self.status = 1
        self.verbose = 1

    def checkFileExistance(self):
        """
        It checks if a file exists and returns a status code
        :return: The status of the file.
        """
        self.configFilePath = self.path + "\\" + self.filename
        if self.verbose:
            print(self.configFilePath)
        try:
            with open(self.configFilePath):
                self.config.read(self.configFilePath)
                self.status = 1
                if self.verbose:
                    print("available file")
                return self.status
        except IOError as e:
            if self.verbose:
                print(e)
            self.status = -1
        return self.status

    def get_data(self, main, key, default):
        """
        If the status is not 1, return the default value. If it is 1, try to get the value from the config file. If it
        fails, return the default value
        
        :param main: The main section of the config file
        :param key: The key of the value you want to get
        :param default: The default value to return if the key is not found
        :return: The value of the key in the main section of the config file.
        """
        if self.status != 1:
            return default
        try:
            value = self.config.get(main, key)
            return value
        except:
            return default

