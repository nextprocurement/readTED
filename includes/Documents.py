from Utils import Utils
import json

class Document:
	__index 	= []
	__cur_index = []
	__new_docs  = []
	__path  	= ''
	
	__soUtils 	= Utils()


	def __init__ ( self, path ):
		self.__path = path
		self.__loadIndex__ ()


	def __loadIndex__ (self):

		index_files = self.__soUtils.getAllFilesInDir (self.__path + '/' + 'Index/' )

		for index in index_files:
			self.__index +=  (self.__soUtils.readJson (index) )

		print ('Se han cargado %s entradas desde los ficheros de indice' % (len (self.__index)))
				

	def __descargarDocuments (self,url):
		#aqui se va a la url y se bajan los datos del documento:
		return ('patata')


	def saveDocuments (self):
		doc_files = self.__soUtils.getAllFilesInDir (self.__path + '/' + 'Data/' )

		repetidas = 0

		for doc in doc_files:
			self.__cur_index = []

			doc_data = self.__soUtils.readJson (doc, is_str=True)
			print ('procesando %s (%s)' % (doc, len(doc_data)) )

			for entry in doc_data:
				if entry['id'] in self.__index:
					repetidas += 1
				else:
					self.__new_docs.append ({'id' : entry['id'], 'url': entry['url'], 'data' : self.__descargarDocuments (entry['url'])})
					self.__cur_index.append (entry['id'])

			if len(self.__cur_index) > 0:				
				name = self.__path + '/Index/' + self.__soUtils.getRandomNameFile ()

				'''
					MODIFICAR EL SALVAR JSON DEL UTILS PARA QUE SEA GENERICO EN VEZ DE USAR ESTO
				'''

				with open (name,'w') as outfile:
					json.dump(self.__cur_index, outfile)

				name = self.__path + '/Documents/' + self.__soUtils.getRandomNameFile ()
				with open (name,'w') as outfile:
					json.dump(self.__new_docs, outfile)

				self.__index += self.__cur_index
				
			print ('\t -> se han grabado %s nuevas entradas, habia %s de repetidas' % (len (self.__cur_index),repetidas  ))



		





