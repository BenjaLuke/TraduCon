from datetime import datetime
import game

def Errores(cadena, error):
    if error == 0:
        respuesta = True
    elif error == 1:
        if cadena == "":
            cadena = datetime.now()
            cadena = cadena.strftime("%d/%m/%y")
            respuesta = True
        else:
            cadena = ArreglaFecha(cadena)
            respuesta = EsFecha(cadena)
    elif error == 13:
        if cadena == "":
            respuesta = False
        else:
            cadena = ArreglaFecha(cadena)
            respuesta = EsFecha(cadena)
    elif cadena == "" and error == 10:
        respuesta = False
    elif error == 14:
        if cadena == "":
            respuesta = True
        else:
            cadena = ArreglaFecha(cadena)
            respuesta = EsFecha(cadena)        
    elif error == 3:
        respuesta = UnCaracterAIC(cadena) 
        cadena = cadena.upper()       
    elif error == 9:
        respuesta = EsNombreArchivo(cadena)
    
    elif cadena == "":
        respuesta = True
    
    elif error == 2:
        cadena = ArreglaFecha(cadena)
        respuesta = EsFecha(cadena)
    elif error == 4:
        respuesta = EsDigito(cadena)
    elif error == 5:
        respuesta = UnCaracterTC(cadena)
        cadena = cadena.upper()       
    elif error == 6:
        respuesta = UnCaracterPCA(cadena)
        cadena = cadena.upper()       
    elif error == 7:
        respuesta = UnCaracterOD(cadena)
        cadena = cadena.upper()       
    elif error == 8:
        respuesta = DigitoEn100(cadena)
    elif error == 11:
        respuesta = EsReal(cadena)
    elif error == 12:
        respuesta = UnCaracterCR(cadena)  
        cadena = cadena.upper()       
    elif error == 15:
        respuesta = UnCaracterAIC(cadena)
        cadena = cadena.upper()
                      
    return respuesta, cadena

def UnCaracterCR(cadena):
    if len(cadena) == 1:
        cadena = cadena.upper()
        if cadena == "T" or cadena == "R":
            return True
        else:
            return False
    else:
        return False
    
def EsReal(cadena):
    try:
        float(cadena)
        return True
    except:
        return False
def EsNombreArchivo(cadena):
        símbolos_no_permitidos = ['/','\\',':','*','?','"','<','>','[',']','{','}','=','!','\'',',',';','.']        
        if any(símbolo in cadena for símbolo in símbolos_no_permitidos) or cadena == "":               
            return False
        else:
            return True
                                              
def EsDigito(cadena):
    if cadena.isdigit():
        return True
    else:
        return False

def DigitoEn100(cadena):
    if cadena.isdigit():
        if int(cadena) >= 0 and int(cadena) <= 100:
            return True
        else:
            return False
    else:
        return False
    
def UnCaracterOD(cadena):
    if len(cadena) == 1:
        cadena = cadena.upper()
        if cadena == "O" or cadena == "D":
            return True
    else:
        return False
    
def UnCaracterPCA(cadena):
    if len(cadena) == 1:
        cadena = cadena.upper()
        if cadena == "P" or cadena == "C" or cadena == "A":
            return True
    else:
        return False

def UnCaracterTC(cadena):
    if len(cadena) == 1:
        cadena = cadena.upper()
        if cadena == "T" or cadena == "C":
            return True
    else:
        return False
        
def UnCaracterAIC(cadena):
    if len(cadena) == 1:
        cadena = cadena.upper()
        if cadena == "A" or cadena == "I" or cadena == "C":
            return True
    else:
        return False
    
def ArreglaFecha(fecha):                                                                        
    if len(fecha) < 4:                      
        return fecha
    if len(fecha) < 8 and fecha[1] == "/":  
        fecha = "0" + fecha                         
    if len(fecha) < 8 and fecha[4] == "/":  
        fecha = fecha[0:3] + "0" + fecha[3:]        
    if len(fecha) > 9:                      
        fecha = fecha[0:6] + fecha[9:]              
    return fecha                            

def EsFecha(fecha):                                                                             
    if (not all(c in "0123456789/" for c in fecha) or
            fecha == "" or 
            len(fecha) != 8 or
            fecha[2] != "/" or 
            fecha[5] != "/" or
            0 >= int(fecha[0:2]) or
            32 <= int(fecha[0:2]) or
            0 >= int(fecha[3:5]) or
            13 <= int(fecha[3:5]) or
            0 >= int(fecha[6:8]) or
            99 <= int(fecha[6:8])):
        return False    
    else:               
        return True     
 
