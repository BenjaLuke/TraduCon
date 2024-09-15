import sqlite3                                                                  # Importamos sqlite para las bases de datos                                              
       
def creaAbreBd(carpeta):                                                        # Crea y abre la base de datos
    conn = sqlite3.connect(carpeta)                                             # Conecta con la base de datos
    cur = conn.cursor()                                                         # Crea un cursor
    return conn,cur                                                             # Devuelve la conexión y el cursor

def CreaUnaTabla(cur,tabla):                                                    # Crea una tabla
    cur.execute(tabla)                                                          # Ejecuta la sentencia
    return cur                                                                  # Devuelve el cursor

def anadeFila(cur,datos1,datos2,baseDatos):                                     # Añade una fila
    cur.execute(datos1,datos2)                                                  # Ejecuta la sentencia
    baseDatos.commit()                                                          # Guarda los cambios

def CierraBd(baseDatos):                                                        # Cierra la base de datos
    baseDatos.close()                                                           # Cierra la base de datos
    
def SeleccionaTodasFilas(carpeta,tabla):                                        # Selecciona las tablas                                        
    apertura,cursor = creaAbreBd(carpeta)                                       # Abre la base de datos
    seleccion = f"SELECT * FROM {tabla}"                                        # Selecciona todas las filas de la tabla
    cursor.execute(seleccion)                                                   # Ejecuta la sentencia
    filas = cursor.fetchall()                                                   # Devuelve todas las filas
    CierraBd(apertura)                                                          # Cierra la base de datos
    return filas                                                                # Devuelve las filas

def eliminaTabla(cursor,tabla):                                                 # Elimina una tabla
    sentencia = f"DROP TABLE {tabla}"                                           # Sentencia para eliminar la tabla
    cursor.execute(sentencia)                                                   # Ejecuta la sentencia
    
def MuestraDato(carpeta,dato,tabla):                                            # Muestra un dato
    apertura,cursor = creaAbreBd(carpeta)                                       # Abre la base de datos
    seleccion = f"SELECT * FROM {tabla} WHERE Nombre = ?"                       # Selecciona el dato
    cursor.execute(seleccion, (dato,))                                          # Ejecuta la sentencia
    fila = cursor.fetchall()                                                    # Devuelve la fila
    CierraBd(apertura)                                                          # Cierra la base de datos
    return fila                                                                 # Devuelve la fila

def Modificar(cursor,sentencia,parametros):                                     # Modifica un dato
    cursor.execute(sentencia,parametros)                                        # Ejecuta la sentencia
    cursor.connection.commit()                                                  # Guarda los cambios

def DevuelveConsulta(cursor,sentencia,parametros):                              # Devuelve una consulta
    cursor.execute(sentencia,parametros)                                        # Ejecuta la sentencia
    linea = cursor.fetchone()                                                   # Devuelve la línea
    return linea                                                                # Devuelve la línea
   
def listados(cursor,consulta):                                                  # Listados
    cursor.execute(consulta)                                                    # Ejecuta la sentencia
    lista = [lista[0] for lista in cursor.fetchall()]                           # Devuelve la lista    
    for i in range(len(lista)):                                                 # Recorre la lista
        if lista[i] == "sqlite_sequence":                                       # Si el dato es igual a sqlite_sequence
            lista.pop(i)                                                        # Lo elimina
            break                                                               # Sale del bucle
    return lista                                                                # Devuelve la lista         

def EliminaFilaenTabPro(cursor,tabla,fila):                                     # Elimina una fila
    fila = str(fila)                                                            # Convierte la fila en cadena
    sentencia = f"DELETE FROM {tabla} WHERE ID = ?"                             # Sentencia para eliminar la fila
    cursor.execute(sentencia,(fila,))                                           # Ejecuta la sentencia
    cursor.connection.commit()                                                  # Guarda los cambios
     