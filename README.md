# readTED
Repository for downloading TED information (Tenders Electronic Daily).

## Full download

To perform the complete download of the tenders, we must use the script contained in the saveByXML directory.

Its use is as follows:

	python saveXML.py -y 2015 -m 12 -p ruta para la descarga

If you do not enter the month, all tenders of the year will be downloaded.

The download is carried out in a compressed file with the XML.


## Download by CPV or NUTS code

If you want to download by CPV or NTS code (https://ted.europa.eu/TED/browse/browseByBS.do), use the script in the saveByCategory folder:

	python saveTables.py -p /export/data_ml4ds/IntelComp/Datasets/ted/completo/BO -t BO
	python saveDocuments.py -b /export/data_ml4ds/IntelComp/Datasets/ted/tedData/ -p /export/data_ml4ds/IntelComp/Datasets/ted/tedData/Data/ -y 2021



