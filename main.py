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
        mensajeConPausa             ("Error. No existe\nla carpeta contenedora adecuada")
        mensajeConPausa             ("Se creará\nla carpeta contenedora adecuada")
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
        
        destino = screen.pushAndCome(options = 5)
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

        screen.paper(50,100,9)
        screen.text(150,300,["Abrir proyecto","1 - Activo","2 - Inactivo","3 - Cerrado"])
        screen.updateScreen()
            
        tipo_proyecto = ""
        destino = screen.pushAndCome(options = 4)
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
            extensión = [".dba",".dbi",".dbc"]
            palabras = ["Activo","Inactivo","Cerrado"]
            for i in range(3):
                if tipo_proyecto == extensión[i]:
                    final = palabras[i]
                    break

            mensajeConPausa("Elige opción\nCursores mueve lista",
                    False,False)
            
            posicion = 0
            numeracion = 1
            in_rotative = True
            while in_rotative:
                screen.paper(50,100,12,False)
                data = []
                lista_corta = datos[posicion:posicion+7]
                for i in lista_corta:
                    if len(i) > 19:
                        i = i[:19]
                        i = i + "..."
                    data.append(i)
                opciones_de_menu = [f"Abrir proyecto {final}"]
                for i in data:

                    i = f"{numeracion} - {i}"
                    opciones_de_menu.append(i)
                    numeracion += 1

                if cantidad == 0:

                    screen.SoundWrongAnswer()
                    mensajeConPausa(f"No existen proyectos\n{final}")
                    in_function = False
                    break                
                screen.text(150,300,opciones_de_menu)
                screen.updateScreen()
                time.sleep(0.1)
                opciones = [str(i) for i in range(0,cantidad+1)]
                    
                opcion = screen.pushAndCome(suma=posicion,options = 8)
                if opcion == "98":
                    if posicion >0:
                        posicion -=1
                    numeracion = posicion+1
                elif opcion == "99":
                    if posicion < len(datos) - 7:
                        posicion += 1
                    numeracion = posicion+1
                elif opcion in opciones:
                    in_rotative = False
                else:
                    numeracion = posicion+1
                            
            opcion = int(opcion)      
            if opcion == 0:  
                    
                in_function = False                                                  
                
            else:                                                                                   
                    
                Proyecto = DiccionarioFiles[opcion-1]                                         
                proyectoSinExt = Proyecto.split(".")[0]
                if len(proyectoSinExt) >22:
                    proyectoSinExt = proyectoSinExt[:22]
                    proyectoSinExt = proyectoSinExt + "..."
                        
                in_function = False                                  
                menuProyectoCRUD(Proyecto,proyectoSinExt)                                           
        
        return
    
def menuProyectoCRUD(proyecto,proyectoSinExt): 
    
    in_function = True
    while in_function:  
        
        exit_project = False
                       
        screen.paper(50,100,11)
        screen.text(150,300,[f"'{proyectoSinExt}'",
                    "1 - Corrige un dato","2 - Añade un dato","3 - Elimina dato/proyecto",
                    "4 - Gráficas","5 - Consultar datos"])
        screen.updateScreen()
        
        destino = screen.pushAndCome(options = 6)
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
        screen.paper(50,100,8)
        screen.text(150,300,[f"Corrige:\n{proyectoSinExt}",
                        "1 - Datos base","2 - Datos proceso","3 - Excepciones"])
        screen.updateScreen()
        
        destino = screen.pushAndCome(options = 4)
        if destino == "1":      menuProyectoCorrigeBase(proyecto,proyectoSinExt)
        elif destino == "2":    menuProyectoCorrigeProceso(proyecto,proyectoSinExt)
        elif destino == "3":    menuProyectoCorrigeExcepciones(proyecto,proyectoSinExt)
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return

def menuProyectoCorrigeBase(proyecto,proyectoSinExt):           
    
    carpeta = "Database/{}".format(proyecto)                                
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
                      f"Euros Página: {listadoExtra[12]}", f"% Revis: {listadoExtra[13]}",
                      f"Notas: {listadoExtra[14]}"]
        
    mensajeConPausa("Introduce datos\nEn blanco mantiene valor\nESC para anular",
                    False,False)                                                        # Muestra mensaje quitando la pausa y sin borrar
    
    screen.paper(50,700,16,2)                                                           # Pinta el papel 
    posicion = 150                                                                      # Posición de inicio
    for i in datos_a_pintar:                                                            # Pinta los datos a modificar
        
        screen.textAlone(900,posicion,i)                                                # Pinta el dato
        posicion += 49                                                                   # Incrementa la posición
        
    datos_necesarios = [listadoExtra[6],listadoExtra[4]]                                # Recoge datos necesarios para la corrección
    codigos_de_error = [15,4,14,2,4,5,4,6,4,4,7,4,8,0]                                  # Da los codigos de posible error que debe seguir
    datos_a_recuperar_tupla = cuestionarioProyecto(codigos_de_error,datos_necesarios)   # Recoge los datos del cuestionario
    if "acción anulada" in datos_a_recuperar_tupla:                                     # Si se recibe esta cadena anulamos la acción
        return                                                                          # y salimos de la función
    datos_a_recuperar = list(datos_a_recuperar_tupla)
    listadoExtra = [listadoExtra[1],listadoExtra[2],listadoExtra[3],
                    listadoExtra[4],listadoExtra[6],listadoExtra[7],
                    listadoExtra[8],listadoExtra[5],listadoExtra[9],
                    listadoExtra[10],listadoExtra[11],listadoExtra[12],
                    listadoExtra[13],listadoExtra[14]]
    for i in range(len(datos_a_recuperar)-1):
    
        if datos_a_recuperar[i] == "":
    
            datos_a_recuperar[i] = listadoExtra[i]
    if datos_a_recuperar[13] != "":
        datos_a_recuperar[13] = listadoExtra[13] + "\n" + datos_a_recuperar[13]
    else:
        datos_a_recuperar[13] = listadoExtra[13]
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
    conexion,cursor = sql.creaAbreBd(carpeta)                    
    sql.Modificar(cursor,sentencia,parametros)                              
    sql.CierraBd(conexion)  

    if datos_a_recuperar[0] == "A": 
        os.rename("Database/"+proyecto,"Database/"+proyecto.split(".")[0]+".dba")
        try:
            os.remove("Database/"+proyecto.split(".")[0]+".dbi")
        except:
            pass
        try:
            os.remove("Database/"+proyecto.split(".")[0]+".dbc")
        except:
            pass
    elif datos_a_recuperar[0] == "I":
        os.rename("Database/"+proyecto,"Database/"+proyecto.split(".")[0]+".dbi")
        try:
            os.remove("Database/"+proyecto.split(".")[0]+".dba")
        except:
            pass
        try:
            os.remove("Database/"+proyecto.split(".")[0]+".dbc")
        except:
            pass
    elif datos_a_recuperar[0] == "C":
        os.rename("Database/"+proyecto,"Database/"+proyecto.split(".")[0]+".dbc")
        try:
            os.remove("Database/"+proyecto.split(".")[0]+".dba")
        except:
            pass
        try:
            os.remove("Database/"+proyecto.split(".")[0]+".dbi")
        except:
            pass
                                                                          
    mensajeConPausa("Cambio realizado con éxito")        
    
    return                                          

