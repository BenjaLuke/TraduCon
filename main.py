import os                                                       
import sys                              
from datetime import datetime                         
import time

import listaFiles                       
import sql                              
import game                             

screen = game.Game()
   
def comprobarExistenciaCarpeta():                               
            
    if not os.path.exists("Database") or not os.path.isdir("Database"):     

        screen.SoundWrongAnswer     ()
        mensajeConPausa             ("Error. No existe la carpeta contenedora adecuada")
        mensajeConPausa             ("Se creará la carpeta contenedora adecuada")
        os.mkdir                    ("Database")
        mensajeConPausa             ("Carpeta creada con éxito")
                 
        return
        
def menuInicial():             
    
    in_function = True
    while in_function:
        
        screen.paper(50,100,10)
        screen.text(150,300,["Menú Principal","1 - Abrir proyecto","2 - Nuevo proyecto",
                    "3 - Clientes","4 - Tablas de corrección"])
        screen.updateScreen()
        
        destino = screen.pushAndCome()
        if destino == "1":      EscogeTipoProyecto()
        elif destino == "2":    menuCreaProyecto()
        elif destino == "3":    menuClientes()
        elif destino == "4":    menuTablasCorreccion()
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    exit()
    
def EscogeTipoProyecto():        
    
    in_function = True
    while in_function:

        screen.paper(100,200,9)
        screen.text(200,400,["Abrir proyecto","1 - Activo","2 - Inactivo","3 - Cerrado"])
        screen.updateScreen()
            
        tipo_proyecto = ""
        destino = screen.pushAndCome()
        if destino == "1":      tipo_proyecto = ".dba"
        elif destino == "2":    tipo_proyecto = ".dbi"
        elif destino == "3":    tipo_proyecto = ".dbc"
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        if tipo_proyecto != "": abrirProyecto(tipo_proyecto)

    return

def abrirProyecto(tipo_proyecto):        

        in_function = True                                                                           
        while in_function:                                                                           
                                                                                    
            DiccionarioFiles,cantidad = listaFiles.listaFiles("Database",tipo_proyecto)   
            datos = []                                                                          
            for dato in DiccionarioFiles:                                                       
                datos.append(dato.split(".")[0])                                                
            opciones_de_menu = [f"Abrir proyecto {tipo_proyecto}"]

            numeracion = 1
            for i in datos:

                i = f"{numeracion} - {i}"
                opciones_de_menu.append(i)
                numeracion += 1

            if cantidad == 0:

                screen.SoundWrongAnswer()
                mensajeConPausa(f"No existen proyectos {tipo_proyecto}")
                in_function = False
                break
            
            screen.paper(300,600,cantidad+6)
            screen.text(400,800,opciones_de_menu)
            screen.updateScreen()

            opciones = [str(i) for i in range(0,cantidad+1)]
            need_answer = True
            while need_answer:
                
                opcion = screen.pushAndCome()
                if opcion in opciones:
                    need_answer = False

            opcion = int(opcion)      
            if opcion == 0:  
                
                in_function = False                                                  
            
            else:                                                                                   
                
                Proyecto = DiccionarioFiles[opcion-1]                                         
                proyectoSinExt = Proyecto.split(".")[0] 
                in_function = False # Al volver desde CRUD, hay que volver a escoter tipo de proyecto                                  
                menuProyectoCRUD(Proyecto,proyectoSinExt)                                           
        
        return
    
def menuProyectoCRUD(proyecto,proyectoSinExt): 
    
    in_function = True
    while in_function:  
        
        exit_project = False
                       
        screen.paper(150,300,11)
        screen.text(250,500,[f"'{proyectoSinExt}'",
                    "1 - Corrige un dato","2 - Añade un dato","3 - Elimina dato/proyecto",
                    "4 - Gráficas","5 - Consultar tablas"])
        screen.updateScreen()
        
        destino = screen.pushAndCome()
        if destino == "1":      menuProyectoCorrige(proyecto,proyectoSinExt)
        elif destino == "2":    menuProyectoAnade(proyecto,proyectoSinExt)
        elif destino == "3":    exit_project = menuProyectoElimina(proyecto,proyectoSinExt)
        elif destino == "4":    menuProyectoGraficas(proyecto,proyectoSinExt)
        elif destino == "5":    menuProyectoTablas(proyecto,proyectoSinExt)
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()

        if exit_project == True: in_function = False
        
    return
        
def menuProyectoCorrige(proyecto,proyectoSinExt):               
    
    in_function = True
    while in_function:
        screen.paper(200,400,8)
        screen.text(300,600,[f"Corrige:  {proyectoSinExt}",
                        "1 - Datos base","2 - Datos proceso","3 - Excepciones"])
        screen.updateScreen()
        
        destino = screen.pushAndCome()
        if destino == "1":      menuProyectoCorrigeBase(proyecto,proyectoSinExt)
        elif destino == "2":    menuProyectoCorrigeProceso(proyecto,proyectoSinExt)
        elif destino == "3":    menuProyectoCorrigeExcepciones(proyecto,proyectoSinExt)
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return

def menuProyectoCorrigeBase(proyecto,proyectoSinExt):           
     
    carpeta = "Database/{}".format(proyecto)                                
    conexion,cursor = sql.creaAbreBd(carpeta)                                   
    listado = sql.SeleccionaTodasFilas(carpeta,"Datos")
                         
    listadoExtra = [listado[0][0],listado[0][1],listado[0][2],
                    listado[0][3],listado[0][4],listado[0][5],
                    listado[0][6],listado[0][7],listado[0][8],
                    listado[0][9],listado[0][10],listado[0][11],
                    listado[0][12],listado[0][13],listado[0][14]]           
    datos_a_pintar = [f"Modifica datos de {proyectoSinExt}","",
                      "Estado...",f"(A)ctiv (I)nactiv (C)lose: {listadoExtra[1]}",
                      f"Cliente: {listadoExtra[2]}", f"Inicio Proyecto: {listadoExtra[3]}",
                      f"Fecha Entrega: {listadoExtra[4]}", f"Páginas de origen: {listadoExtra[6]}",
                      f"(T)raduc. (C)orrec. {listadoExtra[7]}", f"Tabla Usar: {listadoExtra[8]}",
                      f"Calc.: (P)alab.(C)aract.p(A)g. {listadoExtra[5]}", f"Caracteres Holandesa: {listadoExtra[9]}",
                      f"Coste de la Holandesa: {listadoExtra[10]}", f"Palab. (O)rigen (D)estino: {listadoExtra[11]}",
                      f"Euros Página: {listadoExtra[12]}", f"% Correc: {listadoExtra[13]}",
                      f"Notas: {listadoExtra[14]}"]
        
    mensajeConPausa("Introduce datos (en blanco, mantiene antiguo)")
    
    screen.paper(209,1190,16,2)    
    posicion = 284
    for i in datos_a_pintar:
        
        screen.textAlone(1545,posicion,i)
        posicion += 59
        
    
    datos_necesarios = [listadoExtra[6],listadoExtra[4]]
    codigos_de_error = [15,4,14,2,4,5,4,6,4,4,7,4,8,0]
    datos_a_recuperar_tupla = cuestionarioProyecto(codigos_de_error,datos_necesarios)
    datos_a_recuperar = list(datos_a_recuperar_tupla)
    listadoExtra = [listadoExtra[1],listadoExtra[2],listadoExtra[3],
                    listadoExtra[4],listadoExtra[6],listadoExtra[7],
                    listadoExtra[8],listadoExtra[5],listadoExtra[9],
                    listadoExtra[10],listadoExtra[11],listadoExtra[12],
                    listadoExtra[13],listadoExtra[14]]
    
    for i in range(len(datos_a_recuperar)):
    
        if datos_a_recuperar[i] == "":
    
            datos_a_recuperar[i] = listadoExtra[i]
    
    sentencia = """UPDATE Datos SET Estado = ?, Cliente = ?, IncioProyecto = ?, 
                                    FechaEntrega = ?, UnidadCalculo = ?, PáginasOrigen = ?, 
                                    TipoTrabajo = ?, TablaUsar = ?, CaracteresHolandesa = ?, 
                                    EurosHolandesa = ?, PalabraOrigenDestino = ?, EurosPagina = ?, 
                                    TantoCientoCorrec = ?, Notas = ?"""        
    parametros = (datos_a_recuperar[0], datos_a_recuperar[1], datos_a_recuperar[2],
                  datos_a_recuperar[3], datos_a_recuperar[7], datos_a_recuperar[4],
                  datos_a_recuperar[5], datos_a_recuperar[6], datos_a_recuperar[8],
                  datos_a_recuperar[9], datos_a_recuperar[10], datos_a_recuperar[11],
                  datos_a_recuperar[12], datos_a_recuperar[13])                       
    sql.Modificar(cursor,sentencia,parametros)                              
    sql.CierraBd(conexion)  

    if datos_a_recuperar[0] == "A": 
        os.rename("Database/"+proyecto,"Database/"+proyecto.split(".")[0]+".dba")
    elif datos_a_recuperar[0] == "I":
        os.rename("Database/"+proyecto,"Database/"+proyecto.split(".")[0]+".dbi")
    elif datos_a_recuperar[0] == "C":
        os.rename("Database/"+proyecto,"Database/"+proyecto.split(".")[0]+".dbc")
                                                                          
    mensajeConPausa("Cambio realizado con éxito")        
    
    return                                          

