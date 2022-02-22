import sys
sys.path.append('./includes')
from Crawler import nightCrawler
from Utils import Utils
from datetime import date
import argparse




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Script en python bajar datos de TED')
    parser.add_argument('-p','--path', help='Ruta donde salvar los ficheros, dentro de crear un directorio con la fecha', required=True )
    parser.add_argument('-t','--type', help='Tipo de descarga BO o NUTS', required=True, choices=['BO', 'NUTS'])
    parser.add_argument('-f','--mfrom', help='Desde que mes del año actual queremos descargar, si ponemos 1 desde enero del año actual', required=False, type=int)
    arg = parser.parse_args()

    soUtils = Utils ()

    today = date.today()
    d1 = today.strftime("%Y_%m_%d")
    save_path = arg.path + '/' + str(d1)

    if soUtils.makeDir ( save_path ):

        crwl = nightCrawler (remoteExecutor = '192.168.148.139:4444/wd/hub')

        if arg.type == 'BO':        
            crwl.saveBO ( url = 'https://ted.europa.eu/TED/browse/browseByBO.do', path = save_path, mfrom = arg.mfrom ) 
        if arg.type == 'NUTS':
            crwl.saveNUTS ( url = 'https://ted.europa.eu/TED/browse/browseByPD.do', path = save_path, mfrom = arg.mfrom  ) 

        
    else:
        print ('Error creando directorio')


