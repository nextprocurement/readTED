from Utils import Utils
import json
import requests
from bs4 import BeautifulSoup



class Document:
	__index 	= []
	__cur_index = []
	__new_docs  = []
	__path  	= ''
	__bpath  	= ''
	
	__soUtils 	= Utils()


	def __init__ ( self, bpath, path ):
		self.__path = path
		self.__bpath = bpath
		self.__loadIndex__ ()


	def __loadIndex__ (self):

		index_files = self.__soUtils.getAllFilesInDir (self.__bpath + '/' + 'Index/' )

		for index in index_files:
			self.__index +=  (self.__soUtils.readJson (index, is_str=True))

		print ('Se han cargado %s entradas desde los ficheros de indice' % (len (self.__index)))
				

	def __getTextSections (self, sections):
	    dict_section = {}

	    for sec in sections:
	        
	        tit_sec = sec.find ('p',{'class':'tigrseq'}).get_text()
	        dict_section[tit_sec] = {}

	        sub_sec = sec.find_all ('div',{'class':'mlioccur'})

	        for ss in sub_sec:       
	            tit_sub_sec  = ss.find ('span',{'class':'timark'}).get_text().replace(':','')
	            try:
	                text_sub_sec = ss.find ('div',{'class':'txtmark'}).get_text()
	                dict_section[tit_sec][tit_sub_sec] = text_sub_sec
	            except:
	                #algunas secciones solo tienen el titulo sin texto asociado, se ignoran.
	                pass
	    return dict_section


	def __getDataSections (self, table):

		tds = [row.findAll('td') for row in table.findAll('tr')]		
		data = data = {td[0].get_text():td[1].get_text() for td in tds}
		
		return data

	def __descargarDocuments (self,url):


		headers = {
		    'Access-Control-Allow-Origin': '*',
		    'Access-Control-Allow-Methods': 'GET',
		    'Access-Control-Allow-Headers': 'Content-Type',
		    'Access-Control-Max-Age': '3600',
		    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
		    }



		
		url = "https://ted.europa.eu/udl?uri=TED:NOTICE:99655-2022:TEXT:EN:HTML&src=0&tabId=1"
		req = requests.get(url, headers)
		soup_text = BeautifulSoup(req.content, 'html.parser')

		url = soup_text.find ("a", {'title':'Display notice data'}).get('href')
		url = 'https://ted.europa.eu/' + url
		req = requests.get(url, headers)
		soup_data = BeautifulSoup(req.content, 'html.parser')

		sections = soup_text.find_all ('div',{'class':'grseq'})	
		dict_text_section = self.__getTextSections (sections)

		sections = soup_data.find('table')
		#print (url)
		dict_data_section = self.__getDataSections (sections)

		return dict_text_section, dict_data_section		



	def saveDocuments (self):
		#doc_files = self.__soUtils.getAllFilesInDir (self.__path + '/' + 'Data/' )
		doc_files = self.__soUtils.getAllFilesInDir (self.__path)

		repetidas = 0

		for doc in doc_files:
			self.__cur_index = []

			doc_data = self.__soUtils.readJson (doc, is_str=True)
			print ('procesando %s (%s)' % (doc, len(doc_data)) )

			for entry in doc_data:
				#indexpatat = self.__index
				#import ipdb ; ipdb.set_trace()

				if entry['id'] in self.__index:
					repetidas += 1
				else:
					data1, data2 = self.__descargarDocuments (entry['url'])
					self.__new_docs.append ({'id' : entry['id'], 'url': entry['url'], 'text' : data1, 'data':data2})
					self.__cur_index.append (entry['id'])

			if len(self.__cur_index) > 0:				

				#name = self.__path + '/Index/' + self.__soUtils.getRandomNameFile ()
				name = self.__bpath + '/Index/' + self.__soUtils.getNameFileWithTimeStamp (doc, prefix = 'index')
				self.__soUtils.saveToJson (self.__cur_index, name)

				'''
				with open (name,'w') as outfile:
					json.dump(self.__cur_index, outfile)

				'''
				#name = self.__path + '/Documents/' + self.__soUtils.getRandomNameFile ()
				name = self.__bpath + '/Documents/' +  self.__soUtils.getNameFileWithTimeStamp (doc)

				self.__soUtils.saveToJson (self.__new_docs, name)

				'''

				with open (name,'w') as outfile:
					json.dump(self.__new_docs, outfile)
				'''
				self.__index += self.__cur_index

				print ('\t \t el índice tiene ahora %s entradas' % (len (self.__index)))
				
			print ('\t -> se han grabado %s nuevas entradas, habia %s de repetidas' % (len (self.__cur_index),repetidas  ))



		