def menuProyectoCorrigeProceso(proyecto,proyectoSinExt):        
    
    in_function = True
    while in_function:
        
        carpeta = "Database/{}".format(proyecto)                            
        try:
            
            tabla = sql.SeleccionaTodasFilas(carpeta,"Proceso")             
            listaDatosTablaProceso(proyecto,proyectoSinExt,[150,1050,1410,220])             

        except:
            
            mensajeConPausa("No hay procesos para este proyecto")
            in_function = False
            
        screen.paper(1000,400,3,2)
        screen.textAlone(750,1100,f"Elige el ID del proceso a corregir:")                                         
        screen.updateScreen()
        id_seleccionado = screen.AnswerChain([1400,1100,200,40],4)        

        conexion,cursor = sql.creaAbreBd(carpeta)                                                   
        
        try:
            
            fila = ""
            for fila_adecuada in tabla:  
                               
                if fila_adecuada[0] == int(id_seleccionado): 
                     
                    fila = fila_adecuada                
                    break 
                                              
            if fila == "": 
                   
                screen.SoundWrongAnswer()
                mensajeConPausa("No existe ese ID")
                in_function = False
            
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Error en la lectura del archivo")    
            in_function = False
            
        datos_a_pintar = [f"Modifica proceso de {proyectoSinExt} fila {id_seleccionado}","",
                        f"Fecha: {fila[1]}", f"Páginas: {fila[2]}",
                        f"Tipo (T)rad./correc (R)evisión) {fila[3]}:"]
        
        mensajeConPausa("Introduce datos (en blanco, mantiene antiguo)")
        
        screen.paper(150,1200,6,2)
        posicion = 225
        for i in datos_a_pintar:
            
            screen.textAlone(1555,posicion,i)
            posicion += 59
            
        screen.updateScreen()
        
        datos_a_recuperar_tupla = cuestionarioProcesos([14,4,12])
        datos_a_recuperar = list(datos_a_recuperar_tupla) 
        
        for i in range(len(datos_a_recuperar)):
            
            if datos_a_recuperar[i] == "":
                
                datos_a_recuperar[i] = fila[i+1]
        try:
            
            sentencia = "UPDATE Proceso SET Fecha = ?, Paginas = ?, Tipo = ? WHERE ID = ?"    
            parametros = (datos_a_recuperar[0],datos_a_recuperar[1],datos_a_recuperar[2],id_seleccionado)                      
            sql.Modificar(cursor,sentencia,parametros)                      
            sql.CierraBd(conexion)                                          
        
            listaDatosTablaProceso(proyecto,proyectoSinExt,[150,1050,1410,220])             
            mensajeConPausa("Datos modificados con éxito")      
               
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Error al modificar el proceso") 
               
        screen.updateScreen()
        time.sleep(2)
        screen.paper(1000,400,3,2)   
        in_function = False
        
    return   
 
def menuProyectoCorrigeExcepciones(proyecto,proyectoSinExt):    
    
    in_function = True
    while in_function:
        
        carpeta = "Database/{}".format(proyecto)                            
        try:
            
            tabla = sql.SeleccionaTodasFilas(carpeta,"Excepciones")             
            listaTablaExcepciones(proyecto,proyectoSinExt,[150,1050,1305,220])               

        except:
            mensajeConPausa("No hay excepciones para este proyecto")
            in_function = False
            
        screen.paper(1000,400,3,2)
        screen.textAlone(750,1100,f"Elige el ID de la excepción a corregir:")                                         
        screen.updateScreen()
        id_seleccionado = screen.AnswerChain([1400,1100,200,40],4)
        
        conexion,cursor = sql.creaAbreBd(carpeta)                                                   
        try:
            
            fila = ""
            
            for fila_adecuada in tabla:      
                           
                if fila_adecuada[0] == int(id_seleccionado):  
                    
                    fila = fila_adecuada                
                    break 
                                              
            if fila == "": 
                   
                screen.SoundWrongAnswer()
                mensajeConPausa("ID inexistente")
                in_function = False
                break
            
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Error en la lectura del archivo")    
            in_function = False
            
        datos_a_pintar = [f"Modifica excepción de {proyectoSinExt} fila {id_seleccionado}","",
                            f"Fecha: {fila[1]}"]
        
        mensajeConPausa("Introduce datos (en blanco, mantiene antiguo)")
        screen.paper(150,1200,6,2)
        posicion = 225
        for i in datos_a_pintar:
            
            screen.textAlone(1555,posicion,i)
            posicion += 59
            
        screen.updateScreen()
        fecha = cuestionarioExcepciones()
        datos_a_recuperar = [fecha]
        for i in range(len(datos_a_recuperar)):
            
            if datos_a_recuperar[i] == "":
                datos_a_recuperar[i] = fila[i+1]
        try:
            
            sentencia = """UPDATE Excepciones SET Fecha = ? WHERE ID = ?"""      
            parametros = (datos_a_recuperar[0],id_seleccionado)                      
            sql.Modificar(cursor,sentencia,parametros)                      
            sql.CierraBd(conexion)                                          
        
            listaTablaExcepciones(proyecto,proyectoSinExt,[150,1050,1305,220])               
            mensajeConPausa("Datos modificados con éxito")     
                
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Error al modificar la excepción")
        
        in_function = False
        
    return                         
  
