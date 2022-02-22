import json
import os

class Utils:

    def saveToJson (self, data, path):

        #algunas descripciones llevan una barra y al salvar con la barra, kabum:
        nombre = data['description'].split('/')[0].replace(' ','_')

        with open(path + '/' + nombre, "w") as outfile:
            json.dump(json.dumps(data['items']), outfile)

    def makeDir ( self, path ):

        try:
            os.mkdir(path )
        except OSError as O:
            print ("Creation of the directory %s failed, %s" %(path, str(O)))
            return False
        else:
            print ("Successfully created the directory %s " % path)
            return True