__all__ = ['Configuration']

from OBJMetier.configuration.Configuration import Configuration


def main():
    Cfg = Configuration()
    Cfg.path = r"C:\SISNCOM\Config"
    status = Cfg.checkFileExistance()
    if status == 0:
        print('no value')
        return -1
    print('value found')


if __name__ == "__main__":
    main()
