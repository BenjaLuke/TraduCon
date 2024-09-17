import  pygame                                                              # Importamos pygame para dar imagen de juego
import  sys     
from    datetime import datetime                                            # Importamos datetime para manejar fechas
import  time                                                                # Importamos time para manejar el tiempo
import  random                                                              # Importamos random para manejar números aleatorios

import  errores                                                             # Importamos errores
import  mates                                                               # Importamos mates

class Game:                                                                 # Clase que controla toda la interfaz gráfica del juego
    
    def __init__(self):                                                     # Inicia la clase game
        
        pygame.init()                                                       # Inicia pygame

        screen_info = pygame.display.Info()                                 # Información de la pantalla
        self.width, self.height = screen_info.current_w, screen_info.current_h # Ancho y alto de la pantalla
        self.height = int((self.width*1440)/3440)                           # Alto de la pantalla
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)   # Pantalla  
        pygame.display.set_caption("Tradu con")                             # Título de la ventana

        pygame.mixer.init()                                                 # Inicia el mixer
         
        
        self.background_image = pygame.image.load("EXTRAS/escritorio.jpg")  # Imagen de fondo  
        self.background_image = pygame.transform.scale(
            self.background_image, (self.width, self.height))               # Escalamos la imagen de fondo

        
        self.paper_sup = pygame.image.load("EXTRAS/hoja_superior_1.png")    # Imagen de la parte superior de la hoja
        self.paper_mid = pygame.image.load("EXTRAS/hoja_media_1.png")       # Imagen de la parte media de la hoja
        self.paper_down = pygame.image.load("EXTRAS/hoja_inferior_1.png")   # Imagen de la parte inferior de la hoja

        self.paper_sup_3 = pygame.image.load("EXTRAS/hoja_superior_2.png")  # Imagen de la parte superior de la hoja hancha
        self.paper_mid_3 = pygame.image.load("EXTRAS/hoja_media_2.png")     # Imagen de la parte media de la hoja hancha
        self.paper_down_3 = pygame.image.load("EXTRAS/hoja_inferior_2.png") # Imagen de la parte inferior de la hoja hancha
        
        self.paper_sup = pygame.transform.scale(
            self.paper_sup, 
            (int((self.width*664)/3440), 
             int((self.height*116)/1440)))                                  # Escalamos la imagen de la parte superior de la hoja
        self.paper_mid = pygame.transform.scale(
            self.paper_mid, 
            (int((self.width*664)/3440), 
             int((self.height*71)/1440)))                                   # Escalamos la imagen de la parte media de la hoja
        self.paper_down = pygame.transform.scale(
            self.paper_down, 
            (int((self.width*664)/3440),
             int((self.height*145)/1440)))                                  # Escalamos la imagen de la parte inferior de la hoja
        
        self.paper_sup_super_big = pygame.transform.scale(
            self.paper_sup_3,
            (int((self.width*2500)/3440),
             int((self.height*116)/1440)))                                  # Escalamos la imagen de la parte superior de la hoja hancha
        self.paper_mid_super_big = pygame.transform.scale(
            self.paper_mid_3, 
            (int((self.width*2500)/3440), 
             int((self.height*71)/1440)))                                   # Escalamos la imagen de la parte media de la hoja hancha
        self.paper_down_super_big = pygame.transform.scale(
            self.paper_down_3, 
            (int((self.width*2500)/3440),
             int((self.height*145)/1440)))                                  # Escalamos la imagen de la parte inferior de la hoja hancha
        
        self.paper_graph = pygame.image.load("EXTRAS/hoja_de_grafica.png")  # Imagen de la hoja de gráfica
        self.paper_graph = pygame.transform.scale(
            self.paper_graph, 
            (int((self.width*1331)/3440),
             int((self.height*1400)/1440)))                                 # Escalamos la imagen de la hoja de gráfica
        
        self.logo = pygame.image.load("EXTRAS/logo.png")                    # Imagen del logo
        self.logo = pygame.transform.scale(
            self.logo, 
            (int((self.width*177)/3440), 
             int((self.height*185)/1440)))                                  # Escalamos la imagen del logo
        self.logoBig = pygame.image.load(
            "EXTRAS/logo_traducon.png").convert_alpha()                     # Imagen del logo grande
        self.logoBig = pygame.transform.scale(
            self.logoBig, 
            (int((self.width*669)/3440), 
             int((self.height*609)/1440)))                                  # Escalamos la imagen del logo grande

        self.font_1 = pygame.font.Font("EXTRAS/JMH Typewriter-Bold.ttf",
                                       int((self.width*30)/3440))           # Fuente 1
        self.font_2 = pygame.font.Font("EXTRAS/JMH Typewriter-Bold.ttf", 
                                       int((self.width*40)/3440))           # Fuente 2
        
        
        self.pass_page = pygame.mixer.Sound("EXTRAS/pasa hoja.wav")         # Sonido de pasar página
        self.trash = pygame.mixer.Sound("EXTRAS/arruga hoja.wav")           # Sonido de arrugar hoja
        self.wrong = pygame.mixer.Sound("EXTRAS/wrong.wav")                 # Sonido de error
        self.typewriter = [pygame.mixer.Sound("EXTRAS/typewriter_1.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_2.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_3.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_4.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_5.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_6.wav")]   # Sonidos de la máquina de escribir
        self.typewriter_shift = pygame.mixer.Sound(
            "EXTRAS/typewriter_shift.wav")                                  # Sonido de la máquina de escribir con shift
        self.typewriter_carro = pygame.mixer.Sound(
            "EXTRAS/typewriter_carro.wav")                                  # Sonido de la máquina de escribir con carro
        self.typewriter_borrar = pygame.mixer.Sound(
            "EXTRAS/typewriter_backspace.wav")                              # Sonido de la máquina de escribir al borrar
        self.typewriter_espacio = pygame.mixer.Sound(
            "EXTRAS/typewriter_space.wav")                                  # Sonido de la máquina de escribir al poner espacio
        self.music_open = pygame.mixer.Sound("EXTRAS/Audio_enter.mp3")      # Música de entrada cargada como audio
        self.music_close = pygame.mixer.Sound("EXTRAS/Audio_exit.mp3")      # Música de salida cargada como audio
         
        self.logo_origen = self.width+int((self.width*100)/3440)            # Posición origen del logo
        self.logo_destino = int((self.width/15)*14)                         # Posición destino del logo
                
    def run(self):                                                          # Pone en pantalla la clase game

        self.updateScreen()                                                 # Actualizamos la pantalla
        return                                                              # Salimos de la función
        
    def updateScreen(self):                                                 # Actualiza los datos en patalla de la clase
        
        pygame.display.flip()                                               # Actualiza la pantalla
        
    def paper(self,altura,anchura,trozos,que_es = 0):                       # Pone en pantalla una hoja de papel
        
        self.pass_page.play()
        
        originAlt = altura
        altura = int((self.width*altura)/3440)
        anchura = int((self.height*anchura)/1440)

        for i in range(trozos):
            if i == 0:
                if que_es == 0:
                    if originAlt == 50:
                        self.screen.blit(self.background_image,(0,0))
                        self.screen.blit(self.logo, self.image_rect)
                    self.screen.blit(self.paper_sup, (anchura, altura))
                elif que_es == 2:
                    self.screen.blit(self.paper_sup_super_big, (anchura, altura))                    
                else:
                    self.screen.blit(self.paper_sup_big, (anchura, altura))
                altura += int((self.height*45)/1440)
            elif i == trozos-1:
                if que_es == 0:
                    self.screen.blit(self.paper_down, (anchura, altura))
                elif que_es == 2:
                    self.screen.blit(self.paper_down_super_big, (anchura, altura))
                else:
                    self.screen.blit(self.paper_down_big, (anchura, altura))
            else:
                if que_es == 0:
                    self.screen.blit(self.paper_mid, (anchura, altura))
                elif que_es == 2:
                    self.screen.blit(self.paper_mid_super_big, (anchura, altura))
                else:
                    self.screen.blit(self.paper_mid_big, (anchura, altura))
            altura += int((self.height*71)/1440)

    def paperGraph(self,proyectoSinExt,Datos,Procesos,Excepciones):         
        
        self.screen.blit(self.paper_graph, (int((self.width*700)/3440), (int((self.height*50)/1440)) ) ) # Pone en pantalla la hoja de gráfica
        
        
        listaDeDatos = self.calculaDatosGrafica(proyectoSinExt,Datos,Procesos,Excepciones)
        
        
        for i in listaDeDatos: 
            texto_escribe = i[3].render(i[0], True, (0,50,150))    
            ancho = int((self.width*i[1])/3440)
            alto = int((self.height*i[2])/1440)
            text_rect = texto_escribe.get_rect(left=ancho, centery = alto)
            self.screen.blit(texto_escribe, text_rect)
                                
        return
    
    def calculaDatosGrafica(self,proyectoSinExt,Datos,Procesos,Excepciones):
    
        
        listaDeDatos = []
        TipoDeConteo = Datos[0][7]
        if TipoDeConteo == "C": TipoDeConteo = "Corrección"
        else:                   TipoDeConteo = "Traducción"
        
        NumeroPaginasOriginales = Datos[0][6]
        NumeroPaginasTraducidas = 0
        for Proceso in Procesos:
            if Proceso[3] == "T": 
                NumeroPaginasTraducidas += int(Proceso[2])
        NumeroPaginasRevisadas   = 0
        for Proceso in Procesos:
            if Proceso[3] == "R": 
                NumeroPaginasRevisadas += int(Proceso[2])
        try:    
            NumeroPaginasPendientes     = int(NumeroPaginasOriginales) - int(NumeroPaginasTraducidas)       
        except:
            NumeroPaginasPendientes = "---"
        try:    
            NumeroPaginasPorRevisar     = int(NumeroPaginasOriginales) - int(NumeroPaginasRevisadas)
        except:
            NumeroPaginasPorRevisar = "---"
        
        FechaInicioProyecto         = Datos[0][3]
        
        try:
            FechaInicioProyectoSuma     = datetime.strptime(FechaInicioProyecto, "%d/%m/%y")
        except:
            FechaInicioProyectoSuma = "---"
        FechaActual                 = datetime.now()
        try:
            FechaActual                 = FechaActual.strftime("%d/%m/%y")
        except:
            FechaActual = "---"
        try:
            FechaActualSuma             = datetime.strptime(FechaActual, "%d/%m/%y")
        except:
            FechaActualSuma = "---"
        FechaEntrega                = Datos[0][4]   
        try:
            FechaEntregaSuma            = datetime.strptime(FechaEntrega, "%d/%m/%y")
        except:
            FechaEntregaSuma = "---"
        try:
            DiasRestantes               = FechaEntregaSuma - FechaActualSuma
        except:
            DiasRestantes = "---"
            
        try:
            DiasRestantes               = (DiasRestantes.days)+1
        except:
            DiasRestantes = "---"
        try:
            DiasParaProyecto            = FechaEntregaSuma - FechaInicioProyectoSuma  
        except:
            DiasParaProyecto = "---"
        try:
            DiasParaProyecto            = DiasParaProyecto.days
        except:
            DiasParaProyecto = "---"
        try:
            DiasYaPasados               = FechaActualSuma - FechaInicioProyectoSuma
        except:
            DiasYaPasados = "---"
        try:
            DiasYaPasados               = DiasYaPasados.days      
        except:
            DiasYaPasados = "---"
        try:    
            DiasExentos                 = len(Excepciones)
            for Excepcion in Excepciones:
                FechaExcepcion = Excepcion[1]
                try:
                    FechaExcepcionSuma = datetime.strptime(FechaExcepcion, "%d/%m/%y")
                except:
                    FechaExcepcionSuma = "---"
                if FechaExcepcionSuma < FechaActualSuma:
                    DiasExentos -= 1
        except:
            DiasExentos = "---"
        try:
            DiasPosibles                = FechaEntregaSuma - FechaInicioProyectoSuma
        except:
            DiasPosibles = "---"
        try:
            DiasPosibles                = (DiasPosibles.days)+1
        except:
            DiasPosibles = "---"
        try:
            DiasReales                  = DiasRestantes - DiasExentos
        except:
            DiasReales = "---"
        TantoCientoParaRevision     = Datos[0][13]
        try:
            TantoCientoParaTraduccion   = 100 - TantoCientoParaRevision
        except:
            TantoCientoParaTraduccion = "---"
        DiasYaDedicadosRevision     = 0
        try:
            DiasProyectoEnMarcha        = FechaActualSuma - FechaInicioProyectoSuma
        except:
            DiasProyectoEnMarcha = "---"
        try:
            DiasProyectoEnMarcha        = DiasProyectoEnMarcha.days
        except:
            DiasProyectoEnMarcha = "---"
        for Proceso in Procesos:
            if Proceso[3] == "R": 
                DiasYaDedicadosRevision += 1
        DiasYaDedicadosTraduccion   = 0 
        lista = []
        for Proceso in Procesos:
            if Proceso[3] == "T" and Proceso[1] not in lista: 
                DiasYaDedicadosTraduccion += 1
                lista.append(Proceso[1])
        
                
        DiasDedicadosAmbos          = 0                             
        ListasComparadas        = []                                
        ListasCoincidentes      = [] 
        
        if DiasYaDedicadosRevision != 0 and DiasYaDedicadosTraduccion != 0:                               
            for i,Proceso in enumerate(Procesos):                       
                if Proceso in ListasComparadas:                         
                    continue                                            
                else:                                                   
                    ValorAComparar = Proceso[1]                         
                    for j in range(i+1,len(Procesos)):                  
                        if Procesos[j][1] == ValorAComparar:            
                            ListasCoincidentes.append([i,j])            
                            ListasComparadas.append(Procesos[j])        
        DiasDedicadosAmbos = len(ListasCoincidentes)                
        
        try:
            DiasADedicarTrad = DiasReales * TantoCientoParaTraduccion / 100
        except:
            DiasADedicarTrad = "---"
        try:
            DiasADedicarTrad = mates.redondea(DiasADedicarTrad,2)
        except:
            DiasADedicarTrad = "---"
        try:
            DiasADedicarRev  = DiasReales * TantoCientoParaRevision / 100
        except:
            DiasADedicarRev = "---"
        try:
            DiasADedicarRev  = mates.redondea(DiasADedicarRev,2)
        except:
            DiasADedicarRev = "---"
            
        try:
            PorcientoRevisionReal       = DiasYaDedicadosRevision * 100 / DiasPosibles
        except:
            PorcientoRevisionReal = "---"
        try:
            PorcientoTraduccionReal     = DiasYaDedicadosTraduccion * 100 / DiasPosibles
        except:
            PorcientoTraduccionReal = "---"
        try:
            PorcientoMixtoReal          = DiasDedicadosAmbos * 100 / DiasPosibles
        except: 
            PorcientoMixtoReal = "---"
        PaginasRevisadas            = 0
        for Proceso in Procesos:
            if Proceso[3] == "R": 
                PaginasRevisadas += int(Proceso[2])        
        try:
            PaginasTraduceAlDiaDesdeHoy = NumeroPaginasPendientes/DiasReales
        except: 
            PaginasTraduceAlDiaDesdeHoy = "---"
        try:
            PaginasTraduceAlDiaDesdeHoy  = mates.redondea(PaginasTraduceAlDiaDesdeHoy,0)
        except:
            PaginasTraduceAlDiaDesdeHoy = "---"
        try:
            PaginasRevisaAlDiaDesdeHoy = NumeroPaginasPorRevisar/DiasReales
        except:
            PaginasRevisaAlDiaDesdeHoy = "---"
        try:
            PaginasRevisaAlDiaDesdeHoy = mates.redondea(PaginasRevisaAlDiaDesdeHoy,0)
        except:
            PaginasRevisaAlDiaDesdeHoy = "---"         
        try:
            PaginasTraduceAlDiaDesdeMan = NumeroPaginasPendientes/(DiasReales-1)
        except:
            PaginasTraduceAlDiaDesdeMan = "---"
        try:    
            PaginasTraduceAlDiaDesdeMan = mates.redondea(PaginasTraduceAlDiaDesdeMan,0)
        except:
            PaginasTraduceAlDiaDesdeMan = "---"
        try:
            PaginasRevisaAlDiaDesdeMan = NumeroPaginasPorRevisar/(DiasReales-1)
        except:
            PaginasRevisaAlDiaDesdeMan = "---"  
        try:
            PaginasRevisaAlDiaDesdeMan = mates.redondea(PaginasRevisaAlDiaDesdeMan,0)
        except:
            PaginasRevisaAlDiaDesdeMan = "---"  
        tituloLargo = ("Proyecto de "+TipoDeConteo+" "+proyectoSinExt)
        todasLasFechas = "Inicio: "+FechaInicioProyecto+" - Hoy: "+ FechaActual +" - Entrega: "+FechaEntrega
        
        
        listaDeDatos.append([tituloLargo,900,250,self.font_1])
        listaDeDatos.append([todasLasFechas,900,325,self.font_1])
        listaDeDatos.append(["Páginas",900,400,self.font_1])
        listaDeDatos.append(["Totales:",900,475,self.font_1])
        listaDeDatos.append([str(NumeroPaginasOriginales),1110,475,self.font_1])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Traducidas: ",900,575,self.font_1])
        else:
            listaDeDatos.append(["Corregidas: ",900,575,self.font_1])
        listaDeDatos.append([str(NumeroPaginasTraducidas),1110,575,self.font_1])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Por trad.: ",900,625,self.font_1])
        else:
            listaDeDatos.append(["Por corr.: ",900,625,self.font_1])
        listaDeDatos.append([str(NumeroPaginasPendientes),1110,625,self.font_1])
        listaDeDatos.append(["Revisadas: ",900,725,self.font_1])
        listaDeDatos.append([str(NumeroPaginasRevisadas),1110,725,self.font_1])
        listaDeDatos.append(["Por revisar: ",900,775,self.font_1])
        listaDeDatos.append([str(NumeroPaginasPorRevisar),1110,775,self.font_1])
        
        listaDeDatos.append(["Días",1200,400,self.font_1])
        listaDeDatos.append(["Totales: ",1200,475,self.font_1])
        listaDeDatos.append([str(DiasPosibles),1512,475,self.font_1])
        listaDeDatos.append(["Pasados: ",1200,525,self.font_1])
        listaDeDatos.append([str(DiasYaPasados),1512,525,self.font_1])
        listaDeDatos.append(["Restantes: ",1200,575,self.font_1])
        listaDeDatos.append([str(DiasRestantes),1512,575,self.font_1])
        listaDeDatos.append(["Exentos: ",1200,625,self.font_1])
        listaDeDatos.append([str(DiasExentos),1512,625,self.font_1])
        listaDeDatos.append(["Reales: ",1200,675,self.font_1])
        listaDeDatos.append([str(DiasReales),1512,675,self.font_1])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Dedic. T. desde hoy:",1200,725,self.font_1])
        else:
            listaDeDatos.append(["Dedic. C. desde hoy:",1200,725,self.font_1])
        listaDeDatos.append([str(DiasADedicarTrad),1512,725,self.font_1])
        listaDeDatos.append(["Dedic. R. desde hoy:",1200,775,self.font_1])
        listaDeDatos.append([str(DiasADedicarRev),1512,775,self.font_1])
        listaDeDatos.append(["Tradujiste:",1200,825,self.font_1])
        listaDeDatos.append([str(DiasYaDedicadosTraduccion),1512,825,self.font_1])
        listaDeDatos.append(["Revisaste:",1200,875,self.font_1])
        listaDeDatos.append([str(DiasYaDedicadosRevision),1512,875,self.font_1])
        listaDeDatos.append(["Ambos:",1200,925,self.font_1])
        listaDeDatos.append([str(DiasDedicadosAmbos),1512,925,self.font_1])
        
        listaDeDatos.append(["Tanto % sobre días",1605,400,self.font_1])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Trad. Objetivo:",1605,475,self.font_1])
        else:
            listaDeDatos.append(["Corr. Objetivo:",1605,475,self.font_1])
        try:
            listaDeDatos.append([str(int(TantoCientoParaTraduccion))+"%",1902,475,self.font_1])
        except:
            listaDeDatos.append(["---",1902,475,self.font_1])
            
        listaDeDatos.append(["Rev. Objetivo:",1605,525,self.font_1])
        try:
            listaDeDatos.append([str(int(TantoCientoParaRevision))+"%",1902,525,self.font_1])
        except:
            listaDeDatos.append(["---",1902,525,self.font_1])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Traduc. Real:",1605,625,self.font_1])
        else:
            listaDeDatos.append(["Correg. Real:",1605,625,self.font_1])
        try:
            listaDeDatos.append([str(int(PorcientoTraduccionReal))+"%",1902,625,self.font_1])
        except:
            listaDeDatos.append(["---",902,625,self.font_1])
        listaDeDatos.append(["Revisión Real:",1605,675,self.font_1])
        try:
            listaDeDatos.append([str(int(PorcientoRevisionReal))+"%",1902,675,self.font_1])
        except:
            listaDeDatos.append(["---",1902,675,self.font_1])
        listaDeDatos.append(["Mixto Real:",1605,725,self.font_1])
        try:
            listaDeDatos.append([str(int(PorcientoMixtoReal))+"%",1902,725,self.font_1])
        except:
            listaDeDatos.append(["---",1902,725,self.font_1])
            
        listaDeDatos.append([" Pág. trad/rev a partir de hoy: "+str(PaginasTraduceAlDiaDesdeHoy)+" / "+str(PaginasRevisaAlDiaDesdeHoy),900,1065,self.font_2])
        listaDeDatos.append([" Pág, trad/rev a partir mañana: "+str(PaginasTraduceAlDiaDesdeMan)+" / "+str(PaginasRevisaAlDiaDesdeMan) ,900,1115,self.font_2])
        
        return listaDeDatos
        
    def text(self,altura,anchura,textos,aviso = True):                      # Pone en pantalla los textos enviados
        
        altura = int((self.width*altura)/3440)
        anchura = int((self.height*anchura)/1440)
        
        textos.insert(1,"0 - Salir")
        textos.insert(1,"")
        
        
        if aviso:
            textos.append("")
            textos.append("Elige una opción")
                
        num_bucle = 0
        
        for i in textos:
            
            textitos = i.split("\n")
            
            if num_bucle == 0:
                circunstancia = altura
                for a in textitos:
                    texto_escribe = self.font_1.render(a, True, (255, 0, 0))
                    text_rect = texto_escribe.get_rect(left= anchura, centery = altura)
                    self.screen.blit(texto_escribe, text_rect)
                    altura += int((self.height*40+21)/1440)
                altura = circunstancia+int(self.height*71/1440)
            else:
                if num_bucle == 2:
                    texto_escribe = self.font_1.render(i, True, (0, 200, 100))
                elif num_bucle == len(textos)-1 and aviso:
                    texto_escribe = self.font_1.render(i, True, (0, 0, 255))
                else:
                    texto_escribe = self.font_1.render(i, True, (0, 0, 0))
                text_rect = texto_escribe.get_rect(left= anchura, centery = altura)
                self.screen.blit(texto_escribe, text_rect)
                altura += int((self.height*71)/1440)
            num_bucle += 1
    
    def textAlone(self,anchura,altura,texto): 
        anchura = int((self.width*anchura)/3440)
        altura = int((self.height*altura)/1440)
        
        textos = texto.split("\n")
        for texto in textos:
            texto_escribe = self.font_1.render(texto, True, (0, 0, 200))
            text_rect = texto_escribe.get_rect(left= anchura, centery = altura)
            altura += 30
            self.screen.blit(texto_escribe, text_rect)
        
    def animaLogo(self,direccion = 0):                                      # Anima la entrada del logo

        if direccion == 0:                                                  # Si la dirección es 0
            self.start_point = (self.logo_origen, 
                                int((self.height*150)/1440))                # Punto de inicio
            self.end_point = (self.logo_destino, 
                              int((self.height*150)/1440))                  # Punto de destino
            self.direction = (self.end_point[0] - self.start_point[0], 
                        self.end_point[1] - self.start_point[1])            # Dirección
            self.length = pygame.math.Vector2(self.direction).length()      # Longitud
            self.direction_normalized = (self.direction[0] / 
                                    self.length, self.direction[1] / 
                                    self.length)                            # Dirección normalizada
            self.image_rect = self.logo.get_rect(center=self.start_point)   # Rectángulo de la imagen
            self.speed = 40                                                 # Velocidad
        else:                                                               # Si la dirección es 1
            self.start_point, self.end_point = self.end_point, self.start_point # Intercambiamos los puntos
        cotejo = True                                                       # Bucle de cotejo
        while cotejo:                                                       # Mientras cotejo sea True
            
            if direccion == 0:
                self.image_rect.x += (self.direction_normalized[0] * 
                                      self.speed)                           # Movemos la imagen en x
                self.image_rect.y += (self.direction_normalized[1] * 
                                      self.speed)                           # Movemos la imagen en y
            else:
                self.image_rect.x -= (self.direction_normalized[0] * 
                                      self.speed)                           # Movemos la imagen en x
                self.image_rect.y -= (self.direction_normalized[1] * 
                                      self.speed)                           # Movemos la imagen en y
            self.screen.blit(self.background_image, (0, 0))                 # Ponemos la imagen de fondo
            self.screen.blit(self.logo, self.image_rect)                    # Ponemos la imagen del logo
            self.updateScreen()                                             # Actualizamos la pantalla
            time.sleep(0.03)                                                # Esperamos 0.03 segundos
            if ((direccion == 0 and 
                self.image_rect.x <= self.logo_destino) or
                (direccion == 1 and
                 self.image_rect.x >= self.end_point[0])):                  # Si la imagen llega al destino
                cotejo = False                                              # Cotejo es False
            if direccion == 0:                                              # Si la dirección es 0
                self.speed -= 5                                             # La velocidad disminuye en 5
            else:                                                           # Si no
                self.speed += 5                                             # La velocidad aumenta en 5
            if self.speed <= 1:                                             # Si la velocidad es menor o igual a 1
                self.speed = 5                                              # La velocidad es 5
        return                                                              # Salimos de la función
    
    def fadeIn(self):                                                       # Anima la entrada del logo
        
        self.music_open.play()                                              # Reproducimos la música de entrada
        rectangulo = pygame.Rect(0,0, self.width,self.height)               # Rectángulo
        pygame.display.flip()                                               # Actualizamos la pantalla
        time.sleep(0.1)                                                     # Esperamos 0.5 segundos
        for i in range (0,255,4):                                           # Para i en el rango de 0 a 255 de 4 en 4
            
            pygame.draw.rect(self.screen, (0,0,0), rectangulo)              # Dibujamos   
            self.logoBig.set_alpha(i)                                       # Aumentamos la transparencia del logo
            self.screen.blit(self.logoBig,((self.width/2)-
                                           int((self.width*335))/3440,
                            (self.height/2)-int((self.height*305)/1440)))   # Ponemos el logo
            self.updateScreen()                                             # Actualizamos la pantalla
            time.sleep(0.003)                                               # Esperamos 0.003 segundos
            
        for i in range (255,-1,-8):                                         # Para i en el rango de 255 a 0 de 8 en 8
            
            self.screen.blit(self.background_image, (0, 0))                 # Ponemos la imagen de fondo
            temp_surface = pygame.Surface((self.width, self.height),
                                          pygame.SRCALPHA)                  # Creamos una superficie transparente
            temp_surface.set_alpha(i)                                       # Aumentamos la transparencia de la superficie
            pygame.draw.rect(temp_surface, (0,0,0), rectangulo)             # Dibujamos un rectángulo en la superficie transparente
            self.screen.blit(temp_surface, (0,0))                           # Ponemos la superficie en la pantalla
            self.screen.blit(self.logoBig,((self.width/2)-
                                           int((self.width*335))/3440,
                            (self.height/2)-int((self.height*305)/1440)))   # Ponemos el logo
            self.updateScreen()                                             # Actualizamos la pantalla
            time.sleep(0.003)                                               # Esperamos 0.003 segundos
        for i in range (255,-1,-4):                                         # Para i en el rango de 255 a 0 de 4 en 4
            self.screen.blit(self.background_image, (0, 0))                 # Ponemos la imagen de fondo
            self.logoBig.set_alpha(i)                                       # Aumentamos la transparencia del logo
            self.screen.blit(self.logoBig,((self.width/2)-
                                           int((self.width*335))/3440,
                            (self.height/2)-int((self.height*305)/1440)))   # Ponemos el logo
            self.updateScreen()                                             # Actualizamos la pantalla
            time.sleep(0.003)                                               # Esperamos 0.003 segundos
                
    def fadeOut(self):                                                      # Anima la salida del logo
        
        rectangulo = pygame.Rect(0, 0, self.width, self.height)             # Rectángulo

        self.music_close.play()                                             # Reproducimos la música de salida
        for i in range(0, 256, 4):                                          # Para i en el rango de 0 a 256 de 4 en 4
            self.screen.blit(self.background_image, (0, 0))                 # Dibujar fondo
            self.logoBig.set_alpha(i)                                       # Aumentar transparencia del logo
            self.screen.blit(self.logoBig, ((self.width / 2) - 
                                            int((self.width * 335)) / 3440, 
                                            (self.height / 2) - 
                                            int((self.height * 305) /
                                                1440)))                     # Dibujar logo
            self.updateScreen()                                             # Actualizar pantalla
            time.sleep(0.003)                                               # Esperar 0.003 segundos

        for i in range(0, 256, 8):                                          # Para i en el rango de 0 a 256 de 4 en 4
            
            self.screen.blit(self.background_image, (0, 0))                 # Dibujar fondo
            temp_surface = pygame.Surface((self.width, self.height), 
                                          pygame.SRCALPHA)                  # Crear superficie transparente
            temp_surface.set_alpha(i)                                       # Aumentar transparencia del rectángulo
            pygame.draw.rect(temp_surface, (0, 0, 0), rectangulo)           # Dibujar rectángulo en la superficie transparente
            self.screen.blit(temp_surface, (0, 0))                          # Dibujar la superficie en la pantalla
            self.logoBig.set_alpha(255)                                     # Aumentar transparencia del logo
            self.screen.blit(self.logoBig, ((self.width / 2) - 
                                            int((self.width * 335)) / 3440, 
                                            (self.height / 2) - 
                                            int((self.height * 305) / 
                                                1440)))                     # Dibujar logo
            self.updateScreen()                                             # Actualizar pantalla
            time.sleep(0.003)                                               # Esperar 0.003 segundos

        for i in range(255, -1, -4):                                        # Para i en el rango de 255 a 0 de 4 en 4
            pygame.draw.rect(self.screen, (0,0,0), rectangulo)              # Dibujar rectángulo   
            self.logoBig.set_alpha(i)                                       # Aumentar transparencia del logo
            self.screen.blit(self.logoBig, ((self.width / 2) - 
                                            int((self.width * 335)) / 3440, 
                                            (self.height / 2) - 
                                            int((self.height * 305) / 
                                                1440)))                     # Dibujar logo
            self.updateScreen()                                             # Actualizar pantalla
            time.sleep(0.003)                                               # Esperar 0.003 segundos
        
        while pygame.mixer.get_busy():                                      # Mientras el mezclador esté ocupado
            time.sleep(0.1)                                                 # Esperar 0.1 segundos
            
    def pushAndCome(self, pos = [300,275], 
                    suma = 0,options = 10,interlin = 71,anchozona = 420):   # Recoge la información de teclas pulsadas (máximo 2)
        
        pos = [(self.width * pos[0]) / 3440, (self.height * pos[1]) / 1440] # Posición
        sumando = int(self.height)*interlin/1440                            # Sumando
        envio = ""                                                          # Variable de envío
        cotejo = True                                                       # Bucle de cotejo
        while cotejo:                                                       # Mientras cotejo sea True
            keys = pygame.key.get_pressed()                                 # Teclas pulsadas
            if keys[pygame.K_UP]:                                           # Si pulsamos la tecla de flecha arriba
                envio = "98"                                                # Enviamos 98
                cotejo = False                                              # Salimos del bucle
                break                                                       # Salimos del bucle
            elif keys[pygame.K_DOWN]:                                       # Si pulsamos la tecla de flecha abajo
                envio = "99"                                                # Enviamos 99
                cotejo = False                                              # Salimos del bucle
                break                                                       # Salimos del bucle
            for event in pygame.event.get():                                # Para cada evento en los eventos
                if event.type == pygame.KEYDOWN:                            # Si el evento es de pulsación de tecla
                    tecla_pulsada = event.key                               # Tecla pulsada
                    try:                                                    # Intentamos
                        if 1073741913 <= int(tecla_pulsada) <= 1073741921:  # Si la tecla pulsada es un número
                            envio += chr(int(tecla_pulsada)-1073741864)     # Añadir la tecla pulsada a envío
                        elif int(tecla_pulsada) == 1073741922:              # Si la tecla pulsada es un número
                            envio = "0"                                     # Enviamos 0
                        else:                                               # Si no
                            envio += chr(tecla_pulsada)                     # Añadir la tecla pulsada a envío
                        aleatorio = random.randint(0,5)                     # Aleatorio
                        self.typewriter[aleatorio].play()                   # Sonido de máquina de escribir
                        if envio == "0":                                    # Si envío es 0
                            cotejo = False                                  # Salimos del bucle
                            break                                           # Salimos del bucle
                        else:                                               # Si no
                            for i in range(200):                            # Para i en el rango de 200
                                time.sleep(0.0001)                          # Esperamos 0.0001 segundos
                                keys = pygame.key.get_pressed()             # Teclas pulsadas
                                for event in pygame.event.get():            # Para cada evento en los eventos
                                    if event.type == pygame.KEYDOWN:        # Si el evento es de pulsación de tecla
                                        tecla_pulsada = event.key           # Tecla pulsada
                                        try:                                # Intentamos
                                            if (1073741913 <= 
                                                int(tecla_pulsada) <= 
                                                1073741921):                # Si la tecla pulsada es un número
                                                envio += chr(
                                                    int(tecla_pulsada)-
                                                    1073741864)             # Añadir la tecla pulsada a envío
                                            elif (int(tecla_pulsada) == 
                                                  1073741922):              # Si la tecla pulsada es un número
                                                envio = "0"                 # Enviamos 0
                                            else:                           # Si no
                                                envio += chr(tecla_pulsada) # Añadir la tecla pulsada a envío
                                            aleatorio = random.randint(0,5) # Aleatorio
                                            self.typewriter[aleatorio].play() # Sonido de máquina de escribir                                        
                                            break                           # Salimos del bucle
                                        except:                             # Si hay un error
                                            pass                            # Pasamos'''
                        cotejo = False                                      # Salimos del bucle
                        break                                               # Salimos del bucle
                    except:                                                 # Si hay un error
                        pass                                                # Pasamos
                if event.type == pygame.MOUSEBUTTONDOWN:                    # Si pulsamos el ratón
                    if (event.button == 1 and options == 0 or
                        event.button == 3):                                 # Si pulsamos el botón izquierdo y no hay opciones
                        envio = "0"                                         # Enviamos 0
                        cotejo = False                                      # Salimos del bucle
                        break                                               # Salimos del bucle
                    if event.button == 1 or event.button == 2:              # Si pulsamos el botón izquierdo
                        loc = pygame.mouse.get_pos()                        # Posición del ratón
                        for i in range(options):                            # Para i en el rango de opciones
                            if (pos[0] <=
                                loc[0] <=
                                pos[0]+int((self.width*anchozona)/3440) and
                                pos[1]+(sumando*i) <= 
                                loc[1] <= 
                                pos[1]+(sumando*i)+int(self.width*15/1440)):# Si el ratón está en la zona de la opción
                                if str(i) == "0":                           # Si la opción es 0 
                                    envio = "0"                             # Enviamos 0
                                else:                                       # Si no
                                    envio = str (i+suma)                    # Enviamos i+suma
                                cotejo = False                              # Salimos del bucle
                                break                                       # Salimos del bucle
                    elif event.button == 4:                                 # Si pulsamos la rueda del ratón
                        envio = "98"                                        # Enviamos 98
                        cotejo = False                                      # Salimos del bucle
                        break                                               # Salimos del bucle
                    elif event.button == 5:                                 # Si pulsamos la rueda del ratón
                        envio = "99"                                        # Enviamos 99
                        cotejo = False                                      # Salimos del bucle
                        break                                               # Salimos del bucle
        return envio                                                        # Devolvemos envío
    
    def AnswerChain(self,posicion, error = 0):
                
        posiciones = [int((self.width * posicion[0]) / 3440), 
                    int((self.height * posicion[1]) / 1440),
                    int((self.width * posicion[2]) / 3440), 
                    int((self.height * posicion[3]) / 1440)]
        posicion = posiciones
        ancho_texto = 0
        cotejo = True
        chain = ">"
        shift_pressed = False
        caps_pressed = False

        anula = False                                                                       # Variable que controla si se anula la acción
        
        while cotejo:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    tecla_pulsada = event.unicode
                    if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):    
                        shift_pressed = True
                    elif event.key == pygame.K_CAPSLOCK:
                        caps_pressed = not caps_pressed

                    elif event.key == pygame.K_ESCAPE:                                      # Si pulsamos return
                        anula = True                                                        # Anulamos la acción
                        cotejo = False                                                      # Salimos del bucle
                        
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:                                      # Si pulsamos return
                        if len(chain) > 0:                                                  # Si la cadena tiene algo
                            if chain[-1] == ">":                                            # Si el último caracter es un ">"
                                chain = chain[:-1]                                          # Quitamos el último caracter
                            elif chain == ">":                                              # Si la cadena es solo un ">"
                                chain = ""                                                  # La cadena se queda vacía
                        termina, chain = errores.Errores(chain, error)                      # Llamamos a la función errores.Errores
                        if termina:                                                         # Si termina es True
                            self.typewriter_carro.play()                                    # Sonido de carro de máquina de escribir
                            cotejo = False                                                  # Salimos del bucle
                        else:                                                               # Si no
                            self.wrong.play()                                               # Sonido de error
                    elif event.key == pygame.K_BACKSPACE:
                        if len(chain) > 0:
                            self.typewriter_borrar.play()
                            if chain[-1] == ">":
                                chain = chain[:-2]
                            else:
                                chain = chain[:-1]
                    else:
                        try:
                            if shift_pressed:
                                tecla_pulsada = tecla_pulsada.upper()
                                                            
                            if tecla_pulsada == " " and ancho_texto < posicion[2]-int((self.width*20)/3440):
                                self.typewriter_espacio.play()
                            else:
                                if ancho_texto < posicion[2]-int((self.width*20)/3440):
                                    aleatorio = random.randint(0, 5)
                                    self.typewriter[aleatorio].play()
                                else:
                                    self.wrong.play()
                            if len(chain) > 1:
                                if chain[-1] == ">":
                                    chain = chain[:-1]
                                elif chain == ">":
                                    chain = ""
                                    
                            if tecla_pulsada != "`" and ancho_texto < posicion[2]-int((self.width*20)/3440):
                                chain += tecla_pulsada

                            if chain[0] == ">":
                                chain = chain[1:]
                        except:
                            pass
                            
                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                        shift_pressed = False

            if len(chain) > 1:
                if chain[-1] == ">":
                    chain = chain[:-1]
                else:
                    chain += ">"
            elif chain == ">":
                chain = ""
            elif chain == "":
                chain = ">"

            chain = str(chain)
            
            # Bucle que recorre todas las posiciones desde posicion[1] hasta posicion[1]+posicion[3]
            for i in range(posicion[1], posicion[1]+posicion[3]):
                # Descubre el color del pixel de la posición posicion[1]-1,i
                color = self.screen.get_at((posicion[0]-1, i- int((self.height * 19)/1440)))
                # Pinta una linea tan larga como posicion[2] en la posición posicion[1],i, de color "color"
                pygame.draw.line(self.screen, color, (posicion[0], i- int((self.height * 19)/1440)), (posicion[0]+posicion[2], 1-int((self.height * 19)/1440)+i))
                
            
            # self.screen.fill((247, 241, 238), (posicion[0], posicion[1] - int((self.height * 19) / 1440), posicion[2], posicion[3]))
            texto_escribe = self.font_1.render(chain, True, (0, 0, 200))                        
            text_rect = texto_escribe.get_rect(left=posicion[0], centery=posicion[1])
            self.screen.blit(texto_escribe, text_rect)
            ancho_texto = texto_escribe.get_width()
            self.updateScreen()

        if len(chain) > 1 and chain[-1] == ">" or chain == ">":
            chain = chain[:-1]

        if anula == True:                                               # Si anula es True
            chain = "acción anulada"                                    # La cadena es "acción anulada" para avisar de aborto y no hacer nada     
            
        return chain
    
    def SoundKillData(self):
        self.trash.play()
    
    def SoundWrongAnswer(self):
        self.wrong.play()
                   
    def end(self):
        pygame.quit()
            