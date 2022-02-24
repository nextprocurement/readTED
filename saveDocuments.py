import sys
sys.path.append('./includes')
from Documents import Document
from Utils import Utils
import argparse




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Script en python para salvar los documentos del TED (los json con los ids se suponen ya generados)')
    parser.add_argument('-p','--path', help='Ruta donde salvar los ficheros, dentro de crear un directorio con la fecha', required=True )

    arg = parser.parse_args()
    docu = Document ( arg.path )

    print (docu.saveDocuments())

    #print (soUtils.getAllFilesInDir (arg.path + '/' + 'index/' ))

    

    #tf = soUtils.getRandomNameFile (prefix = 'index_')
    #print (tf.name)
    
    '''
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

    '''
