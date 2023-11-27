import sqlite3                                                                  
       
def creaAbreBd(carpeta):                                                            
    conn = sqlite3.connect(carpeta)     
    cur = conn.cursor()                 
    return conn,cur                     

def CreaUnaTabla(cur,tabla):                                                    
    cur.execute(tabla)      
    return cur              

def anadeFila(cur,datos1,datos2,baseDatos):                                     
    cur.execute(datos1,datos2)                  
    baseDatos.commit()                          

def CierraBd(baseDatos):                                                        
    baseDatos.close()       
    
def SeleccionaTodasFilas(carpeta,tabla):                                        
    apertura,cursor = creaAbreBd(carpeta)       
    seleccion = f"SELECT * FROM {tabla}"    
    cursor.execute(seleccion)               
    filas = cursor.fetchall()               
    CierraBd(apertura)                      
    return filas                            

def eliminaTabla(cursor,tabla):                                                 
    sentencia = f"DROP TABLE {tabla}"   
    cursor.execute(sentencia)           
    
def MuestraDato(carpeta,dato,tabla):                                            
    apertura,cursor = creaAbreBd(carpeta)                       
    seleccion = f"SELECT * FROM {tabla} WHERE Nombre = ?"   
    cursor.execute(seleccion, (dato,))                      
    fila = cursor.fetchall()                                
    CierraBd(apertura)                                      
    return fila                                             

def Modificar(cursor,sentencia,parametros):                                     
    cursor.execute(sentencia,parametros)    
    cursor.connection.commit()              

def DevuelveConsulta(cursor,sentencia,parametros):                              
    cursor.execute(sentencia,parametros)    
    linea = cursor.fetchone()               
    return linea                            
   
def listados(cursor,consulta):                                           
    cursor.execute(consulta)                            
    lista = [lista[0] for lista in cursor.fetchall()]   
    for i in range(len(lista)):                         
        if lista[i] == "sqlite_sequence":               
            lista.pop(i)                                
            break                                       
    return lista

def EliminaFilaenTabPro(cursor,tabla,fila):                                     
    fila = str(fila)
    sentencia = f"DELETE FROM {tabla} WHERE ID = ?" 
    cursor.execute(sentencia,(fila,))                   
    cursor.connection.commit()                          
     