def menuProyectoCorrigeProceso(proyecto,proyectoSinExt):        
    
    in_function = True
    while in_function:
        
        id_seleccionado, tabla, carpeta, in_function = PintaListaCorrecta("Proceso",proyecto,proyectoSinExt,listaDatosTablaProceso)
        if in_function == False: 
            break
       
        conexion,cursor = sql.creaAbreBd(carpeta)                                                   
        
        fila, in_function = abreIdSeleccionado(tabla,id_seleccionado)
        if in_function == False: 
            break
                
        datos_a_pintar = [f"Modifica proceso de {proyectoSinExt} fila {id_seleccionado}","",
                        f"Fecha: {fila[1]}", f"Páginas: {fila[2]}",
                        f"Tipo (T)rad./correc (R)evisión) {fila[3]}:"]
        
        mensajeConPausa("Introduce datos\nEn blanco mantiene valor\nESC para anular",
                    False,False) 
        
        screen.paper(50,700,6,2)
        posicion = 150
        for i in datos_a_pintar:
            
            screen.textAlone(900,posicion,i)
            posicion += 49 
            
        screen.updateScreen()
        
        datos_a_recuperar_tupla = cuestionarioProcesos([14,4,12])
        if "acción anulada" in datos_a_recuperar_tupla:
            return
        datos_a_recuperar = list(datos_a_recuperar_tupla) 
        
        for i in range(len(datos_a_recuperar)):
            
            if datos_a_recuperar[i] == "":
                
                datos_a_recuperar[i] = fila[i+1]
        try:
            
            sentencia = "UPDATE Proceso SET Fecha = ?, Paginas = ?, Tipo = ? WHERE ID = ?"    
            parametros = (datos_a_recuperar[0],datos_a_recuperar[1],datos_a_recuperar[2],id_seleccionado)                      
            sql.Modificar(cursor,sentencia,parametros)                      
            sql.CierraBd(conexion)                                          
        
            listaDatosTablaProceso(proyecto,proyectoSinExt,[550,700,900,650],12,False)             
            mensajeConPausa("Modificación exitosa")      
               
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Error al modificar el proceso") 
               
        in_function = False
        
    return   
 
def menuProyectoCorrigeExcepciones(proyecto,proyectoSinExt):    
    
    in_function = True
    while in_function:
        
        id_seleccionado, tabla, carpeta, in_function = PintaListaCorrecta("Excepciones",proyecto,proyectoSinExt,listaTablaExcepciones)
        if in_function == False: break
        
        conexion,cursor = sql.creaAbreBd(carpeta)                                                   
        
        fila, in_function = abreIdSeleccionado(tabla,id_seleccionado)
        if in_function == False: 
            break
        
        datos_a_pintar = [f"Modifica excepción de {proyectoSinExt} fila {id_seleccionado}","",
                            f"Fecha: {fila[1]}"]
        
        mensajeConPausa("Introduce datos\nEn blanco mantiene valor\nESC para anular",
                    False,False) 
        screen.paper(50,700,6,2)
        posicion = 150
        for i in datos_a_pintar:
            
            screen.textAlone(900,posicion,i)
            posicion += 49 
            
        screen.updateScreen()
        fecha = cuestionarioExcepciones()
        if "acción anulada" in fecha:
            return
        datos_a_recuperar = [fecha]
        for i in range(len(datos_a_recuperar)):
            
            if datos_a_recuperar[i] == "":
                datos_a_recuperar[i] = fila[i+1]
        try:
            
            sentencia = """UPDATE Excepciones SET Fecha = ? WHERE ID = ?"""      
            parametros = (datos_a_recuperar[0],id_seleccionado)                      
            sql.Modificar(cursor,sentencia,parametros)                      
            sql.CierraBd(conexion)                                          
        
            listaTablaExcepciones(proyecto,proyectoSinExt,[550,700,900,650],12,False)               
            mensajeConPausa("Modificación exitosa")     
                
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Error al modificar la excepción")
        
        in_function = False
        
    return                         

def abreIdSeleccionado(tabla,id_seleccionado):
    
    try:
            
        fila = ""
            
        for fila_adecuada in tabla:      
                           
            if fila_adecuada[0] == int(id_seleccionado):  
                    
                fila = fila_adecuada                
                break 
                                              
        if fila == "": 
                   
            screen.SoundWrongAnswer()
            mensajeConPausa("ID inexistente")
            return fila,False
            
    except:
            
        screen.SoundWrongAnswer()
        mensajeConPausa("Error en la lectura del archivo")    
        return fila,False
    
    return fila,True        

def PintaListaCorrecta(nombre_carpeta,proyecto,proyectoSinExt,listaAMostrar):
    
    tabla = []
    carpeta = "Database/{}".format(proyecto)
    try:
        tabla = sql.SeleccionaTodasFilas(carpeta,nombre_carpeta)
        id_seleccionado = listaAMostrar(proyecto,proyectoSinExt,[50,700,900,150])
    except:
        screen.SoundWrongAnswer()
        mensajeConPausa("Lista vacía")
        return "",tabla, carpeta, False
    
    return id_seleccionado, tabla, carpeta, True 
  
def menuProyectoAnade(proyecto,proyectoSinExt):                 
    
    in_function = True
    while in_function:
        
        screen.paper(50,100,8)
        screen.text(150,300,[f"Añade un dato a\n'{proyectoSinExt}'",
                    "1 - Procesos","2 - Excepciones"])
        
        screen.updateScreen()
        
        destino = screen.pushAndCome(options = 3)
        if destino == "1":      menuProyectoAnadeProceso(proyecto,proyectoSinExt)
        elif destino == "2":    menuProyectoAnadeExcepcion(proyecto,proyectoSinExt)
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return

def menuProyectoAnadeProceso(proyecto,proyectoSinExt):          
    
    listaDatosTablaProceso(proyecto,proyectoSinExt,[550,700,900,650],7,True)             
    mensajeConPausa("ESC para anular",False,False)
    
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
            
            screen.paper(50,700,6,2)
            posicion = 150
            for i in datos_a_pintar:
                
                screen.textAlone(900,posicion,i)
                posicion += 49 
                
            screen.updateScreen()
            fecha,paginas,tipo = cuestionarioProcesos([1,4,12])
            if "acción anulada" in fecha:
                return
            mensajeConPausa("¿Datos correctos? (S/N)",False,False)
            stay = True
            while stay: 
                respuesta = screen.pushAndCome(options = 0)
                if respuesta.upper() == "S":
                    carpeta = "Database/{}".format(proyecto)
                    tabla = sql.SeleccionaTodasFilas(carpeta,"Excepciones")
                    for i in tabla:
                        if i[1] == fecha:
                            conexion,cursor = sql.creaAbreBd(carpeta)
                            sentencia = "DELETE FROM Excepciones WHERE Fecha = ?"
                            parametros = (fecha,)
                            sql.Modificar(cursor,sentencia,parametros)
                            sql.CierraBd(conexion)
                            break
                    tabla = sql.SeleccionaTodasFilas(carpeta,"Proceso")
                    debemos_grabar = True
                    for i in tabla:
                        if i[1] == fecha and i[3] == tipo:
                            conexion,cursor = sql.creaAbreBd(carpeta)
                            sentencia = "UPDATE Proceso SET Paginas = ? WHERE Fecha = ? AND Tipo = ?"
                            parametros = (str(int(paginas)+int(i[2])),fecha,tipo)
                            sql.Modificar(cursor,sentencia,parametros)
                            sql.CierraBd(conexion)
                            debemos_grabar = False
                            break               
                    in_answer = False
                    mensajeConPausa("Datos añadidos")
                    stay = False
                elif respuesta.upper() == "N":
                    mensajeConPausa("Repitamos")
                    stay = False
        if debemos_grabar == True:
            conexion,cursor = sql.creaAbreBd("Database/{}".format(proyecto))                   
            introducimos = 'INSERT INTO Proceso (Fecha,Paginas,Tipo) VALUES (:Fecha,:Paginas,:Tipo)'
            parametros = {'Fecha':fecha,'Paginas':paginas,'Tipo':tipo}
            sql.anadeFila(cursor,introducimos,parametros,conexion)
            sql.CierraBd(conexion)                                      
        
        listaDatosTablaProceso(proyecto,proyectoSinExt,[550,700,900,650],7,True)             
        
        mensajeConPausa("¿proceso? (S/N)",False,False)
        stay = True
        while stay:
            respuesta = screen.pushAndCome(options = 0)
            if respuesta.upper() == "N":
                in_function = False
                stay = False  
            elif respuesta.upper() == "S":
                stay = False         
    return                                          

