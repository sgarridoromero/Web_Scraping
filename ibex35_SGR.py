# -*- coding: utf-8 -*-
# Se importan las librerias necesarias
import requests
from bs4 import BeautifulSoup
import csv
# Se guarda la página web que se va a utilizar en una variable
url_page = 'http://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice'
# Se obtiene la información de la página
page = requests.get(url_page).text 
# Se parsea la información obtenida
soup = BeautifulSoup(page, "lxml")
# Se obtiene la tabla en la que se encuentran los datos
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
#Lista que contiene los nombres de las columnas de datos
encabezado=["Nombre", "Último","% Dif.","Máx.","Min.","Volumen","Efectivo (miles €)","Fecha","Hora"]
#Lista vacía que contendrá los datos
datos=[]
#Se le añade a la lista vacía el encabezado
datos.append(encabezado)
#Bucle que recorre las filas de la tabla
for n_fila in tabla.find_all("tr"):
   #Lista vacía que permite guardar cada una de las filas de la tabla
   accion=[]
   # Bucle que recorre cada una de las columnas de la tabla por cada fila
   for celda in n_fila.find_all('td'):
       #Se le van añadiendo los datos de cada celda a la lista que guarda la información de las filas
       accion.append(celda.text) 
   #Una vez que se han obtenido todos los datos de una fila, se añaden a la lista que contiene todos los datos
   datos.append(accion)
   
# Cuando se han obtenido todos los datos de la tabla se guardan en un fichero CSV
with open('precios_sesion_ibex35_SGR.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    for emp in datos:
        writer.writerow(emp)
   
   
       
   
       
    
       
   


