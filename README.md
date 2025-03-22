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

## Acknowledgements

This work has received funding from the NextProcurement European Action (grant agreement INEA/CEF/ICT/A2020/2373713-Action 2020-ES-IA-0255).

<p align="center">
  <img src="static/Images/eu-logo.svg" alt="EU Logo" height=100 width="200" style="margin-right: -27px;">
  <img src="static/Images/nextprocurement-logo.png" alt="Next Procurement Logo" height=100 width="200">
</p>