def cuestionarioProcesos(errores):                                              # Activa el cuestionario para los procesos
    fecha,paginas,tipo = "","",""                                               # Inicializa las variables
    YTexto = [245,294,343]                                                      # Posiciones de los textos
    variablesPasar = ["","",""]                                                 # Inicializa las variables a pasar
    i=0                                                                         # Inicializa el contador
    while i<3:                                                                  # Bucle para recoger los datos
        data = screen.AnswerChain([1430,YTexto[i],500,40],errores[i])           # Recoge los datos
        anular = CotejaAnulacion(data)                                          # Comprueba si se anula
        if anular: return (data,)*3                                             # Si se anula, devuelve los datos
        variablesPasar[i] = data                                                # Si no se anula, guarda los datos
        i+=1                                                                    # Incrementa el contador
    fecha,paginas,tipo = variablesPasar                                         # Asigna los datos a las variables
    return fecha,paginas,tipo                                                   # Devuelve los datos

def menuProyectoAnadeExcepcion(proyecto,proyectoSinExt):
    
    listaTablaExcepciones(proyecto,proyectoSinExt,[550,700,900,650],7,True)               
    mensajeConPausa("ESC para anular",False,False)        
    
    conexion,cursor = sql.creaAbreBd("Database/{}".format(proyecto))                                                                   
    insercionDatos = f'''CREATE TABLE IF NOT EXISTS Excepciones(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Fecha TEXT)'''                                          
    cursor = sql.CreaUnaTabla(cursor,insercionDatos)
    datos_a_pintar = [f"Añade excepción a {proyectoSinExt}","","Fecha:"]
    
    in_function = True
    while in_function:
        
        in_answer = True
        while in_answer:
            
            screen.paper(50,700,6,2)
            posicion = 150
            for i in datos_a_pintar:
                
                screen.textAlone(900,posicion,i)
                posicion += 49 
                
            screen.updateScreen()
            fecha = cuestionarioExcepciones()
            if "acción anulada" in fecha:
                return
            stay = True
            while stay:
                mensajeConPausa("¿Datos correctos? (S/N)",False,False)
                respuesta = screen.pushAndCome(options = 0)
                if respuesta.upper() == "S":
                    
                    carpeta = "Database/{}".format(proyecto)
                    tabla = sql.SeleccionaTodasFilas(carpeta,"Excepciones")
                    problemas = False
                    for i in tabla:
                        if i[1] == fecha:
                            screen.SoundWrongAnswer()
                            mensajeConPausa("Ya existe una excepción\ncon esa fecha")
                            problemas = True
                            break
                    if problemas == False:
                        in_answer = False
                        stay = False
                elif respuesta.upper() == "N":
                    mensajeConPausa("Repitamos")
                    stay = False
        conexion,cursor = sql.creaAbreBd("Database/{}".format(proyecto))                   
        introducimos = 'INSERT INTO Excepciones (Fecha) VALUES (:Fecha)'
        parametros = {'Fecha':fecha}
        sql.anadeFila(cursor,introducimos,parametros,conexion)
        sql.CierraBd(conexion)                                      
        
        listaTablaExcepciones(proyecto,proyectoSinExt,[550,700,900,650],7,True)               
                
        mensajeConPausa("¿Otra excepción? (S/N)",False,False)
        stay = True
        while stay:
            respuesta = screen.pushAndCome(options = 0)
            if respuesta.upper() == "N":
                in_function = False  
                stay = False
                mensajeConPausa("Añadidas con éxito")
            elif respuesta.upper() == "S":
                mensajeConPausa("")
                stay = False     
    return                                             

def cuestionarioExcepciones():
    
    fecha = screen.AnswerChain([1150,244,500,40],13)    
    anular = CotejaAnulacion(fecha)
    return fecha

def menuProyectoTablas(proyecto,proyectoSinExt):                
    
    in_function = True
    while in_function:
        
        screen.paper(50,100,9)
        screen.text(150,300,[f" Consultar datos de\n{proyectoSinExt}",
                        "1 - Datos base","2 - Datos proceso","3 - Excepciones"])
        screen.updateScreen()
        
        destino = screen.pushAndCome(options = 4)
        if destino == "1":      menuProyectoTablasBase(proyecto,proyectoSinExt)
        elif destino == "2":    menuProyectoTablasProceso(proyecto,proyectoSinExt)
        elif destino == "3":    menuProyectoTablasExcepciones(proyecto,proyectoSinExt)
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return

def esperaPulsaTecla():
    mensajeConPausa("Pulsa una tecla",False,False)
    screen.updateScreen()
    screen.pushAndCome(options = 0)
    
def menuProyectoTablasBase(proyecto,proyectoSinExt):  
              
    listaDatosTablasBase(proyecto,proyectoSinExt)               
    esperaPulsaTecla()
    return

def listaDatosTablasBase(proyecto,proyectoSinExt):
    
    carpeta = "Database/{}".format(proyecto)                
    tabla = sql.SeleccionaTodasFilas(carpeta,"Datos")       
    screen.paper(50,700,13,2)
    datos_a_pintar = [proyectoSinExt,"","Estado:","Cliente:",
                      "Inicio Proyecto:","Fecha Entrega:","Unidad de cálculo:",
                      "Páginas de origen:","Tipo Trabajo:","Tabla Usar:",
                      "Caracteres Holandesa:","Coste de la Holandesa:","Palab. Origen Destino:",
                      "Euros Página:","% Correc:","Notas:"]
    posicion = 150
    for i in datos_a_pintar:
        
        screen.textAlone(900,posicion,i)
        posicion += 49 
    
    posicion = 150
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
        # Si "frase" es el valor que denota al cliente
        elif frase == 2:
                # Busca en la tabla de clientes el ID = frase
                carpeta = "Database/Clientes.db"
                tabla = sql.SeleccionaTodasFilas(carpeta,"Clientes")
                for a in tabla:
                        if a[0] == int(i):
                            
                            i = a[1]
                            break
            
        elif frase == 0:
            
            i = ""    
        screen.textAlone(1300,posicion,str(i))
        if frase == 0:
            
            posicion += 49 
            
        posicion += 49 
        frase += 1           
    return  

def menuProyectoTablasProceso(proyecto,proyectoSinExt): 
            
    listaDatosTablaProceso(proyecto,proyectoSinExt,[50,700,900,150])             
    return                    