def menuProyectoAnade(proyecto,proyectoSinExt):                 
    
    in_function = True
    while in_function:
        
        screen.paper(250,500,8)
        screen.text(350,700,[f"Añade a '{proyectoSinExt}'",
                    "1 - Datos proceso","2 - Excepciones"])
        
        screen.updateScreen()
        
        destino = screen.pushAndCome()
        if destino == "1":      menuProyectoAnadeProceso(proyecto,proyectoSinExt)
        elif destino == "2":    menuProyectoAnadeExcepcion(proyecto,proyectoSinExt)
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return

def menuProyectoAnadeProceso(proyecto,proyectoSinExt):          
    
    listaDatosTablaProceso(proyecto,proyectoSinExt,[300,2100,2450,420])             
    
    conexion,cursor = sql.creaAbreBd("Database/{}".format(proyecto))                                                                   
    insercionDatos = f'''CREATE TABLE IF NOT EXISTS Proceso(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Fecha TEXT, paginas INTEGER, Tipo TEXT)'''                                          
    cursor = sql.CreaUnaTabla(cursor,insercionDatos) 
        
    hoy = datetime.now()                                            
    hoy = hoy.strftime("%d/%m/%Y")                                  
    datos_a_pintar = [f"Añade proceso a {proyectoSinExt}","",f"Fecha: {hoy}","Páginas:","Tipo (T)rad./correc (R)evisión):"]
    
    in_function = True
    while in_function:
        
        in_answer = True
        while in_answer:
            
            screen.paper(150,1200,6,2)
            posicion = 225
            for i in datos_a_pintar:
                
                screen.textAlone(1555,posicion,i)
                posicion += 59
                
            screen.updateScreen()
            fecha,paginas,tipo = cuestionarioProcesos([1,4,12])
            screen.textAlone(1505,520,"Son correctos los datos introducidos? (S/N): ")
            screen.updateScreen()
            
            respuesta = screen.pushAndCome()
            if respuesta.upper() == "S":
                           
                in_answer = False
        
        conexion,cursor = sql.creaAbreBd("Database/{}".format(proyecto))                   
        introducimos = 'INSERT INTO Proceso (Fecha,Paginas,Tipo) VALUES (:Fecha,:Paginas,:Tipo)'
        parametros = {'Fecha':fecha,'Paginas':paginas,'Tipo':tipo}
        sql.anadeFila(cursor,introducimos,parametros,conexion)
        sql.CierraBd(conexion)                                      
        
        listaDatosTablaProceso(proyecto,proyectoSinExt,[300,2100,2450,420])             
        
        screen.textAlone(1555,579,"¿Quieres añadir otro proceso? (S/N): ")
        screen.updateScreen()
        respuesta = screen.pushAndCome()
        if respuesta.upper() == "N":
            
            in_function = False  
            mensajeConPausa("Proceso(s) añadido(s) con éxito")
                  
    return                                          

def cuestionarioProcesos(errores):
    
    fecha =     screen.AnswerChain([2080,343,500,40], errores[0])
    paginas =   screen.AnswerChain([2080,402,500,40], errores[1])
    tipo =      screen.AnswerChain([2080,461,500,40], errores[2])
    
    return fecha,paginas,tipo

def menuProyectoAnadeExcepcion(proyecto,proyectoSinExt):
            
    listaTablaExcepciones(proyecto,proyectoSinExt,[300,2100,2345,420])               
    
    conexion,cursor = sql.creaAbreBd("Database/{}".format(proyecto))                                                                   
    insercionDatos = f'''CREATE TABLE IF NOT EXISTS Excepciones(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Fecha TEXT)'''                                          
    cursor = sql.CreaUnaTabla(cursor,insercionDatos)
    datos_a_pintar = [f"Añade excepción a {proyectoSinExt}","","Fecha:"]
    
    in_function = True
    while in_function:
        
        in_answer = True
        while in_answer:
            
            screen.paper(150,1200,6,2)
            posicion = 225
            for i in datos_a_pintar:
                
                screen.textAlone(1555,posicion,i)
                posicion += 59
                
            screen.updateScreen()
            fecha = cuestionarioExcepciones()
            screen.textAlone(1555,520,"Son correctos los datos introducidos? (S/N): ")
            screen.updateScreen()
            respuesta = screen.pushAndCome()
            if respuesta.upper() == "S":
                
                in_answer = False
                
        conexion,cursor = sql.creaAbreBd("Database/{}".format(proyecto))                   
        introducimos = 'INSERT INTO Excepciones (Fecha) VALUES (:Fecha)'
        parametros = {'Fecha':fecha}
        sql.anadeFila(cursor,introducimos,parametros,conexion)
        sql.CierraBd(conexion)                                      
        
        listaTablaExcepciones(proyecto,proyectoSinExt,[300,2100,2345,420])               
        
        screen.textAlone(1555,579,"¿Quieres añadir otra excepción? (S/N): ")
        screen.updateScreen()
        respuesta = screen.pushAndCome()
        if respuesta.upper() == "N":
            
            mensajeConPausa("Excepción(es) añadida(s) con éxito")
            in_function = False  
             
    return                                             

def cuestionarioExcepciones():
    
    fecha = screen.AnswerChain([2000,343,500,40],13)
    
    return fecha

def menuProyectoTablas(proyecto,proyectoSinExt):                
    
    in_function = True
    while in_function:
        
        screen.paper(250,500,9)
        screen.text(350,700,[f"Tablas de '{proyectoSinExt}'",
                        "1 - Datos base","2 - Datos proceso","3 - Excepciones"])
        screen.updateScreen()
        
        destino = screen.pushAndCome()
        if destino == "1":      menuProyectoTablasBase(proyecto,proyectoSinExt)
        elif destino == "2":    menuProyectoTablasProceso(proyecto,proyectoSinExt)
        elif destino == "3":    menuProyectoTablasExcepciones(proyecto,proyectoSinExt)
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return

def menuProyectoTablasBase(proyecto,proyectoSinExt):  
              
    listaDatosTablasBase(proyecto,proyectoSinExt)               

    return

def listaDatosTablasBase(proyecto,proyectoSinExt):
    
    carpeta = "Database/{}".format(proyecto)                
    tabla = sql.SeleccionaTodasFilas(carpeta,"Datos")       
    screen.paper(150,1200,13,1)
    datos_a_pintar = [proyectoSinExt,"","Estado:","Cliente:",
                      "Inicio Proyecto:","Fecha Entrega:","Unidad de cálculo:",
                      "Páginas de origen:","Tipo Trabajo:","Tabla Usar:",
                      "Caracteres Holandesa:","Coste de la Holandesa:","Palab. Origen Destino:",
                      "Euros Página:","% Correc:","Notas:"]
    posicion = 220
    for i in datos_a_pintar:
        
        screen.textAlone(1435,posicion,i)
        posicion += 59
    
    posicion = 220
    frase = 0
    for i in tabla[0]:
        
        if frase == 1:
            
            if i == "A":    i = "Activo"
            elif i == "C":  i = "Cerrado"
            elif i == "I":  i = "Inactivo"
            
        elif frase == 5:
            
            if i == "P":    i = "Palabras"
            elif i == "C":  i = "Caracteres"
            elif i == "A":  i = "Páginas"
            
        elif frase == 7:
            
            if i == "T":    i = "Traducción"
            elif i == "C":  i = "Corrección"
            
        elif frase == 11:
            
            if i == "O":    i = "Origen"
            elif i == "D":  i = "Destino"
            
        elif posicion == int((screen.height*220)/1440):
            
            i = ""    
        screen.textAlone(1795,posicion,str(i))
        if posicion == int((screen.height*220)/1440):
            
            posicion += 59
            
        posicion += 59
        frase += 1
        
    screen.updateScreen()  
    
    return  

