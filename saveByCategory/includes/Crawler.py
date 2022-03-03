'''
En 192.168.148.139, levantamos el docker:
docker pull juusechec/firefox-headless-selenium-python
docker run -p 4444:4444 -p 5900 -d . --name firefox-headless-selenium-python
'''


from selenium.webdriver.firefox.options import Options
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from Utils import Utils
from datetime import date
from datetime import datetime


class nightCrawler ():

    __options              = Options ()
    __driver               = None
    __remoteExecutor       = None


    def __init__ ( self, remoteExecutor ):
        self.__options.headless = True
        del(self.__options.capabilities['moz:debuggerAddress'])

        self.__driver = webdriver.Remote(
            options = self.__options,
            command_executor= remoteExecutor
        )

        self.__driver.implicitly_wait(20) 


    def __getSearchResults (self, url, mfrom ):


        driver = self.__driver

        salir = False
        listItem = []
        contador = 0

        while not salir:

            driver.get ( url )   

            #debe existir una manera mas correcta de esperar a que cargue la tabla, pero el implicitly_wait no funciona         
            time.sleep(2)

            print ('/%s' % contador)

            tr_table = driver.find_elements(By.XPATH, "//table[@id='notice']//tbody//tr")

            for tr in tr_table:    

                td = tr.find_elements (By.TAG_NAME,"td")

                #si queremos hacer bajadas incrementales usamos el parametro mfrom, lo que hace es indicar el mes desde el cual se bajan los datos, siempre según el año actual
                if mfrom:                    
                    publication = datetime.strptime(td[4].text,'%d/%m/%Y')
                    currentdate = date.today()

                    if not (currentdate.year == publication.year and publication.month >= mfrom):
                        salir = True
                        break

                data = {}                
                data['id']              = td[1].text
                data['url']             = td[1].find_element (By.TAG_NAME,"a").get_attribute('href')
                data['description']     = td[2].text
                data['country']         = td[3].text
                data['publication']     = td[4].text
                data['deadline']        = td[5].text

                pos1 = td[2].text.find('Type of buyer')
                pos2 = td[2].text.find('Notice type')
                pos3 = td[2].text.find('Type of procedure')
                pos4 = td[2].text.find('Type of contract')

                data['TypeOfBuyer']         =   td[2].text[pos1:pos2].replace ('Type of buyer:','')
                data['Notice type']         =   td[2].text[pos2:pos3].replace ('Notice type:','')
                data['TypeOfProcedure']     =   td[2].text[pos3:pos4].replace ('Type of procedure:','')
                data['TypeOfContract']      =   td[2].text[pos4:].replace ('Type of contract:','')


                listItem.append (data)

            contador += 1

            try:                
                url_new = driver.find_element(By.XPATH, "//div[contains(@class, 'pagenext')]").find_element (By.TAG_NAME,"a").get_attribute('href')
                if url_new == url:
                    Salir = True
                else:
                    url = url_new
            except Exception as E:
                salir = True

            




        return listItem





    def saveBO (self, url, path, mfrom):

        self.__driver.get ( url )
        
        print ('connect to %s' % self.__driver.title)

        soUtils = Utils ()



        driver = self.__driver

        listItems = driver.find_elements(By.XPATH, "//div[@id='filterTree']/ul/li")

        listLinks = [ {'url':item.find_element (By.TAG_NAME,"a").get_attribute ("href"),'description': item.find_element (By.TAG_NAME,"a").text}for item in listItems ]



        listItems = []
        for link in listLinks:
            print ('Crawlink %s' % link['description'])
            data = {}
            data ['description'] = link['description']
            data['items'] = self.__getSearchResults (link['url'], mfrom)

            nombre = path + '/' + soUtils.getValidFilename (data['description'])

            soUtils.saveToJson (data['items'],nombre)


    def saveNUTS (self, url, path, mfrom):
        self.__driver.get ( url )
        
        print ('connect to %s' % self.__driver.title)

        soUtils = Utils ()



        driver = self.__driver

        listItems = driver.find_elements(By.XPATH, "//div[@id='filterTree']/ul/li")        

        #el ultimo elemento es especial, no hay dos tag a por lo que se procesa de otra manra:
        data = listItems.pop(len(listItems)-1)
        listLinks = [ {'url': item.find_elements (By.TAG_NAME,"a")[1].get_attribute ("href"),'description': item.find_elements (By.TAG_NAME,"a")[1].text} for item in listItems ]

        listItems.append({'url':data.find_element (By.TAG_NAME,"a").get_attribute ("href"),'description': data.find_element (By.TAG_NAME,"a").text})

        for link in listLinks:
            print ('Crawlink %s' % link['description'])
            data = {}
            data ['description'] = link['description']
            data['items'] = self.__getSearchResults (link['url'], mfrom)

            nombre = path + '/' + soUtils.getValidFilename (data['description'])

            soUtils.saveToJson (data['items'],nombre)                    




    def __del__ (self):
        print ('bye')
        self.__driver.quit()
