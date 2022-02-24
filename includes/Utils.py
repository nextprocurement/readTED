import json
import os
from pathlib import Path
import re
import uuid
import glob


class Utils:


    def getValidFilename(self, s):
        s = str(s).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s)


    def saveToJson (self, data, path):

        
        nombre = self.getValidFilename (data['description'])

        with open(path + '/' + nombre, "w") as outfile:
            json.dump(json.dumps(data['items']), outfile)

    def readJson (self, file, is_str=False):
        try:
            with open( file ) as jsonfile:
                data = json.load(jsonfile)            
            if is_str:
                return json.loads(data)
            else:
                return data
        except Exception as E:
            print ('fallo leyendo %s, %s' % (file, E))


    def makeDir ( self, path ):

        try:
            os.mkdir(path )
        except OSError as O:
            print ("Creation of the directory %s failed, %s" %(path, str(O)))
            return False
        else:
            print ("Successfully created the directory %s " % path)
            return True

    def getAllFilesInDir (self, path):
        #result = list(Path(".").rglob("*.[tT][xX][tT]"))
        files = list(Path(path).rglob("*"))
        return [f for f in files if os.path.isfile(f)]



    def getRandomNameFile (self, prefix = ''):
        #return ( tempfile.NamedTemporaryFile(prefix=prefix))
        return prefix + uuid.uuid4().hex


        