def menuProyectoTablasProceso(proyecto,proyectoSinExt): 
            
    listaDatosTablaProceso(proyecto,proyectoSinExt,[150,1050,1410,220])             
    
    return                    

def listaDatosTablaProceso(proyecto,proyectoSinExt,posiciones):
    
    carpeta = "Database/{}".format(proyecto)                        
    try:
        
        tabla = sql.SeleccionaTodasFilas(carpeta,"Proceso")  
                   
        if len(tabla) <= 3:
            
            valor = 5
            
        else:
            
            valor = len(tabla)+2
            
        screen.paper(posiciones[0],posiciones[1],valor,2)
        screen.textAlone(posiciones[2],posiciones[3],"Procesos de "+proyectoSinExt)
        
    except:
        
        screen.paper(posiciones[0],posiciones[1],3,2)
        screen.textAlone(posiciones[2],posiciones[3]+int((screen.height*100)/1440),"No hay procesos para "+proyectoSinExt)
        tabla = []
        
    posicion = posiciones[3]+int((screen.height*100)/1440)
    
    for i in tabla:
        
        if i[3] == "T":
            
            b = "Traducción"
            
        elif i[3] == "R":
            
            b = "Revisión"
            
        else:
            
            b = "Corrección"
            
        screen.textAlone(posiciones[2],posicion,f"{i[0]} - A {i[1]},  realicé")
        screen.textAlone(posiciones[2],posicion,f"                             {i[2]} páginas de {b}")
        posicion += 59  
        
    return  
            
def menuProyectoTablasExcepciones(proyecto,proyectoSinExt):   
      
    listaTablaExcepciones(proyecto,proyectoSinExt,[150,1200,1345,220])               

    return

def listaTablaExcepciones(proyecto,proyectoSinExt,posiciones):  
    
    carpeta = "Database/{}".format(proyecto)                            
    try:
        
        tabla = sql.SeleccionaTodasFilas(carpeta,"Excepciones") 
                    
        if len(tabla) <= 3:
            
            valor = 5
            
        else:
            
            valor = len(tabla)+2
            
        screen.paper(posiciones[0],posiciones[1],valor,1)
        screen.textAlone(posiciones[2],posiciones[3],"Excepciones de "+proyectoSinExt)
        
    except:
        
        screen.paper(posiciones[0],posiciones[1],3,1)
        screen.textAlone(posiciones[2],posiciones[3],"No hay excepciones para "+proyectoSinExt)
        tabla = []
        
    posicion = posiciones[3]+int((screen.height*100)/1440)
    for i in tabla:
        
        screen.textAlone(posiciones[2],posicion,f"{i[0]} - El {i[1]}, no se trabaja")
        posicion += 59    
    
    return

def menuProyectoElimina(proyecto,proyectoSinExt):               
    
    in_function = True
    while in_function:
        
        screen.paper(250,500,9)
        screen.text(350,700,[f"Elimina '{proyectoSinExt}'",
                    "1 - Proyecto entero","2 - Algún dato del proceso","3 - Alguna excepción"])
        screen.updateScreen()
        
        destino = screen.pushAndCome()
        
        resultado = False
        in_function = False
        if destino == "1":      resultado = menuProyectoEliminaProyecto(proyecto,proyectoSinExt)
        elif destino == "2":    menuProyectoEliminaProceso(proyecto,proyectoSinExt)
        elif destino == "3":    menuProyectoEliminaExcepcion(proyecto,proyectoSinExt)
        elif destino == "0":    in_function = False
        else:                   
            screen.SoundWrongAnswer()
            in_function = True
            
    return resultado
    
def menuProyectoEliminaProyecto(proyecto,proyectoSinExt):
    
           
    screen.paper(1000,400,3,2)
    screen.textAlone(750,1100,f"¿Seguro de que quieres eliminar {proyectoSinExt}? (S/N): ")                                         
    screen.updateScreen()
    respuesta = screen.pushAndCome()
    if respuesta.upper() == "S":                                                                                                            
        os.remove("Database/{}".format(proyecto))                                                                                           
        screen.SoundKillData()
        screen.textAlone(750,1159,"Proyecto eliminado con éxito")
        screen.updateScreen()
        time.sleep(1)
        screen.paper(1000,400,3,2)
        return  True                                                                                                                       
    else:
        screen.paper(1000,400,3,2)
        return  False                                                                                                        
            
def menuProyectoEliminaProceso(proyecto,proyectoSinExt):
            
    in_function = True
    while in_function:
            
        carpeta = "Database/{}".format(proyecto)                            
        try:
            
            tabla = sql.SeleccionaTodasFilas(carpeta,"Proceso")             
        
        except:
            
            screen.paper(1000,400,3,2)
            screen.textAlone(750,1159,"No hay procesos para este proyecto")
            screen.updateScreen()
            time.sleep(2)
            screen.paper(1000,400,3,2)
            in_function = False
            break
                                                
        listaDatosTablaProceso(proyecto,proyectoSinExt,[300,2100,2450,420])             
        screen.paper(1000,400,3,2)
        screen.textAlone(750,1100,f"Elige el ID del proceso a borrar:")                                         
        screen.updateScreen()
        
        id_seleccionado = screen.AnswerChain([1400,1100,200,40],4)
        screen.textAlone(750,1159,f"¿Quieres eliminar el proceso {id_seleccionado}? (S/N): ")                                         
        screen.updateScreen()
        
        respuesta = screen.pushAndCome()
        if respuesta.upper() == "S":    
                                                                                                                    
            try:             
                                                                       
                id_de_linea_a_borrar = None
                for i in tabla:     
                                                                    
                    if i[0] == int(id_seleccionado):  
                                                                
                            id_de_linea_a_borrar = int(id_seleccionado)                                        
                            break     
                                                                          
                if id_de_linea_a_borrar is not None:
                    
                    conexion,cursor = sql.creaAbreBd(carpeta)                               
                    sql.EliminaFilaenTabPro(cursor,"Proceso",id_de_linea_a_borrar)                   
                    sql.CierraBd(conexion)                                              
                    mensajeConPausa("Proyecto eliminado con éxito")
                    listaDatosTablaProceso(proyecto,proyectoSinExt,[300,2100,2385,420])  
                               
                else:
                    
                    screen.SoundWrongAnswer()
                    mensajeConPausa("No existe el ID seleccionado")
                    
            except:             
                                                                    
                    screen.SoundWrongAnswer()
                    mensajeConPausa("Error al borrar el proceso")                                              
            
            in_function = False
                                                     
        return
    
