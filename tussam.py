# -*- coding: utf-8 -*-

from lxml import etree
from suds.client import Client
try:
	linea=raw_input("Pon un numero de linea: ")
	cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)
	respuesta=cliente.service.GetStatusLinea(linea)
	obtener=etree.fromstring(respuesta.encode("utf-8"))
	obtener2=obtener[0][0]
	re=etree.tostring(obtener2,pretty_print=True)
	ns="{http://tempuri.org/}"
	nb="GetStatusLineaResult/"
	activos=obtener2.find(ns+nb+ns+"activos")
	frecuencia=obtener2.find(ns+nb+ns+"frec_bien")
	graves=obtener2.find(ns+nb+ns+"graves")
	
	print "------------------------------------------------------"
	print "Los datos de TUSSAM son los siguientes:"
	print "------------------------------------------------------"
	print "El número de coches activos en la linea",linea,"son:",activos.text,
	print "\n""El número de coches que van bien de frecuencia es:",frecuencia.text,
	print "\n""El número de incidencias graves son:",graves.text,
	print "\n""------------------------------------------------------"

except:
	print "----------------------------"
	print "La linea número",linea,"no existe."
	print "----------------------------"