def listaDatosTablaProceso(proyecto,proyectoSinExt,posiciones,alto = 12,vuelve = False):
            
    opcion = ""
    carpeta = "Database/{}".format(proyecto)                        
    in_function = True
    while in_function:
        try:
            
            tabla = sql.SeleccionaTodasFilas(carpeta,"Proceso")  
            tabla = sorted(tabla, key=lambda x: datetime.strptime(x[1], "%d/%m/%y"))
        except:
            
            mensajeConPausa(f"No hay procesos para\n{proyectoSinExt}")
            in_function = False
            break
        
        mensajeConPausa("Cursores rota lista\nOtra tecla salir",False,False)    
        in_rotative = True
        posicion = 0
        while in_rotative:
            posicionY = posiciones[3]+int((screen.height*100)/1440)
            screen.paper(posiciones[0],posiciones[1],alto,2)
            screen.textAlone(posiciones[2],posiciones[3],"Procesos de "+proyectoSinExt)        
            if vuelve == False or len(tabla) < alto+2:
                a_mostrar = tabla[posicion:posicion+alto+3]
            else:
                a_mostrar = tabla[len(tabla)-alto:len(tabla)]
            for i in a_mostrar:
                if i[3] == "T":
                    
                    b = "Traducción"
                    
                elif i[3] == "R":
                    
                    b = "Revisión"
                    
                else:
                    
                    b = "Corrección"
                screen.textAlone(posiciones[2],posicionY,f"{i[0]} - A {i[1]},  realicé")
                screen.textAlone(posiciones[2],posicionY,f"                                {i[2]} páginas de {b}")
                screen.updateScreen()    
                posicionY += 49
            
            time.sleep(0.1)
            if vuelve == False:
                opcion = screen.pushAndCome(suma=posicion,options = 16,pos = [858,180],interlin = 49,anchozona = 1200)
            else:
                opcion = ""
            if opcion == "98": 
                if posicion > 0:
                    posicion -= 1
            elif opcion == "99": 
                if posicion < len(tabla)-15:
                    posicion += 1
            else:
                in_rotative = False 
        in_function = False 
        
    return opcion
            
def menuProyectoTablasExcepciones(proyecto,proyectoSinExt):   
      
    listaTablaExcepciones(proyecto,proyectoSinExt,[50,700,900,150])               
    return

def listaTablaExcepciones(proyecto,proyectoSinExt,posiciones,alto = 12,vuelve = False):  
    
    carpeta = "Database/{}".format(proyecto)                            
    in_function = True
    while in_function:
        try:
            
            tabla = sql.SeleccionaTodasFilas(carpeta,"Excepciones") 
            tabla = sorted(tabla, key=lambda x: datetime.strptime(x[1], "%d/%m/%y"))    
            
        except:
            
            mensajeConPausa(f"No hay excepciones para\n{proyectoSinExt}")
            in_function = False
            break
        
        mensajeConPausa("Cursores rota lista\nOtra tecla salir",False,False)
        in_rotative = True
        posicion = 0
        while in_rotative:    
            posicionY = posiciones[3]+int((screen.height*100)/1440)
            screen.paper(posiciones[0],posiciones[1],alto,2)
            screen.textAlone(posiciones[2],posiciones[3],"Excepciones de "+proyectoSinExt)
            if vuelve == False or len(tabla) < alto+2:
                a_mostrar = tabla[posicion:posicion+alto+3]
            else:
                a_mostrar = tabla[len(tabla)-alto:len(tabla)]
                
            for i in a_mostrar:
                
                screen.textAlone(posiciones[2],posicionY,f"{i[0]} - El {i[1]} no se trabaja")
                screen.updateScreen()
                posicionY += 49
                
            time.sleep(0.1)
            if vuelve == False:
                opcion = screen.pushAndCome(suma=posicion,options = 16,pos = [858,131],interlin = 49,anchozona = 1200)
            else:
                opcion = ""
            if opcion == "98":
                if posicion > 0:
                    posicion -= 1
            elif opcion == "99":
                if posicion < len(tabla)-15:
                    posicion += 1
            else:
                in_rotative = False    
        in_function = False
    return opcion

def menuProyectoElimina(proyecto,proyectoSinExt):               
    
    in_function = True
    while in_function:
        
        screen.paper(50,100,9)
        screen.text(150,300,[f"Elimina\n{proyectoSinExt}",
                    "1 - Proyecto entero","2 - Proceso","3 - Excepción"])
        screen.updateScreen()
        
        destino = screen.pushAndCome(options = 4)
        
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
    
    stay = True
    while stay:
        mensajeConPausa(f"¿Eliminar el proyecto\n{proyectoSinExt}?\n(S/N)",False,False)
        respuesta = screen.pushAndCome(options = 0)
        if respuesta.upper() == "S":                                                                                                            
            os.remove("Database/{}".format(proyecto))                                                                                           
            screen.SoundKillData()
            mensajeConPausa("Proyecto eliminado")
            stay = False
            return  True                                                                                                                       
        elif respuesta.upper() == "N":
            mensajeConPausa("No se eliminó\nel proyecto")
            stay = False
            return  False                                                                                                        
            
def menuProyectoEliminaProceso(proyecto,proyectoSinExt):
            
    in_function = True
    while in_function:
        
        id_seleccionado, tabla, carpeta, in_function = PintaListaCorrecta("Proceso",proyecto,proyectoSinExt,listaDatosTablaProceso)    
        if in_function == False: 
            break
               
        mensajeConPausa(f"¿Eliminar proceso\n{id_seleccionado}?\n(S/N)",False,False)        
        stay = True
        while stay:
            respuesta = screen.pushAndCome(options = 0)
            if respuesta.upper() == "S":    
                stay = False                                                                                                        
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
                        listaDatosTablaProceso(proyecto,proyectoSinExt,[50,700,900,150],12,True)  
                        mensajeConPausa("Proceso eliminado")
                                
                    else:
                        
                        screen.SoundWrongAnswer()
                        mensajeConPausa("ID inexistente")
                        
                except:             
                                                                        
                        screen.SoundWrongAnswer()
                        mensajeConPausa("Error en el proceso\nde borrado")                                              
                
                in_function = False
            
            elif respuesta.upper() == "N":
                    
                    mensajeConPausa("No se eliminó\nel proceso")
                    in_function = False                                             
                    stay = False
        return
    
def menuProyectoEliminaExcepcion(proyecto,proyectoSinExt): 

    in_function = True
    while in_function:
        
        id_seleccionado, tabla, carpeta, in_function = PintaListaCorrecta("Excepciones",proyecto,proyectoSinExt,listaTablaExcepciones)         
        if in_function == False: 
            break
        
        mensajeConPausa(f"¿Eliminar excepción\n{id_seleccionado}?\n(S/N)",False,False)
        stay = True
        while stay:
            respuesta = screen.pushAndCome(options = 0)
            if respuesta.upper() == "S":  
                stay = False                                                                                                        
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
                        listaTablaExcepciones(proyecto,proyectoSinExt,[50,700,900,150],12,True)
                        mensajeConPausa("Excepción eliminada") 
                                    
                    else:
                        
                        screen.SoundWrongAnswer()
                        mensajeConPausa("ID inexistente")
                        
                except:     
                                                                                    
                    screen.SoundWrongAnswer()
                    mensajeConPausa("Error en el proceso\nde borrado")
                        
                in_function = False
            
            elif respuesta.upper() == "N":
                        
                mensajeConPausa("No se eliminó\nla excepción")
                in_function = False
                stay = False    
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
    esperaPulsaTecla()    
    return
    