def menuProyectoEliminaExcepcion(proyecto,proyectoSinExt): 

    in_function = True
    while in_function:
                 
        carpeta = "Database/{}".format(proyecto)                                                
        try:
        
            tabla = sql.SeleccionaTodasFilas(carpeta,"Excepciones")                                 
        
        except:
        
            screen.paper(1000,400,3,2)
            screen.textAlone(750,1159,"No hay excepciones para este proyecto")
            screen.updateScreen()
            time.sleep(2)
            screen.paper(1000,400,3,2)
            in_function = False                                          
        
        listaTablaExcepciones(proyecto,proyectoSinExt,[300,2100,2345,420])               
        screen.paper(1000,400,3,2)
        screen.textAlone(750,1100,f"Elige el ID de la excepción a borrar:")                                         
        screen.updateScreen()
        
        id_seleccionado = screen.AnswerChain([1400,1100,200,40],4)
        screen.textAlone(750,1159,f"¿Quieres eliminar la excepción {id_seleccionado}? (S/N): ")                                         
        screen.updateScreen()
        
        respuesta = screen.pushAndCome()
        if respuesta.upper() == "S":  
                                                                                                                      
            try:                
                                                                        
                id_de_linea_a_borrar = None 
                
                for i in tabla:   
                                                                          
                    if i[0] == int(id_seleccionado): 
                        
                            id_de_linea_a_borrar = int(id_seleccionado)                                        
                            break     
                                                                          
                if id_de_linea_a_borrar is not None:
                    
                    conexion,cursor = sql.creaAbreBd(carpeta)                                   
                    sql.EliminaFilaenTabPro(cursor,"Excepciones",id_de_linea_a_borrar)                 
                    sql.CierraBd(conexion)                                                  
                    screen.SoundKillData()
                    mensajeConPausa("Excepción eliminada con éxito")
                    listaTablaExcepciones(proyecto,proyectoSinExt,[300,2100,2305,420]) 
                                  
                else:
                    
                    screen.SoundWrongAnswer()
                    mensajeConPausa("No existe el ID seleccionado")
                    
            except:     
                                                                                
                    screen.SoundWrongAnswer()
                    mensajeConPausa("Error al borrar la excepción")
                    
            in_function = False
            
        return                                        
        
def menuProyectoGraficas(proyecto,proyectoSinExt):              

    carpeta = "Database/{}".format(proyecto)                            
    conexion,cursor = sql.creaAbreBd(carpeta)                               
    Datos = sql.SeleccionaTodasFilas(carpeta,"Datos")                  
    
    try:
        
        Procesos = sql.SeleccionaTodasFilas(carpeta,"Proceso")              
   
    except:
        
        Procesos = []
   
    try:
        
        Excepciones = sql.SeleccionaTodasFilas(carpeta,"Excepciones")       
    
    except:
        
        Excepciones = []
        
    conexion.close()                                                    
    screen.paperGraph(proyectoSinExt,Datos,Procesos,Excepciones)
    
    return
    
def menuCreaProyecto():     
                                        
    hoy = datetime.now()
    hoy = hoy.strftime("%d/%m/%y")
    datos_a_pintar = ["Creando un proyecto","","Nombre:","Estado...","(A)ctiv (I)nactiv (C)lose:","Cliente:",
                      "Inicio Proyecto:"+hoy,"Fecha Entrega:","Páginas de origen:",
                      "(T)raduc. (C)orrec.","Tabla Usar:","Calc.: (P)alab.(C)aract.p(A)g.",
                      "Caracteres Holandesa:","Coste de la Holandesa:","Palab. (O)rigen (D)estino:",
                      "Euros Página:","% Correc:","Notas:"]    
    screen.paper(150,1200,16,2)
    posicion = 225
    for i in datos_a_pintar:
        
        screen.textAlone(1555,posicion,i)
        posicion += 59
        
    screen.updateScreen()
    nombre = screen.AnswerChain([2000,346,600,40],9)

    codigos_de_error = [3,4,1,2,4,5,4,6,4,4,7,4,8,0]
    datos_necesarios = ["",""]
    estado,cliente,inicio_proyecto,fecha_entrega,paginas_origen,tipo_trabajo,tabla_usar,unidad_calculo,caracteres_holandesa,coste_holandesa,palabra_origen_destino,euros_pagina,tanto_ciento_correc,notas = cuestionarioProyecto(codigos_de_error,datos_necesarios)
    crea_tabla = f'''
                     CREATE TABLE IF NOT EXISTS Datos(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Estado TEXT,
                            Cliente TEXT,
                            IncioProyecto TEXT,
                            FechaEntrega TEXT,
                            UnidadCalculo TEXT,
                            PáginasOrigen INTEGER,
                            TipoTrabajo TEXT,
                            TablaUsar TEXT,
                            CaracteresHolandesa INTEGER,
                            EurosHolandesa REAL,
                            PalabraOrigenDestino TEXT,
                            EurosPagina REAL,
                            TantoCientoCorrec INTEGER,
                            Notas TEXT)
    '''                                                                                     
    if estado == "A":   
                                                                    
        BdProyecto,cursor = sql.creaAbreBd(f"Database/{nombre}.dba")   
                         
    elif estado == "I":  
                                                                   
        BdProyecto,cursor = sql.creaAbreBd(f"Database/{nombre}.dbi")          
                  
    elif estado == "C":    
                                                                 
        BdProyecto,cursor = sql.creaAbreBd(f"Database/{nombre}.dbc")    
                        
    cursor = sql.CreaUnaTabla(cursor,crea_tabla)                                        
    
    insertamos = f'''INSERT INTO Datos (Estado,Cliente,IncioProyecto,FechaEntrega,
                UnidadCalculo, PáginasOrigen, TipoTrabajo, TablaUsar,
                CaracteresHolandesa, EurosHolandesa, PalabraOrigenDestino,
                EurosPagina, TantoCientoCorrec, Notas) VALUES (
                    :estado,:cliente,:inicio,:entrega,:unidad,
                    :paginas,:tipo,:tabla,:caracteres,:euros,
                    :palabra,:eurospag,:tanto,:notas)'''                                    
    estos_datos = {'estado':estado, 'cliente':cliente, 'inicio':inicio_proyecto, 
              'entrega':fecha_entrega, 'unidad':unidad_calculo, 'paginas':paginas_origen, 
              'tipo':tipo_trabajo, 'tabla':tabla_usar, 'caracteres':caracteres_holandesa, 
              'euros':coste_holandesa, 'palabra':palabra_origen_destino, 'eurospag':euros_pagina, 
              'tanto':tanto_ciento_correc, 'notas':notas}                                     
    sql.anadeFila(cursor, insertamos, estos_datos, BdProyecto)                                          
    sql.CierraBd(BdProyecto) 
    
    mensajeConPausa("Proyecto creado con éxito")
                                                                                   
    return    

