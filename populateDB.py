# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:14:59 2016
@author: javier
"""


#read this https://github.com/pbugnion/gmaps

import pymongo
import json
import glob
import os
from pymongo import MongoClient
from servelParser import *
import xlrd
import sys
import csv
import json

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

    
#-------------------------------------------------------------------------------
#DB creation
#
#DBdirectory ='/home/javier/.../Code/jsonData/' #The database Directory

#Client connection with MongoDB
try:
    client = MongoClient('127.0.0.1')
    client.RutChile.authenticate('superuser','picodeperro',source='admin')
    #uri = "mongodb://superuser:picodeperro@35.188.87.1:27017/admin"
    #client = pymongo.MongoClient(uri)
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 


pdfServelPath = '../Padron/' #the path where you have all the pdf
files = [name for name in glob.glob(os.path.join(pdfServelPath, '*.pdf'))] #search each pdf file


#pointers
db = client.RutChile # Nombre de la base de datos: Militantes
Servel = db.Padron

for i in range(len(files)):
    archivo = files[i]
    #Parse files
    archivoServel = servelParser(archivo)
    
    #Servel DB
    for i in range(len(archivoServel)):
        Servel.insert_one(archivoServel[i])
    print "Populating servel Collection"
    
print "Todos los datos han sido migrados a la base de datos"