def menuCreaProyecto():     
                                        
    hoy = datetime.now()
    hoy = hoy.strftime("%d/%m/%y")
    datos_a_pintar = ["Creando un proyecto","","Nombre:","Estado...","(A)ctiv (I)nactiv (C)lose:","Cliente:",
                      "Inicio Proyecto:"+hoy,"Fecha Entrega:","Páginas de origen:",
                      "(T)raduc. (C)orrec.","Tabla Usar:","Calc.: (P)alab.(C)aract.p(A)g.",
                      "Caracteres Holandesa:","Coste de la Holandesa:","Palab. (O)rigen (D)estino:",
                      "Euros Página:","% Correc:","Notas:"]    
    screen.paper(50,700,16,2)
    posicion = 150
    for i in datos_a_pintar:
        
        screen.textAlone(900,posicion,i)
        posicion += 49 
        
    screen.updateScreen()
    nombre = screen.AnswerChain([1600,250,600,40],9)
    if nombre == "acción anulada":
        screen.SoundKillData()
        mensajeConPausa("Acción anulada")
        return
    codigos_de_error = [3,4,1,2,4,5,4,6,4,4,7,4,8,0]
    datos_necesarios = ["",""]
    YTexto = [342,391,440,489,538,587,636,685,734,783,832,881,930,979]
    estado,cliente,inicio_proyecto,fecha_entrega,paginas_origen,tipo_trabajo,tabla_usar,unidad_calculo,caracteres_holandesa,coste_holandesa,palabra_origen_destino,euros_pagina,tanto_ciento_correc,notas = cuestionarioProyecto(codigos_de_error,datos_necesarios,YTexto)
    if estado == "acción anulada":                                                      # Si el estado es "Acción anulada"
        return                                                                          # Sale de la función
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
                                                                    
        nombre += ".dba"  
                         
    elif estado == "I":  
                                                                   
        nombre += ".dbi"        
                  
    elif estado == "C":    
        nombre += ".dbc"                                                         
    BdProyecto,cursor = sql.creaAbreBd(f"Database/{nombre}")    
                        
    cursor = sql.CreaUnaTabla(cursor,crea_tabla)                                        
    
    insertamos = f'''INSERT INTO Datos (Estado,Cliente,IncioProyecto,FechaEntrega,
                UnidadCalculo, PáginasOrigen, TipoTrabajo, TablaUsar,
                CaracteresHolandesa, EurosHolandesa, PalabraOrigenDestino,
                EurosPagina, TantoCientoCorrec, Notas) VALUES (
                    :estado,:cliente,:inicio,:entrega,:unidad,
                    :paginas,:tipo,:tabla,:caracteres,:euros,
                    :palabra,:eurospag,:tanto,:notas)'''                                    
    estos_datos = {'estado':estado, 'cliente':cliente, 'inicio':inicio_proyecto, 
              'entrega':fecha_entrega, 'unidad':unidad_calculo,
              'paginas':paginas_origen, 'tipo':tipo_trabajo, 'tabla':tabla_usar,
              'caracteres':caracteres_holandesa,'euros':coste_holandesa, 
              'palabra':palabra_origen_destino, 'eurospag':euros_pagina, 
              'tanto':tanto_ciento_correc, 'notas':notas}                                     
    sql.anadeFila(cursor, insertamos, estos_datos, BdProyecto)                                          
    sql.CierraBd(BdProyecto) 
    
    BdProyecto, cursor = sql.creaAbreBd(f"Database/{nombre}")                               # Abre la base de datos del proyecto
    crea_excepciones =  '''
                        CREATE TABLE IF NOT EXISTS Excepciones(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Fecha TEXT)
                        '''                                                                 # Crea la tabla de excepciones
    cursor = sql.CreaUnaTabla(cursor,crea_excepciones)                                      # Crea la tabla de excepciones
    sql.CierraBd(BdProyecto)                                                                # Cierra la base de datos del proyecto
    
    mensajeConPausa("Proyecto creado con éxito")                                            # Muestra un mensaje
                                                                                   
    return                                                                                  # Sale de la función

def CotejaAnulacion(estado):                                                            # Coteja si se ha pedido suspender la acción
    if estado == "acción anulada":                                                      # Si el estado es "acción anulada"
        screen.SoundKillData()                                                          # Activa el sonido de error
        mensajeConPausa("Acción anulada")                                               # Muestra un mensaje y sale de la función
        return True                                                                     # Devuelve True
    else:                                                                               # Si no
        return False                                                                    # Devuelve False
    
def cuestionarioProyecto(errores,datos_necesarios,YTexto = [293,342,391,440,489,538,587,636,685,734,783,832,881,930]):   
    tabla_usar,unidad_calculo,caracteres_holandesa,coste_holandesa,palabra_origen_destino,euros_pagina, = "","","","","",""
    error = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    estado,cliente,inicio_proyecto,fecha_entrega,paginas_origen,tipo_trabajo,tanto_ciento_correc,notas = "","","","","","","",""
    variablesPasar = ["","","","","","","","","","","","","",""]    
    i = 0
    cliente_dado = ""
    tabla_dada = ""
    while i < 14:
        if i == 1:
            data = cliente_dado
            screen.textAlone(1600,YTexto[i],data)
        elif i == 6:
            data = tabla_dada
            screen.textAlone(1600,YTexto[i],data)
        else:    
            data = screen.AnswerChain([1600,YTexto[i],600,40],errores[error[i]])
        anular = CotejaAnulacion(data) 
        if anular: return (data,)*14
        variablesPasar[i] = data
        if i == 0:
            listado,carpeta = preparaListaClientes()
            cliente_dado = listaClientes(listado)
        if i == 5:
            if variablesPasar[5] == "C" or variablesPasar[5] == "" and datos_necesarios[0] == "C":
                listado,carpeta = preparaListaTablas()
                tabla_dada= listaTablas(listado)
            elif variablesPasar[5] == "T" or variablesPasar[5] == "" and datos_necesarios[0] == "T":
                i += 1
        if i == 7:
            if variablesPasar[7] == "P" or variablesPasar[7] == "" and datos_necesarios[1] == "P":
                i += 2
            elif variablesPasar[7] != "C" or variablesPasar[7] == "" and datos_necesarios[1] != "C":
                i += 3
        i += 1
    estado,cliente,inicio_proyecto,fecha_entrega,paginas_origen,tipo_trabajo,tabla_usar,unidad_calculo,caracteres_holandesa,coste_holandesa,palabra_origen_destino,euros_pagina,tanto_ciento_correc,notas=variablesPasar
    return estado,cliente,inicio_proyecto,fecha_entrega,paginas_origen,tipo_trabajo,tabla_usar,unidad_calculo,caracteres_holandesa,coste_holandesa,palabra_origen_destino,euros_pagina,tanto_ciento_correc,notas                                      
    