def cuestionarioProyecto(errores,datos_necesarios):   
                                      
    tabla_usar,unidad_calculo,caracteres_holandesa,coste_holandesa,palabra_origen_destino,euros_pagina, = "", "","","","",""
    estado = screen.AnswerChain([2000,464,600,40],errores[0])
    listado,carpeta = preparaListaClientes()                                            
    listaClientes(listado)                                            
    cliente = screen.AnswerChain([2000,523,600,40],errores[1])
    inicio_proyecto = screen.AnswerChain([2000,582,600,40],errores[2])   
    fecha_entrega = screen.AnswerChain([2000,641,600,40],errores[3])
    paginas_origen = screen.AnswerChain([2000,700,600,40],errores[4])
    tipo_trabajo = screen.AnswerChain([2000,759,600,40],errores[5])
    if tipo_trabajo == "C" or tipo_trabajo == "" and datos_necesarios[0] == "C":
        listado,carpeta = preparaListaTablas()
        listaTablas(listado)
        tabla_usar = screen.AnswerChain([2000,818,600,40],errores[6]) 
    elif tipo_trabajo == "T" or tipo_trabajo == "" and datos_necesarios[0] == "T":
        unidad_calculo = screen.AnswerChain([2000,877,600,40],errores[7]) 
        if unidad_calculo == "C" or unidad_calculo == "" and datos_necesarios[1] == "C":
            caracteres_holandesa = screen.AnswerChain([2000,936,600,40],errores[8]) 
            coste_holandesa = screen.AnswerChain([2000,995,600,40],errores[9])
        elif unidad_calculo == "P" or unidad_calculo == "" and datos_necesarios[1] == "P":
            palabra_origen_destino = screen.AnswerChain([2000,1054,600,40],errores[10]) 
        else:
            euros_pagina = screen.AnswerChain([2000,1113,600,40],errores[11]) 
    tanto_ciento_correc = screen.AnswerChain([2000,1172,600,40],errores[12])
    notas = screen.AnswerChain([2000,1231,600,40],errores[13])    
      
    return estado,cliente,inicio_proyecto,fecha_entrega,paginas_origen,tipo_trabajo,tabla_usar,unidad_calculo,caracteres_holandesa,coste_holandesa,palabra_origen_destino,euros_pagina,tanto_ciento_correc,notas
            
def menuClientes():                
        
    in_function = True
    while in_function:
        
        screen.paper(100,200,10)
        screen.text(200,400,[f"Menú de Clientes",
                    "1 - Crear Cliente","2 - Consultar Cliente","3 - Modificar Cliente","4 - Eliminar Cliente"])
        screen.updateScreen()
        
        destino = screen.pushAndCome()
        if destino == "1":      creaCliente()
        elif destino == "2":    consultaCliente()
        elif destino == "3":    modificaCliente()
        elif destino == "4":    eliminaCliente()
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return
    
def creaCliente():   
                                               
    listado,carpeta = preparaListaClientes()
    listaClientes(listado)

    datos_a_pintar = ["Creando un cliente","","Nombre:","",
                      "Teléfono:","Dirección:","NIF:",
                      "Contacto:","Teléfono contacto:",
                      "Email contacto:","Pago previo:"]
    in_function = True
    while in_function:   
         
        in_answer = True
        while in_answer:  
              
            screen.paper(150,1200,11,2)    
            posicion = 225
            for i in datos_a_pintar:
                
                screen.textAlone(1555,posicion,i)
                posicion += 59
                
            screen.updateScreen()
            nombre = screen.AnswerChain([2000,346,600,40],9)
            telefono,direccion,nif,contacto,telefono_contacto,email_contacto,pago_previo = cuestionarioClientes()

            screen.textAlone(1555,877,"¿Son correctos los datos (S/N)?")
            screen.updateScreen()
            respuesta = screen.pushAndCome()
            if respuesta.upper() == "S":
                
                in_answer = False
            
        conexion,cursor = sql.creaAbreBd(carpeta)                           
        insertamos = f'INSERT INTO Clientes (Nombre, Telefono, Direccion, Nif, Contacto, TelContacto, EmailContacto,PagoPrevio ) VALUES (:nombre, :telefono, :direccion, :nif, :contacto, :telContacto, :emailContacto, :pagoPrevio)'   
        esos_datos = {'nombre' : nombre, 'telefono' : telefono, 
                'direccion' : direccion, 'nif' : nif, 
                'contacto' : contacto, 'telContacto' : telefono_contacto, 
                'emailContacto' : email_contacto, 'pagoPrevio' : pago_previo}                                
        sql.anadeFila(cursor,insertamos,esos_datos,conexion)                                            
        sql.CierraBd(conexion) 
                                                                                     
        listado,carpeta = preparaListaClientes()                                            
        listaClientes(listado)                                            
        screen.textAlone(1555,936,"¿Quieres crear otro cliente (S/N)?")
        screen.updateScreen()
        
        respuesta = screen.pushAndCome()
        if respuesta.upper() == "N":
            
            mensajeConPausa("Cliente(s) creado(s) con éxito")
            in_function = False
            
    return                                              
 
def cuestionarioClientes(): 
                                                  
    telefono = screen.AnswerChain([2000,464,600,40],4)
    direccion = screen.AnswerChain([2000,523,600,40])
    nif = screen.AnswerChain([2000,582,600,40])
    contacto = screen.AnswerChain([2000,641,600,40])
    telefono_contacto = screen.AnswerChain([2000,700,600,40],4)
    email_contacto = screen.AnswerChain([2000,759,600,40])
    pago_previo = screen.AnswerChain([2000,818,600,40],4)
    
    return telefono,direccion,nif,contacto,telefono_contacto,email_contacto,pago_previo
    
def consultaCliente():     
                                         
    in_function = True
    while in_function:
        
        listado,carpeta = preparaListaClientes()                                            
        listaClientes(listado)                                            

        opciones = ["0"]
        for i in range (1,len(listado)+1):
            
            opciones.append(str(i))
        
        in_answer = True                                                                           
        while in_answer:                                                                           
        
            opcion = screen.pushAndCome()
            if opcion in opciones:                                                              
        
                in_answer = False                                                                  
        
        opcion = int(opcion)
        if opcion == 0: 
            
            in_function = False
            in_answer = False
            break 
        
        cliente = listado[int(opcion)-1]                                               
        
        filas = sql.MuestraDato(carpeta,cliente,"Clientes")                       
        if len(filas[0])<3:
        
            valor = 3
        
        else:
        
            valor = len(filas[0])+2
        
        screen.paper(100,700,valor,2)
        screen.textAlone(435,220,"Datos del cliente "+cliente)
        titulos = ["ID","Nombre:","Teléfono:","Dirección:","NIF:","Contacto:","Teléfono contacto:","Email contacto:","Pago previo:"]
        posicion = 320
        orden = 0
        for i in filas[0]:
        
            screen.textAlone(1035,posicion,f"{titulos[orden]}")
            screen.textAlone(1275,posicion,f"       {i}")
            orden += 1
            posicion += 59
        
        in_function = False
        
    return                                                                  

def preparaListaClientes():
    
    carpeta =           "Database/Clientes.db"                                                        
    conexion,cursor =   sql.creaAbreBd(carpeta)                                                   
    consulta =          "SELECT Nombre FROM Clientes;"                                               
    listado =           sql.listados(cursor,consulta)                                          
    sql.CierraBd(conexion) 
                                                                     
    return listado,carpeta
    
def listaClientes(listado):      
                                          
    if len(listado)<3:
        screen.paper(150,300,5)
    else:
        screen.paper(150,300,len(listado)+5)
        
    todos_clientes = ["Todos los clientes"]
    numeracion = 1
    for i in listado:
        
        todos_clientes.append(f"{numeracion} - {i}")
        numeracion += 1
        
    screen.text(250,500,todos_clientes)
    screen.updateScreen()

