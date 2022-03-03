import sys
sys.path.append('./includes')
from Documents import Document
from Utils import Utils
import argparse

'''
Este script se encarga de procesar las tablas bajadas con el script saveTables, y procesar la url de cada entrada para bajar la ficha detallada.

Para ello carga los ficheros json con las tablas resumidas, busca las urls de cada entrada y baja para cada ficha la pestaña de texto y la de datos:

Una url con la ficha típica puede ser:
https://ted.europa.eu/udl?uri=TED:NOTICE:91761-2022:TEXT:EN:HTML&src=0

Además, cada entrada de la tabla puede estar repetida o aparecer en diferentes descargas, por lo que este script se encarga de bajar sólo las entradas que no han sido bajadas.

Para lograr evitar las repeticiones, sin usar fuerza bruta y mirar de forma secuencial, lo que hace es crear varios ficheros de índices (uno por cada descarga) con los ids de
los documentos. Por lo tanto se implementan controles para actulizar el índice y las descargas.

El script recibe como párametro el basepath que es el punto de partida y el path con los datos de las descargas. Por ejemplo:

.
├── Data
│   └── completo
│       ├── BO
│       │   └── 2022_02_25
│       │       └── Call_for_expressions_of_interest_47
│       └── NUTS
│           ├── 2022_02_22
│           │   ├── DE_-_Deutschland_28258
│           │   └── MT_-_Malta_322
│           └── 2022_02_25
│               └── BE_-_Belgique__België_2870
├── Documents
│   └── Call_for_expressions_of_interest_47_1645790955_9071846
└── Index
    └── index_Call_for_expressions_of_interest_47_1645790955_907018


. Es el directorio raíz, el basepath

completo/BO/ y completo/NUTS las diversas descargas realizada, eso es lo que se pasa como path

Documents son los documentos descargado, son un json con el nombre de la tabla de origen y un datetime para evitar machacar los resultados
Index son los dicheros de índice generados, son un json con el nombre de la tabla de origen y un datetime para evitar machacar los resultados


'''


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Script en python para salvar los documentos del TED (los json con los ids se suponen ya generados)')
    parser.add_argument('-b','--bpath', help='Ruta base de la estructura de documentos', required=True )
    parser.add_argument('-p','--path', help='Ruta con los datos de las tablas de las que se bajaran los documentos', required=True )
    parser.add_argument('-y','--year', help='año del que bajar los documentos',type=int, choices=range(2015,2022),  required=True )

    arg = parser.parse_args()
    docu = Document ( arg.bpath, arg.path )

    print (docu.saveDocuments( arg.year))

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