def menuClientes():                
        
    in_function = True
    while in_function:
        
        screen.paper(50,100,10)
        screen.text(150,300,[f"Menú de Clientes",
                    "1 - Crear Cliente","2 - Consultar Cliente","3 - Modificar Cliente","4 - Eliminar Cliente"])
        screen.updateScreen()
        
        destino = screen.pushAndCome(options = 5)
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

    datos_a_pintar = ["Creando un cliente","", "Nombre:","",
                      "Teléfono:", "Dirección:", "Ciudad:",
                      "C.P.:", "País:", "NIF:",
                      "Contacto:", "Teléfono contacto:",
                      "Email contacto:", "Pago previo:"]
    in_function = True
    while in_function:   
         
        in_answer = True
        while in_answer:  
              
            screen.paper(50,700,14,2)    
            posicion = 150
            for i in datos_a_pintar:
                
                screen.textAlone(900,posicion,i)
                posicion += 49 
                
            screen.updateScreen()
            nombre = screen.AnswerChain([1300,248,600,40],9)
            if nombre == "acción anulada":
                screen.SoundKillData()            
                mensajeConPausa("Acción anulada")
                return
            telefono,direccion,ciudad,cp, pais,nif,contacto,telefono_contacto,email_contacto,pago_previo = cuestionarioClientes()
            if "acción anulada" in telefono:
                return
            mensajeConPausa("¿Datos correctos?\n(S/N)",False,False)
            stay = True
            while stay:
                
                respuesta = screen.pushAndCome(options = 0)
                if respuesta.upper() == "S":
                    
                    in_answer = False
                    stay = False
                elif respuesta.upper() == "N":
                        
                        stay = False
                        mensajeConPausa("Repitamos")
            
        conexion,cursor = sql.creaAbreBd(carpeta)                           
        insertamos = f'INSERT INTO Clientes (Nombre, Telefono, Direccion, Ciudad, cp, pais, Nif, Contacto, TelContacto, EmailContacto,PagoPrevio ) VALUES (:nombre, :telefono, :direccion, :ciudad, :cp, :pais, :nif, :contacto, :telContacto, :emailContacto, :pagoPrevio)'   
        esos_datos = {'nombre' : nombre, 'telefono' : telefono, 
                'direccion' : direccion, 'ciudad' : ciudad, 'cp' : cp, 'pais' : pais,
                'nif' : nif, 'contacto' : contacto, 'telContacto' : telefono_contacto, 
                'emailContacto' : email_contacto, 'pagoPrevio' : pago_previo}                                
        sql.anadeFila(cursor,insertamos,esos_datos,conexion)                                            
        sql.CierraBd(conexion) 
                                                                                     
        listado,carpeta = preparaListaClientes()                                            
        listaClientes(listado)  
        
        mensajeConPausa("¿Añadir otro?\n(S/N)",False,False)
        
        stay = True
        while stay:
            respuesta = screen.pushAndCome(options = 0)
            if respuesta.upper() == "N":
                
                in_function = False
                stay = False
            elif respuesta.upper() == "S":
                stay = False
    return                                              
 
def cuestionarioClientes(): 
    datos = ["","","","","","","","","",""]
    error = [4,0,0,4,0,0,0,4,0,4]    
    for i in range(10):
        
        datos[i] = screen.AnswerChain([1600,346+(49*i),600,40],error[i])                                          
        anular = CotejaAnulacion(datos[i])
        if anular: 
            return (datos[i],)*10
    
    telefono,direccion,ciudad,cp,pais,nif,contacto,telefono_contacto,email_contacto,pago_previo = datos

    return telefono,direccion,ciudad,cp,pais,nif,contacto,telefono_contacto,email_contacto,pago_previo
    
def consultaCliente():    
                                         
    in_function = True
    while in_function:
        
        listado,carpeta = preparaListaClientes()                                            
        opcion = listaClientes(listado)                                            

        opciones = ["0"]
        for i in range (1,len(listado)+1):
            
            opciones.append(str(i))
        
        in_answer = True                                                                           
        while in_answer:                                                                           
        
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
        
        screen.paper(50,700,valor,2)
        screen.textAlone(900,150,"Datos del cliente "+cliente)
        titulos = ["ID","Nombre:","Teléfono:","Dirección:","Ciudad:","C.P.:","País:","NIF:","Contacto:","Teléfono contacto:","Email contacto:","Pago previo:"]
        posicion = 250
        orden = 0
        for i in filas[0]:
        
            screen.textAlone(900,posicion,f"{titulos[orden]}")
            screen.textAlone(1200,posicion,f"       {i}")
            orden += 1
            posicion += 49 
        
        in_function = False
        
        mensajeConPausa("Pulsa una tecla",False,False)
        screen.pushAndCome(options = 0)
        
    return                                                                  

def preparaListaClientes():
    
    carpeta =           "Database/Clientes.db"                                                        
    conexion,cursor =   sql.creaAbreBd(carpeta)
    insercionDatos =    '''CREATE TABLE IF NOT EXISTS Clientes(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nombre TEXT, 
                        Telefono TEXT, 
                        Direccion TEXT, 
                        Ciudad TEXT, 
                        cp TEXT, 
                        pais TEXT,
                        Nif TEXT,
                        Contacto TEXT,
                        TelContacto TEXT,
                        EmailContacto TEXT,
                        PagoPrevio TEXT)                        
                        '''   
    cursor =            sql.CreaUnaTabla(cursor,insercionDatos)           
                                                        
    consulta =          "SELECT Nombre FROM Clientes;"                                               
    listado =           sql.listados(cursor,consulta)                                          
    sql.CierraBd(conexion) 
                                                                     
    return listado,carpeta
    
def listaClientes(listado):     
    
    mensajeConPausa("Elige opción\nCursores mueve lista",
                    False,False)
    
    posicion = 0
    numeracion = 1
    in_function = True
    while in_function:                                      
        
        screen.paper(51,100,12,False)     
        todos_clientes = ["Todos los clientes"]
        lista_corta = listado[posicion:posicion+7]
        for i in lista_corta:
            if len(i)>20:
                a = i[:20]
                a = a + "..."
            else:
                a = i
                
            todos_clientes.append(f"{numeracion} - {a}")
            numeracion += 1
            
        screen.text(150,300,todos_clientes,False)
        screen.updateScreen()
        time.sleep(0.1)
        pulsacion = screen.pushAndCome(suma=posicion,options = 7)
        if pulsacion == "98":
            if posicion > 0:                                                # Si la tecla es "98" y la posición es mayor que 0
                posicion -= 1                                               # Disminuye la posición
            numeracion = posicion+1
        elif pulsacion == "99":
            if posicion < len(listado) - 7:                                 # Si da cursor abajo y la posición es menor que la cantidad de tablas menos 7
                posicion += 1                                               # Aumenta la posición
            numeracion = posicion+1
        else:                                                               # Si no
            in_function = False                                             # Sale del bucle
    return pulsacion
                          
