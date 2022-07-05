class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # type=1:OK, 2:alert
    def prtColor( type, texte):
        dspl = texte
        if(type==1):
            dspl = bcolors.OKGREEN+texte+bcolors.ENDC
        if (type == 2):
            dspl = bcolors.FAIL + texte + bcolors.ENDC
        print(dspl)