def modificaCliente():                                          

    in_function = True
    while in_function:
        
        carpeta = "Database/Clientes.db"
        try:
            
            lista_clientes, carpeta = preparaListaClientes()
            listaClientes(lista_clientes)
            
        except:
            
            mensajeConPausa("No hay clientes")                                  
            in_function = False
            break
            
        screen.paper(1000,400,3,2)
        screen.textAlone(750,1100,f"Elige el ID del cliente a modificar:")
        screen.updateScreen()
        id_seleccionado = screen.AnswerChain([1400,1100,200,40],4)
        
        if id_seleccionado == "0":
        
            in_function = False
            break
        
        cliente = lista_clientes[int(id_seleccionado)-1]
        fila = sql.MuestraDato(carpeta,cliente,"Clientes")
        
        datos_a_pintar = [f"Modificando un cliente","",f"Nombre: {fila[0][1]}","",f"Teléfono: {fila[0][2]}",
                          f"Dirección: {fila[0][3]}",f"NIF: {fila[0][4]}",f"Contacto: {fila[0][5]}",
                          f"Teléfono contacto: {fila[0][6]}",f"Email contacto: {fila[0][7]}",
                          f"Pago previo: {fila[0][8]}"]
        
        mensajeConPausa("Introduce datos (en blanco, mantiene antiguo)")
        
        screen.paper(150,1200,11,2)
        posicion = 225
        for i in datos_a_pintar:
            
            screen.textAlone(1555,posicion,i)
            posicion += 59
            
        screen.updateScreen()
        
        cliente_tupla = cuestionarioClientes()
        cliente = list(cliente_tupla)
        
        for i in range(len(cliente)):
            
            if cliente[i] == "":
                cliente[i] = fila[0][i+2]
        try:
            
            sentencia = """UPDATE Clientes SET Telefono = ?, Direccion = ?,
                        Nif = ?, Contacto = ?, TelContacto = ?, EmailContacto = ?,
                        PagoPrevio = ? WHERE Nombre = ?"""
            parametros = (cliente[0], cliente[1], cliente[2],
                        cliente[3], cliente[4], cliente[5],
                        cliente[6], id_seleccionado)
            conexion,cursor = sql.creaAbreBd(carpeta)
            sql.Modificar(cursor,sentencia,parametros)
            sql.CierraBd(conexion)
            
            lista_clientes, carpeta = preparaListaClientes()
            listaClientes(lista_clientes)
            
            mensajeConPausa("Cliente modificado con éxito")
            
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Error al modificar el cliente")
            
        in_function = False  
        
    return
                                                             
def eliminaCliente():                                           
    
    in_function = True
    while in_function:
        
        carpeta = "Database/Clientes.db"                                                        
        try:
            
            nombres,carpeta = preparaListaClientes()                                            
            listaClientes(nombres)   
                                                     
        except:
            
            screen.paper(1000,600,3,2)
            screen.textAlone(950,1159,"No hay clientes")
            screen.updateScreen()
            time.sleep(2)
            screen.paper(1000,600,3,2)
            in_function = False                                         
        
        screen.paper(1000,600,3,2)
        screen.textAlone(950,1100,f"Elige el ID del cliente a borrar:")                                         
        screen.updateScreen()
        id_seleccionado = screen.AnswerChain([1600,1100,200,40],4)
        
        screen.textAlone(950,1159,f"¿Quieres eliminar el cliente {id_seleccionado}? (S/N): ")                                         
        screen.updateScreen()
        respuesta = screen.pushAndCome()
        
        tabla = sql.SeleccionaTodasFilas(carpeta,"Clientes")                                 
        
        if respuesta.upper() == "S":    
                                                                                                                    
            try:  
                                                                                  
                id_de_linea_a_borrar = None
                sumatorio = 1
                for i in tabla: 
                                                                        
                    if sumatorio == int(id_seleccionado):
                        
                        id_de_linea_a_borrar = i[0]                                        
                        break    
                                                                       
                    sumatorio += 1
                if id_de_linea_a_borrar is not None:
                    
                    conexion,cursor = sql.creaAbreBd(carpeta)                               
                    sql.EliminaFilaenTabPro(cursor,"Clientes",id_de_linea_a_borrar)                   
                    sql.CierraBd(conexion)                                              
                    screen.SoundKillData()
                    screen.textAlone(950,1208,"Cliente eliminado con éxito")
                    nombres, carpeta = preparaListaClientes()                                            
                    listaClientes(nombres) 
                                                               
                else:
                    
                    screen.SoundWrongAnswer()
                    screen.textAlone(950,1208,"No existe el ID seleccionado")
                    
            except:  
                                                                               
                    screen.SoundWrongAnswer()
                    screen.textAlone(950,1208,"Error al borrar el cliente")
                    
            screen.updateScreen()
            time.sleep(2)
            screen.paper(1000,600,3,2)
        
        in_function = False
            
    return                                                                  

def menuTablasCorreccion():    
    
    in_function = True
    while in_function:
        
        screen.paper(100,200,10)
        screen.text(200,400,[f"Menú de Tablas para Corrección",
                    "1 - Crear tabla","2 - Consultar tabla","3 - Modificar tabla","4 - Eliminar tabla"])
        screen.updateScreen()
    
        destino = screen.pushAndCome()
        if destino == "1":      creaTabla()
        elif destino == "2":    consultaTabla()
        elif destino == "3":    modificaTabla()
        elif destino == "4":    eliminaTabla()
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return                             

def creaTabla():  
                                                  
    listado,carpeta = preparaListaTablas()
    listaTablas(listado)
    nombre = ""
    datos_a_pintar = ["Creando una tabla","","Nombre:",
                    "De:","A:","Euros/palabra:"]
    conexion,cursor = sql.creaAbreBd("Database/Tablas.db")            

    in_function = True
    while in_function:
        
        in_answer = True                                                                           
        while in_answer:                                                                           

            screen.paper(150,1200,7,2)
            posicion = 225
            for i in datos_a_pintar:
                
                screen.textAlone(1555,posicion,i)
                posicion += 59
                
            screen.updateScreen()
            if nombre == "":
                
                nombre = screen.AnswerChain([2000,346,600,40],9)
                crea_tabla = f'''
                   CREATE TABLE IF NOT EXISTS {nombre}(
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       De INTEGER,
                       A INTEGER,
                       Euros REAL
                   )
                   '''
                cursor = sql.CreaUnaTabla(cursor,crea_tabla)   
                                                     
            else:
                
                screen.textAlone(1950,346,nombre)
                
            sql.CierraBd(conexion)                                                                  
            de,a,euros = cuestionarioTabla()
            
            screen.textAlone(1555,582,"¿Es correcto (S/N)?")
            screen.updateScreen()
            
            respuesta = screen.pushAndCome()
            if respuesta == "S" or respuesta == "s":
                
                in_answer = False
                
        conexion,cursor = sql.creaAbreBd(carpeta)                           
        insertamos = f'INSERT INTO {nombre} (De, A, Euros) VALUES (:de, :a, :euros)'   
        esos_datos = {'de' : de,'a' : a, 'euros' : euros}                                
        sql.anadeFila(cursor,insertamos,esos_datos,conexion)                                            
        sql.CierraBd(conexion)  
                                                                                    
        lineas = sql.SeleccionaTodasFilas(carpeta,nombre)
        listaLaTabla(lineas,nombre,[300,2100,2435,420])        
        screen.textAlone(1555,641,"¿Quieres crear otra linea (S/N)?")
        screen.updateScreen()
        
        respuesta = screen.pushAndCome()
        if respuesta == "N" or respuesta == "n":
            
            mensajeConPausa("Tabla creada con éxito")
            in_function = False
  
    return                 