def modificaCliente():                                          

    in_function = True
    while in_function:
        
        carpeta = "Database/Clientes.db"
        try:
            
            lista_clientes, carpeta = preparaListaClientes()
            id_seleccionado = listaClientes(lista_clientes)
            
        except:
            
            mensajeConPausa("No hay clientes")                                  
            in_function = False
            break
                          
        if id_seleccionado == "0":
        
            in_function = False
            break
        
        cliente = lista_clientes[int(id_seleccionado)-1]
        fila = sql.MuestraDato(carpeta,cliente,"Clientes")
        
        datos_a_pintar = [f"Modificando un cliente","",f"Nombre: {fila[0][1]}","",f"Teléfono: {fila[0][2]}",
                          f"Dirección: {fila[0][3]}",f"Ciudad: {fila[0][4]}", f"C.P.: {fila[0][5]}",
                          f"País: {fila[0][6]}",
                          f"NIF: {fila[0][7]}",f"Contacto: {fila[0][8]}",
                          f"Teléfono contacto: {fila[0][9]}",f"Email contacto: {fila[0][10]}",
                          f"Pago previo: {fila[0][11]}"]
        
        mensajeConPausa("Introduce datos\nEn blanco mantiene valor\nESC para anular",
                    False,False) 
        
        screen.paper(50,700,13,2)
        posicion = 150
        for i in datos_a_pintar:
            
            screen.textAlone(900,posicion,i)
            posicion += 49 
            
        screen.updateScreen()
        
        
        cliente_tupla = cuestionarioClientes()
        if "acción anulada" in cliente_tupla:
                
                return
            
        cliente = list(cliente_tupla)
        
        for i in range(len(cliente)):
            
            if cliente[i] == "":
                cliente[i] = fila[0][i+2]
        try:
            
            sentencia = """UPDATE Clientes SET Telefono = ?, Direccion = ?, Ciudad = ?, cp = ?, pais = ?,
                        Nif = ?, Contacto = ?, TelContacto = ?, EmailContacto = ?,
                        PagoPrevio = ? WHERE ID = ?"""
            parametros = (cliente[0], cliente[1], cliente[2],
                        cliente[3], cliente[4], cliente[5],
                        cliente[6], cliente[7], cliente[8],
                        cliente[9],  
                        id_seleccionado)
            conexion,cursor = sql.creaAbreBd(carpeta)
            sql.Modificar(cursor,sentencia,parametros)
            conexion.commit()
            sql.CierraBd(conexion)

            mensajeConPausa("Cliente modificado")
            
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
            id_seleccionado = listaClientes(nombres)   
                                                     
        except:
            
            mensajeConPausa("No hay clientes")
            in_function = False                                         
        
        if id_seleccionado == "0":
                
                in_function = False
                break
            
        mensajeConPausa(f"¿Eliminar el cliente\n{id_seleccionado}?\n(S/N)",False,False)                                         
        stay = True
        while stay:
            respuesta = screen.pushAndCome(options = 0)
        
            if respuesta.upper() == "S":
                    
                tabla = sql.SeleccionaTodasFilas(carpeta,"Clientes")                                 
                
                stay = False                                                                                                        
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
                        mensajeConPausa("Cliente eliminado")                                        
                    else:
                        
                        screen.SoundWrongAnswer()
                        mensajeConPausa("ID inexistente")
                        
                except:  
                                                                                
                        screen.SoundWrongAnswer()
                        mensajeConPausa("Error en el proceso\nde borrado")
                        
            elif respuesta.upper() == "N":
                mensajeConPausa("No se eliminó\nel cliente")
                stay = False
        in_function = False
            
    return                                                                  

def menuTablasCorreccion():                                                             # Menú de tablas de corrección    
    
    in_function = True                                                              
    while in_function:
        
        screen.paper(50,100,10)
        screen.text(150,300,[f"Menú de Tablas\npara Corrección",
                    "1 - Crear tabla","2 - Consultar tabla",
                    "3 - Modificar tabla","4 - Eliminar tabla"])
        screen.updateScreen()
    
        destino = screen.pushAndCome(options = 5)
        if destino == "1":      creaTabla()
        elif destino == "2":    consultaTabla()
        elif destino == "3":    modificaTabla()
        elif destino == "4":    eliminaTabla()
        elif destino == "0":    in_function = False
        else:                   screen.SoundWrongAnswer()
        
    return                             

def creaTabla():                                                                        # Creamos una tabla de corrección nueva  
                                                  
    listado,carpeta = preparaListaTablas()

    nombre = ""
    datos_a_pintar = ["Creando una tabla","","Nombre:","","",
                    "De:","A:","Euros/palabra:"]
    conexion,cursor = sql.creaAbreBd("Database/Tablas.db")            

    in_function = True
    while in_function:
        
        in_answer = True                                                                           
        while in_answer:                                                                           

            screen.paper(50,700,7,2)
            posicion = 125
            for i in datos_a_pintar:
                
                screen.textAlone(900,posicion,i)
                posicion += 49 
                
            screen.updateScreen()
            if nombre == "":
                
                nombre = screen.AnswerChain([1200,224,600,40],9)
                if nombre == "acción anulada":
                    screen.SoundKillData()
                    mensajeConPausa("Acción anulada")
                    return
                nombre = nombre.replace(" ","_")
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
                
                screen.textAlone(1200,224,nombre)
                
            sql.CierraBd(conexion)                                                                  
            de,a,euros = cuestionarioTabla()
            
            mensajeConPausa("¿correcto? (S/N)",False,False)
            
            stay = True
            while stay:
                
                respuesta = screen.pushAndCome(options = 0)
                if respuesta.upper() == "S":
                    
                    in_answer = False
                    stay = False
                elif respuesta.upper() == "N":
                        
                        stay = False
                        mensajeConPausa("Repitamos")
        conexion,cursor = sql.creaAbreBd(carpeta)                           
        insertamos = f'INSERT INTO {nombre} (De, A, Euros) VALUES (:de, :a, :euros)'   
        esos_datos = {'de' : de,'a' : a, 'euros' : euros}                                
        sql.anadeFila(cursor,insertamos,esos_datos,conexion)                                            
        sql.CierraBd(conexion)  
                                                                                    
        lineas = sql.SeleccionaTodasFilas(carpeta,nombre)
        listaLaTabla(lineas,nombre,[600,700,900,700])        

        mensajeConPausa("¿Otra linea? (S/N)",False,False)
        
        stay = True
        while stay:
            respuesta = screen.pushAndCome(options = 0)
            if respuesta.upper() == "N":
                mensajeConPausa("Tabla creada")
                in_function = False
                stay = False
            elif respuesta.upper() == "S":
                stay = False
  
    return                 

def cuestionarioTabla():
    
    de,a,euros = "","",""
    de = screen.AnswerChain([1300,372,600,40],4)
    if de == "acción anulada":
        return de,a,euros
    a = screen.AnswerChain([1300,421,600,40],4)
    if a == "acción anulada":
        return de,a,euros
    euros = screen.AnswerChain([1300,470,600,40],11)
    
    return de,a,euros
   
def consultaTabla():         
                                       
    in_function = True
    while in_function:
        
        tabla = ""
        listado,carpeta = preparaListaTablas()                                            
        opcion = listaTablas(listado)                                            
        
        opciones = ["0"]                                                                        
        for i in range(1,len(listado)+1):                                                       
            opciones.append(str(i))                                                             
        cotejo = True                                                                           
        while cotejo:                                                                           
            if opcion in opciones:                                                              
                cotejo = False                                                                  
        opcion = int(opcion)                                                                    
        if opcion == 0: 
            in_function = False
            break                                                 
        
        try:
            
            tabla = listado[int(opcion)-1]                                                   
        
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("Tabla inexistente")
            in_function = False
            break
        
        filas = sql.SeleccionaTodasFilas(carpeta,tabla)                                 
        fila = listaLaTabla(filas,tabla,[50,700,900,150])                                            
        in_function = False
        
    return tabla,fila                                                         

