from datetime import datetime                           # Importa la clase datetime para manejar fechas y horas
def Errores(cadena, error):                             # Función principal para manejar errores y validar cadenas en función de diferentes tipos de errores

    if error == 0:                                      # Si el error es 0, siempre es válido
        respuesta = True                                # La respuesta es verdadera
    elif error == 1:                                    # Si el error es 1, valida si la cadena está vacía
        if cadena == "":                                # Si está vacía, asigna la fecha actual
            cadena = datetime.now()                     # Obtiene la fecha y hora actual
            cadena = cadena.strftime("%d/%m/%y")        # Formatea la fecha a formato dd/mm/yy
            respuesta = True                            # Devuelve que es válido
        else:                                           # Si no está vacía
            cadena = ArreglaFecha(cadena)               # Corrige el formato de la fecha si es necesario
            respuesta = EsFecha(cadena)                 # Verifica si la fecha es válida
    elif error == 13:                                   # Si el error es 13, valida si la cadena es una fecha válida o está vacía
        if cadena == "":                                # Si la cadena está vacía
            respuesta = False                           # Si está vacía, es inválida
        else:                                           # Si no está vacía
            cadena = ArreglaFecha(cadena)               # Corrige el formato de la fecha
            respuesta = EsFecha(cadena)                 # Verifica si la fecha es válida
    elif cadena == "" and error == 10:                  # Si el error es 10 y la cadena está vacía
        respuesta = False                               # La respuesta es falsa
    elif error == 14:                                   # Si el error es 14, valida una fecha pero permite una cadena vacía
        if cadena == "":                                # Si la cadena está vacía
            respuesta = True                            # Si está vacía, es válida
        else:                                           # Si no está vacía
            cadena = ArreglaFecha(cadena)               # Corrige el formato de la fecha
            respuesta = EsFecha(cadena)                 # Verifica si la fecha es válida
    elif error == 3:                                    # Si el error es 3, valida si la cadena es un solo carácter 'A', 'I', o 'C'
        respuesta = UnCaracterAIC(cadena)               # Valida el carácter
        cadena = cadena.upper()                         # Convierte la cadena a mayúsculas
    elif error == 9:                                    # Si el error es 9, valida si la cadena es un nombre de archivo válido
        respuesta = EsNombreArchivo(cadena)             # Valida el nombre de archivo
    elif cadena == "":                                  # Si la cadena está vacía, es válida por defecto
        respuesta = True                                # La respuesta es verdadera
    elif error == 2:                                    # Si el error es 2, valida si la cadena es una fecha válida
        cadena = ArreglaFecha(cadena)                   # Corrige el formato de la fecha
        respuesta = EsFecha(cadena)                     # Verifica si la fecha es válida
    elif error == 4:                                    # Si el error es 4, verifica si la cadena es un número
        respuesta = EsDigito(cadena)                    # Verifica si la cadena es un dígito
    elif error == 5:                                    # Si el error es 5, valida si la cadena es un carácter 'T' o 'C'
        respuesta = UnCaracterTC(cadena)                # Valida el carácter
        cadena = cadena.upper()                         # Convierte la cadena a mayúsculas
    elif error == 6:                                    # Si el error es 6, valida si la cadena es 'P', 'C', o 'A'
        respuesta = UnCaracterPCA(cadena)               # Valida el carácter
        cadena = cadena.upper()                         # Convierte la cadena a mayúsculas
    elif error == 7:                                    # Si el error es 7, valida si la cadena es 'O' o 'D'
        respuesta = UnCaracterOD(cadena)                # Valida el carácter
        cadena = cadena.upper()                         # Convierte la cadena a mayúsculas
    elif error == 8:                                    # Si el error es 8, valida si la cadena es un dígito entre 0 y 100
        respuesta = DigitoEn100(cadena)                 # Verifica si es un número entre 0 y 100
    elif error == 11:                                   # Si el error es 11, verifica si la cadena es un número real (flotante)
        respuesta = EsReal(cadena)                      # Verifica si es un número real
    elif error == 12:  # Si el error es 12, valida si la cadena es 'T' o 'R'
        respuesta = UnCaracterCR(cadena)  # Valida el carácter
        cadena = cadena.upper()  # Convierte la cadena a mayúsculas
    elif error == 15:  # Si el error es 15, valida si la cadena es 'A', 'I', o 'C'
        respuesta = UnCaracterAIC(cadena)  # Valida el carácter
        cadena = cadena.upper()  # Convierte la cadena a mayúsculas

    return respuesta, cadena  # Devuelve si es válida y la cadena posiblemente modificada

# Valida si la cadena es 'T' o 'R' y tiene exactamente un carácter
def UnCaracterCR(cadena):
    if len(cadena) == 1:  # Si la cadena tiene solo un carácter
        cadena = cadena.upper()  # Convierte a mayúsculas
        if cadena == "T" or cadena == "R":  # Verifica si es 'T' o 'R'
            return True
        else:
            return False
    else:
        return False

