import json
import os
import re

class Utils:


    def getValidFilename(self, s):
        s = str(s).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s)


    def saveToJson (self, data, path):

        
        nombre = self.getValidFilename (data['description'])

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