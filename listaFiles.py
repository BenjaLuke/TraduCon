import os                               
import time
import sqlite3

def listaFiles(carpeta,extension):                                                              
    archivos_db = [archivo for archivo in os.listdir(carpeta) if archivo.endswith(extension)]   
    if not archivos_db:                                                                         
        return archivos_db,0                                                                    
    return archivos_db,len(archivos_db)                                                         
            