def cuestionarioTabla():
    
    de = screen.AnswerChain([2000,405,600,40],4)
    a = screen.AnswerChain([2000,464,600,40],4)
    euros = screen.AnswerChain([2000,523,600,40],11)
    
    return de,a,euros
   
def consultaTabla():         
                                       
    in_function = True
    while in_function:
        
        listado,carpeta = preparaListaTablas()                                            
        listaTablas(listado)                                            
        
        opciones = ["0"]                                                                        
        for i in range(1,len(listado)+1):                                                       
            opciones.append(str(i))                                                             
        cotejo = True                                                                           
        while cotejo:                                                                           
            opcion = screen.pushAndCome()
            if opcion in opciones:                                                              
                cotejo = False                                                                  
        opcion = int(opcion)                                                                    
        if opcion == 0: in_function = False                                                 
        
        try:
            
            tabla = ""
            tabla = listado[int(opcion)-1]                                                   
        
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Tabla inexistente")
            in_function = False
            break
        
        filas = sql.SeleccionaTodasFilas(carpeta,tabla)                                 
        listaLaTabla(filas,tabla,[100,700,1035,220])                                            
        in_function = False
        
    return tabla                                                         

def listaLaTabla(filas,tabla,posiciones): 
                                               
    if len(filas)<3:
        
        valor = 5
        
    else:
        
        valor = len(filas)+2
        
    screen.paper(posiciones[0],posiciones[1],valor,2)
    screen.textAlone(posiciones[2],posiciones[3],"Tabla "+tabla)
    posicion = posiciones[3]+100
    for i in filas:
        
        screen.textAlone(posiciones[2],posicion,f"{i[0]} - De {i[1]:} a")
        screen.textAlone(posiciones[2],posicion,f"                     {i[2]:} palabras,")
        screen.textAlone(posiciones[2],posicion,f"                                         {i[3]:>5} €/palabra")
        posicion += 59    
    
    return

def preparaListaTablas():
    
    carpeta =           "Database/Tablas.db"                                                          
    conexion,cursor =   sql.creaAbreBd(carpeta)                                                   
    consulta =          "SELECT name FROM sqlite_master WHERE type='table';"                         
    listado =           sql.listados(cursor,consulta)                                          
    sql.CierraBd(conexion)
    
    return listado,carpeta

def listaTablas(listado):
                                                
    if len(listado)<3:
        
        screen.paper(150,300,5)
        
    else:
        
        screen.paper(150,300,len(listado)+5)
        
    todas_tablas = ["Listado de tablas"]
    numeracion = 1
    for i in listado:
        
        todas_tablas.append(str(numeracion) +" - " + str(i))
        numeracion += 1
        
    screen.text(250,500,todas_tablas)
    screen.updateScreen()
     
    return
              
def modificaTabla():                                            
    
    in_function = True
    while in_function:
        
        tabla_a_modificar = consultaTabla()   
                
        screen.paper(1000,400,3,2)
        screen.textAlone(750,1100,f"Elige el ID de la linea a modificar:")
        screen.updateScreen()
        id_seleccionado = screen.AnswerChain([1400,1100,200,40],4)
        
        if id_seleccionado == "0":
            
            in_function = False
            break
        
        try:
            
            lista_tablas, carpeta = preparaListaTablas()
            for i in range(len(lista_tablas)):
                    
                    if lista_tablas[i] == tabla_a_modificar:
                        tabla = lista_tablas[i]
                        break
                            
            linea = int(id_seleccionado)
            
            conexion,cursor = sql.creaAbreBd(carpeta)
            sentencia = f"SELECT * FROM {tabla} WHERE ID = ?"
            parametros = (linea,)
            fila = sql.DevuelveConsulta(cursor,sentencia,parametros)
            
            datos_a_pintar = [f"Modificando una tabla",f"Nombre: {tabla}","",f"De: {fila[1]}",
                            f"A: {fila[2]}",f"Euros/palabra: {fila[3]}"]
        
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("ID inexistente")
            in_function = False
            break
        
        mensajeConPausa("Introduce datos (en blanco, mantiene antiguo)")
        
        screen.paper(150,1200,6,2)
        posicion = 225
        for i in datos_a_pintar:
            
            screen.textAlone(1555,posicion,i)
            posicion += 59
            
        screen.updateScreen()
        
        tabla_tupla = cuestionarioTabla()
        tabla = list(tabla_tupla)
        
        for i in range(len(tabla)):
            
            if tabla[i] == "":
                tabla[i] = fila[i+1]
                
        try:
            
            sentencia = """UPDATE """+tabla_a_modificar+""" SET De = ?, A = ?,
                        Euros = ? WHERE ID = ?"""
            parametros = (tabla[0], tabla[1], tabla[2],
                        linea)
            conexion,cursor = sql.creaAbreBd(carpeta)
            sql.Modificar(cursor,sentencia,parametros)
            sql.CierraBd(conexion)
                
            lista_tablas, carpeta = preparaListaTablas()
            listaTablas(lista_tablas)
                
            mensajeConPausa("Tabla modificada con éxito")
            
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Error al modificar la tabla")
            
        in_function = False
        
    return
                                    
def eliminaTabla(): 
                                                
    in_function = True
    while in_function:
        
        carpeta = "Database/Tablas.db"                                                          
        try:
            
            nombres,carpeta = preparaListaTablas()                                            
            listaTablas(nombres)   
                                                     
        except:
            
            screen.paper(1000,600,3,2)
            screen.textAlone(950,1159,"No hay tablas")
            screen.updateScreen()
            time.sleep(2)
            screen.paper(1000,600,3,2)
            in_function = False                                         
            
        screen.paper(1000,600,3,2)
        screen.textAlone(950,1100,f"Elige el ID de la tabla a borrar:")                                         
        screen.updateScreen()
        id_seleccionado = screen.AnswerChain([1600,1100,200,40],4)
        
        screen.textAlone(950,1159,f"¿Quieres eliminar la tabla {id_seleccionado}? (S/N): ")                                         
        screen.updateScreen()
        respuesta = screen.pushAndCome()

        if respuesta.upper() == "S":   
                                                                                                                     
            try:  
                                                                                  
                conexion,cursor = sql.creaAbreBd(carpeta)                                                   
                consulta = "SELECT name FROM sqlite_master WHERE type='table';"                         
                listado = sql.listados(cursor,consulta)                                          
                tabla = listado[int(id_seleccionado)-1]                                                   
                sql.eliminaTabla(cursor,tabla)                                                  
                sql.CierraBd(conexion)                    
                screen.SoundKillData()
                mensajeConPausa("Tabla eliminada con éxito")
                nombres, carpeta = preparaListaTablas()                                            
                listaTablas(nombres)  
                                                          
            except:
                
                screen.SoundWrongAnswer()
                mensajeConPausa("Error al borrar la tabla")
                
        screen.paper(1000,600,3,2)
        in_function = False                                                                  

    return                                           

def exit(): 
                                                        
    screen.fadeOut()                                                
    sys.exit()                              

def mensajeConPausa(mensaje):
    
    screen.paper(1000,600,3,2)
    screen.textAlone(960,1159,mensaje)
    screen.updateScreen()
    time.sleep(2)
    screen.paper(1000,600,3,2)
    screen.updateScreen()
                                
if __name__ == "__main__":                                      
    
    screen.run()
    comprobarExistenciaCarpeta()
    screen.fadeIn()
    screen.animaLogoEntra()    
    menuInicial()    