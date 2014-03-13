# -*- coding: utf-8 -*-

from lxml import etree
from suds.client import Client

a=1

while a!=0:
	
	linea=raw_input("Pon un numero de linea: ")
	cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)
	respuesta=cliente.service.GetStatusLinea(linea)
	obtener=etree.fromstring(respuesta.encode("utf-8"))
	re=etree.tostring(obtener,pretty_print=True)

	print re