# Verifica si la cadena es un número real
def EsReal(cadena):
    try:
        float(cadena)  # Intenta convertir a flotante
        return True
    except:
        return False

# Valida si la cadena es un nombre de archivo (sin caracteres no permitidos)
def EsNombreArchivo(cadena):
    símbolos_no_permitidos = ['/','\\',':','*','?','"','<','>','[',']','{','}','=','!','\'',',',';','.']  # Lista de símbolos no permitidos
    if any(símbolo in cadena for símbolo in símbolos_no_permitidos) or cadena == "":  # Si contiene símbolos no permitidos
        return False
    else:
        return True

# Verifica si la cadena es un dígito numérico
def EsDigito(cadena):
    if cadena.isdigit():  # Verifica si todos los caracteres son dígitos
        return True
    else:
        return False

# Verifica si la cadena es un dígito entre 0 y 100
def DigitoEn100(cadena):
    if cadena.isdigit():  # Verifica si es un dígito
        if int(cadena) >= 0 and int(cadena) <= 100:  # Verifica si está entre 0 y 100
            return True
        else:
            return False
    else:
        return False

# Verifica si la cadena es 'O' o 'D' y tiene un solo carácter
def UnCaracterOD(cadena):
    if len(cadena) == 1:  # Si la cadena tiene un solo carácter
        cadena = cadena.upper()  # Convierte a mayúsculas
        if cadena == "O" or cadena == "D":  # Verifica si es 'O' o 'D'
            return True
    else:
        return False

# Verifica si la cadena es 'P', 'C', o 'A' y tiene un solo carácter
def UnCaracterPCA(cadena):
    if len(cadena) == 1:  # Si la cadena tiene un solo carácter
        cadena = cadena.upper()  # Convierte a mayúsculas
        if cadena == "P" or cadena == "C" or cadena == "A":  # Verifica si es 'P', 'C', o 'A'
            return True
    else:
        return False

# Verifica si la cadena es 'T' o 'C' y tiene un solo carácter
def UnCaracterTC(cadena):
    if len(cadena) == 1:  # Si la cadena tiene un solo carácter
        cadena = cadena.upper()  # Convierte a mayúsculas
        if cadena == "T" or cadena == "C":  # Verifica si es 'T' o 'C'
            return True
    else:
        return False

# Verifica si la cadena es 'A', 'I', o 'C' y tiene un solo carácter
def UnCaracterAIC(cadena):
    if len(cadena) == 1:  # Si la cadena tiene un solo carácter
        cadena = cadena.upper()  # Convierte a mayúsculas
        if cadena == "A" or cadena == "I" or cadena == "C":  # Verifica si es 'A', 'I', o 'C'
            return True
    else:
        return False

# Corrige el formato de una fecha, asegurándose de que siga el formato dd/mm/yy
def ArreglaFecha(fecha):
    if len(fecha) < 4:  # Si la fecha tiene menos de 4 caracteres, la devuelve como está
        return fecha
    if len(fecha) < 8 and fecha[1] == "/":  # Si el día es de un solo dígito, añade un 0
        fecha = "0" + fecha
    if len(fecha) < 8 and fecha[4] == "/":  # Si el mes es de un solo dígito, añade un 0
        fecha = fecha[0:3] + "0" + fecha[3:]
    if len(fecha) > 9:  # Si el año tiene más de 2 dígitos, lo trunca
        fecha = fecha[0:6] + fecha[9:]
    return fecha

# Verifica si la cadena tiene el formato de fecha dd/mm/yy válido
def EsFecha(fecha):
    if (not all(c in "0123456789/" for c in fecha) or  # Verifica si todos los caracteres son válidos
            fecha == "" or  # Verifica si la fecha está vacía
            len(fecha) != 8 or  # Verifica si tiene exactamente 8 caracteres
            fecha[2] != "/" or  # Verifica que el tercer carácter sea '/'
            fecha[5] != "/" or  # Verifica que el sexto carácter sea '/'
            0 >= int(fecha[0:2]) or  # Verifica que el día sea mayor que 0
            32 <= int(fecha[0:2]) or  # Verifica que el día sea menor que 32
            0 >= int(fecha[3:5]) or  # Verifica que el mes sea mayor que 0
            13 <= int(fecha[3:5]) or  # Verifica que el mes sea menor que 13
            0 >= int(fecha[6:8]) or  # Verifica que el año sea mayor que 0
            99 <= int(fecha[6:8])):  # Verifica que el año sea menor que 99
        return False  # Si alguna de estas condiciones no se cumple, la fecha es inválida
    else:
        return True  # Si todas las condiciones se cumplen, la fecha es válida
 