def listaLaTabla(filas,tabla,posiciones,lineas = 10):                               # Muestra la tabla
    primero = 0                                                                     # Inicializa la variable
    valor = 5 if len(filas) < 3 else (lineas if 
                                      len(filas) > lineas else 
                                      len(filas) + 2)                               # Calcula la cantidad de papel a poner en pantalla
        
    in_function = True                                                              # Inicializa la variable
    while in_function:                                                              # Bucle de la función
        screen.paper(posiciones[0],posiciones[1],valor,2)                           # Pone el papel en pantalla                
        screen.textAlone(posiciones[2],posiciones[3],"Tabla "+tabla)                # Pone el título de la tabla
        posicion = posiciones[3]+100                                                # Pone la posición de la primera línea
        PocasFilas,recorrido = [],0                                                 # Inicializa las variables      
        for i in filas:                                                             # Recorre las filas de la tabla
            if recorrido < primero or recorrido > primero + lineas:                 # Si la fila no está entre las que se deben mostrar
                pass                                                                # No hace nada
            else:                                                                   # Si está entre las que se deben mostrar
                PocasFilas.append(i)                                                # La añade a la lista de las que se deben mostrar
            recorrido += 1                                                          # Aumenta el recorrido
        for i in PocasFilas:                                                        # Recorre las filas que se deben mostrar
            
            screen.textAlone(posiciones[2],posicion,
                             f"{i[0]} - De {i[1]:} a")                              # Muestra la fila
            screen.textAlone(posiciones[2],posicion,
                            f"                     {i[2]:} palabras,")              # Muestra la fila
            screen.textAlone(posiciones[2],posicion,
                f"                                         {i[3]:>5} €/palabra")    # Muestra la fila
            posicion += 49                                                           # Aumenta la posición  
        
        mensajeConPausa("Selecciona una fila\nCursores mueve lista",
                        False,False)                                        # Muestra un mensaje
        move = screen.pushAndCome(suma=primero,options = len(filas))                                         # Espera una tecla
        if move == "98":                                                    # Si la tecla es "98"
            if primero > 0:                                                 # Si la primera fila es mayor que 0
                primero -= 1                                                # Disminuye la primera fila
        elif move == "99":                                                  # Si la tecla es "99"
            if primero < len(filas) - lineas - 1:                           # Si la primera fila es menor que la cantidad de filas menos las que se deben mostrar
                primero += 1                                                # Aumenta la primera fila
        else:                                                               # Si no
            in_function = False                                             # Sale del bucle
    return move                                                             # Sale de la función

def preparaListaTablas():
    
    carpeta =           "Database/Tablas.db"                                                          
    conexion,cursor =   sql.creaAbreBd(carpeta)                                                   
    consulta =          "SELECT name FROM sqlite_master WHERE type='table';"                         
    listado =           sql.listados(cursor,consulta)                                          
    sql.CierraBd(conexion)
    
    return listado,carpeta

def listaTablas(listado):                                                   # Muestra las tablas
    
    mensajeConPausa("Elige opción\nCursores mueve lista",
                    False,False)                                            # Muestra un mensaje
    posicion = 0                                                            # Inicializa la variable
    numeracion = 1                                                          # Inicializa la variable
    in_function = True                                                      # Inicializa la variable
    while in_function:                                                      # Bucle de la función
        
        screen.paper(51,100,12,False)                                             # Pone el papel en pantalla
        todas_tablas = ["Listado de tablas"]                            
        lista_corta = listado[posicion:posicion+7]                          # Coge las primeras 7 tablas
        for i in lista_corta:
            
            if len(i)>20:
                a = i[:20]
                a = a + "..."
            else:
                a = i
            todas_tablas.append(str(numeracion) +" - " + a)
            numeracion += 1
            
        screen.text(150,300,todas_tablas,False)
        screen.updateScreen()     
        time.sleep(0.1)
        pulsacion = screen.pushAndCome(suma=posicion,options = 7)                                    # Espera una tecla
        if pulsacion == "98":
            if posicion > 0:                                                # Si la tecla es "98" y la posición es mayor que 0
                posicion -= 1                                               # Disminuye la posición
            numeracion = posicion+1
        elif pulsacion == "99":
            if posicion < len(listado) - 7:                                 # Si da cursor abajo y la posición es menor que la cantidad de tablas menos 7
                posicion += 1                                               # Aumenta la posición
            numeracion = posicion+1
        else:                                                               # Si no
            in_function = False                                             # Sale del bucle
    return pulsacion
              
def modificaTabla():                                            
    
    in_function = True
    while in_function:
        
        tabla_a_modificar,id_seleccionado = consultaTabla()   
        if tabla_a_modificar == "":
            
            in_function = False
            break
                
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
            
            datos_a_pintar = [f"Modificando una tabla",
                              f"Nombre: {tabla}",
                              "",f"De: {fila[1]}",
                              f"A: {fila[2]}",
                              f"Euros/palabra: {fila[3]}"]
        
        except:
            
            screen.SoundWrongAnswer()
            mensajeConPausa("ID inexistente")
            in_function = False
            break
        
        mensajeConPausa("Introduce datos\nEn blanco mantiene valor\nESC para anular",
                    False,False) 
        
        screen.paper(50,700,6,2)
        posicion = 224
        for i in datos_a_pintar:
            
            screen.textAlone(900,posicion,i)
            posicion += 49 
            
        screen.updateScreen()
        
        tabla_tupla = cuestionarioTabla()
        if "acción anulada" in tabla_tupla:
            screen.SoundKillData()
            mensajeConPausa("Acción anulada")        
            in_function = False
            break
        
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
                
            mensajeConPausa("Tabla modificada")
            
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
            id_seleccionado = listaTablas(nombres)   
                                                     
        except:
            
            mensajeConPausa("No hay tablas")
            in_function = False                                         
            
        if id_seleccionado == "0":
                    
                    in_function = False
                    break
                
        mensajeConPausa(f"¿Eliminar la tabla {id_seleccionado}?\n(S/N)",False,False)                                         
        stay = True
        while stay:
            respuesta = screen.pushAndCome(options = 0)

            if respuesta.upper() == "S":   
                stay = False                                                                                                        
                try:  
                                                                                    
                    conexion,cursor = sql.creaAbreBd(carpeta)                                                   
                    consulta = "SELECT name FROM sqlite_master WHERE type='table';"                         
                    listado = sql.listados(cursor,consulta)                                          
                    tabla = listado[int(id_seleccionado)-1]                                                   
                    sql.eliminaTabla(cursor,tabla)                                                  
                    sql.CierraBd(conexion)                    
                    screen.SoundKillData()
                    mensajeConPausa("Tabla eliminada con éxito")
                                                            
                except:
                    
                    screen.SoundWrongAnswer()
                    mensajeConPausa("Error al borrar la tabla")
            elif respuesta.upper() == "N":
                mensajeConPausa("No se eliminó\nla tabla")
                
                stay = False    
        in_function = False                                                                  

    return                                           

def exit(): 
                                                        
    screen.animaLogo(1)
    screen.fadeOut()                                                
    sys.exit()                              

def mensajeConPausa(mensaje,pause = True,borra = True):
    
    screen.paper(1000,100,3,0)
    screen.textAlone(300,1100,mensaje)
    screen.updateScreen()
    if pause:
        time.sleep(2)
    if borra:
        screen.paper(1000,100,3,0)
        screen.updateScreen()
                                
if __name__ == "__main__":                                      
    
    screen.run()
    comprobarExistenciaCarpeta()
    screen.fadeIn()
    screen.animaLogo()    
    menuInicial()    