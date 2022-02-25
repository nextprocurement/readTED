import sys
sys.path.append('./includes')
from Crawler import nightCrawler
from Utils import Utils
from datetime import date
import argparse

'''
Este script se encarga de buscar en las páginas del TED las entradas seleccionadas las tablas resumidas con las últimas entradas.

Por ejemplo, https://ted.europa.eu/TED/browse/browseByBO.do, contiene una tabla dinámica que muestra por fecha descendente las entradas.
El scritp se baja los datos de la tabla mediante selenium y los guarda en un json. 

Los datos de las tablas son muy breves, fecha, tipo y descripción, además de un enlace a la ficha del documento. Esas fichas serán procesadas por otro programa.

Para evitar tener que usar una interfaz gráfica se usa un selenium remoto que se levanta en un docker.

El script recibe la ruta donde se quieren grabar los datos, el tipo de datos que se quiere bajar (BO o NUTS) y un párametro opcional que indica el mes desde el que 
queremos bajar los datos. Por ejemplo, si estamos en Marzo del 2022 y ponemos un 1 en el parámetro, se bajarán todos los datos del Mes 1,2 y 3. De esta forma 
sólo debemos hacer una descarga completa una vez y el resto son incrementales. El problema es que habrá entradas repetidas con bastante seguridad, por lo que el siguiente
programa, que se baja los datos de cada ficha, debe gestionar ese problema. Este script eso no lo tiene en cuenta, como son pocos datos se guardan algunos repetidos.
'''


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


