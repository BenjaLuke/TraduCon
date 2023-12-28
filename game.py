import  pygame
import  sys
from    datetime import datetime
import  time
import  random

import  errores
import  mates

class Game:
    def __init__(self):
        
        pygame.init()

        
        screen_info = pygame.display.Info()
        self.width, self.height = screen_info.current_w, screen_info.current_h
        # self.width = 2000
        self.height = (self.width*1440)/3440
        
        self.screen = pygame.display.set_mode((self.width, self.height),)# pygame.FULLSCREEN)

        
        pygame.display.set_caption("Tradu con")

        
        pygame.mixer.init()
         
        
        self.background_image = pygame.image.load("EXTRAS/escritorio_3.jpg")  
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        
        self.paper_sup = pygame.image.load("EXTRAS/hoja_superior.png")
        self.paper_mid = pygame.image.load("EXTRAS/hoja_media.png")
        self.paper_down = pygame.image.load("EXTRAS/hoja_inferior.png")
        
        self.paper_sup = pygame.transform.scale(self.paper_sup, (int((self.width*664)/3440), int((self.height*116)/1440)))
        self.paper_mid = pygame.transform.scale(self.paper_mid, (int((self.width*664)/3440), int((self.height*71)/1440)))
        self.paper_down = pygame.transform.scale(self.paper_down, (int((self.width*664)/3440), int((self.height*145)/1440)))
        
        self.paper_sup_big = pygame.transform.scale(self.paper_sup, (int((self.width*800)/3440), int((self.height*116)/1440)))
        self.paper_mid_big = pygame.transform.scale(self.paper_mid, (int((self.width*800)/3440), int((self.height*71)/1440)))
        self.paper_down_big = pygame.transform.scale(self.paper_down, (int((self.width*800)/3440), int((self.height*145)/1440)))
        
        self.paper_sup_super_big = pygame.transform.scale(self.paper_sup, (int((self.width*1500)/3440), int((self.height*116)/1440)))
        self.paper_mid_super_big = pygame.transform.scale(self.paper_mid, (int((self.width*1500)/3440), int((self.height*71)/1440)))
        self.paper_down_super_big = pygame.transform.scale(self.paper_down, (int((self.width*1500)/3440), int((self.height*145)/1440)))
        
        self.paper_graph = pygame.image.load("EXTRAS/hoja_de_grafica.png") 
        self.paper_graph = pygame.transform.scale(self.paper_graph, (int((self.width*1331)/3440), int((self.height*1400)/1440)))  
        
        self.logo = pygame.image.load("EXTRAS/logo.png")
        self.logo = pygame.transform.scale(self.logo, ((self.width*177)/3440, (self.height*185)/1440))
        self.logoBig = pygame.image.load("EXTRAS/logo_traducon.png").convert_alpha()
        self.logoBig = pygame.transform.scale(self.logoBig, ((self.width*669)/3440, (self.height*609)/1440))

        
        self.font_1 = pygame.font.Font("EXTRAS/JMH Typewriter-Bold.ttf", int((self.width*30)/3440))
        self.font_2 = pygame.font.Font("EXTRAS/JMH Typewriter-Bold.ttf", int((self.width*30)/3440))
        self.font_3 = pygame.font.Font("EXTRAS/JMH Typewriter-Bold.ttf", int((self.width*40)/3440))
        
        
        self.pass_page = pygame.mixer.Sound("EXTRAS/pasa hoja.wav")
        self.trash = pygame.mixer.Sound("EXTRAS/arruga hoja.wav")    
        self.wrong = pygame.mixer.Sound("EXTRAS/wrong.wav")  
        self.typewriter = [pygame.mixer.Sound("EXTRAS/typewriter_1.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_2.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_3.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_4.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_5.wav"),
                           pygame.mixer.Sound("EXTRAS/typewriter_6.wav")]
        self.typewriter_shift = pygame.mixer.Sound("EXTRAS/typewriter_shift.wav")
        self.typewriter_carro = pygame.mixer.Sound("EXTRAS/typewriter_carro.wav")
        self.typewriter_borrar = pygame.mixer.Sound("EXTRAS/typewriter_backspace.wav")
        self.typewriter_espacio = pygame.mixer.Sound("EXTRAS/typewriter_space.wav")
         
        
        self.logo_origen = self.width+int((self.width*100)/3440)
        self.logo_destino = int((self.width/10)*9)
                
    def run(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    pygame.quit()
                    sys.exit()

            
            self.screen.blit(self.background_image, (0, 0))

            
            self.updateScreen()
    
            return
        
    def updateScreen(self):
        pygame.display.flip()
        
    def paper(self,altura,anchura,trozos,que_es = 0):
        self.pass_page.play()
        
        altura = int((self.width*altura)/3440)
        anchura = int((self.height*anchura)/1440)

        for i in range(trozos):
            if i == 0:
                if que_es == 0:
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
        
        self.screen.blit(self.paper_graph, ( self.width-int((self.width*1400)/3440), self.height-(int((self.height*1250)/1440)) ) )
        
        
        listaDeDatos = self.calculaDatosGrafica(proyectoSinExt,Datos,Procesos,Excepciones)
        
        
        for i in listaDeDatos: 
            texto_escribe = i[3].render(i[0], True, (0,50,150))    
            ancho = self.width-int((self.width*i[1])/3440)
            alto = self.height-int((self.height*i[2])/1440)
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
            NumeroPaginasPendientes = " --- "
        try:    
            NumeroPaginasPorRevisar     = int(NumeroPaginasOriginales) - int(NumeroPaginasRevisadas)
        except:
            NumeroPaginasPorRevisar = " --- "
        
        FechaInicioProyecto         = Datos[0][3]
        
        try:
            FechaInicioProyectoSuma     = datetime.strptime(FechaInicioProyecto, "%d/%m/%y")
        except:
            FechaInicioProyectoSuma = " --- "
        FechaActual                 = datetime.now()
        try:
            FechaActual                 = FechaActual.strftime("%d/%m/%y")
        except:
            FechaActual = " --- "
        try:
            FechaActualSuma             = datetime.strptime(FechaActual, "%d/%m/%y")
        except:
            FechaActualSuma = " --- "
        FechaEntrega                = Datos[0][4]   
        try:
            FechaEntregaSuma            = datetime.strptime(FechaEntrega, "%d/%m/%y")
        except:
            FechaEntregaSuma = " --- "
        try:
            DiasRestantes               = FechaEntregaSuma - FechaActualSuma
        except:
            DiasRestantes = " --- "
            
        try:
            DiasRestantes               = (DiasRestantes.days)+1
        except:
            DiasRestantes = " --- "
        try:
            DiasParaProyecto            = FechaEntregaSuma - FechaInicioProyectoSuma  
        except:
            DiasParaProyecto = " --- "
        try:
            DiasParaProyecto            = DiasParaProyecto.days
        except:
            DiasParaProyecto = " --- "
        try:
            DiasYaPasados               = FechaActualSuma - FechaInicioProyectoSuma
        except:
            DiasYaPasados = " --- "
        try:
            DiasYaPasados               = DiasYaPasados.days      
        except:
            DiasYaPasados = " --- "
        try:    
            DiasExentos                 = len(Excepciones)
            for Excepcion in Excepciones:
                FechaExcepcion = Excepcion[1]
                try:
                    FechaExcepcionSuma = datetime.strptime(FechaExcepcion, "%d/%m/%y")
                except:
                    FechaExcepcionSuma = " --- "
                if FechaExcepcionSuma < FechaActualSuma:
                    DiasExentos -= 1
        except:
            DiasExentos = " --- "
        try:
            DiasPosibles                = FechaEntregaSuma - FechaInicioProyectoSuma
        except:
            DiasPosibles = " --- "
        try:
            DiasPosibles                = (DiasPosibles.days)+1
        except:
            DiasPosibles = " --- "
        try:
            DiasReales                  = DiasRestantes - DiasExentos
        except:
            DiasReales = " --- "
        TantoCientoParaRevision     = Datos[0][13]
        try:
            TantoCientoParaTraduccion   = 100 - TantoCientoParaRevision
        except:
            TantoCientoParaTraduccion = " --- "
        DiasYaDedicadosRevision     = 0
        try:
            DiasProyectoEnMarcha        = FechaActualSuma - FechaInicioProyectoSuma
        except:
            DiasProyectoEnMarcha = " --- "
        try:
            DiasProyectoEnMarcha        = DiasProyectoEnMarcha.days
        except:
            DiasProyectoEnMarcha = " --- "
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
            DiasADedicarTrad = " --- "
        try:
            DiasADedicarTrad = mates.redondea(DiasADedicarTrad,2)
        except:
            DiasADedicarTrad = " --- "
        try:
            DiasADedicarRev  = DiasReales * TantoCientoParaRevision / 100
        except:
            DiasADedicarRev = " --- "
        try:
            DiasADedicarRev  = mates.redondea(DiasADedicarRev,2)
        except:
            DiasADedicarRev = " --- "
            
        try:
            PorcientoRevisionReal       = DiasYaDedicadosRevision * 100 / DiasPosibles
        except:
            PorcientoRevisionReal = " --- "
        try:
            PorcientoTraduccionReal     = DiasYaDedicadosTraduccion * 100 / DiasPosibles
        except:
            PorcientoTraduccionReal = " --- "
        try:
            PorcientoMixtoReal          = DiasDedicadosAmbos * 100 / DiasPosibles
        except: 
            PorcientoMixtoReal = " --- "
        PaginasRevisadas            = 0
        for Proceso in Procesos:
            if Proceso[3] == "R": 
                PaginasRevisadas += int(Proceso[2])        
        try:
            PaginasTraduceAlDiaDesdeHoy = NumeroPaginasPendientes/DiasReales
        except: 
            PaginasTraduceAlDiaDesdeHoy = " --- "
        try:
            PaginasTraduceAlDiaDesdeHoy  = mates.redondea(PaginasTraduceAlDiaDesdeHoy,0)
        except:
            PaginasTraduceAlDiaDesdeHoy = " --- "
        try:
            PaginasRevisaAlDiaDesdeHoy = NumeroPaginasPorRevisar/DiasReales
        except:
            PaginasRevisaAlDiaDesdeHoy = " --- "
        try:
            PaginasRevisaAlDiaDesdeHoy = mates.redondea(PaginasRevisaAlDiaDesdeHoy,0)
        except:
            PaginasRevisaAlDiaDesdeHoy = " --- "         
        try:
            PaginasTraduceAlDiaDesdeMan = NumeroPaginasPendientes/(DiasReales-1)
        except:
            PaginasTraduceAlDiaDesdeMan = " --- "
        try:    
            PaginasTraduceAlDiaDesdeMan = mates.redondea(PaginasTraduceAlDiaDesdeMan,0)
        except:
            PaginasTraduceAlDiaDesdeMan = " --- "
        try:
            PaginasRevisaAlDiaDesdeMan = NumeroPaginasPorRevisar/(DiasReales-1)
        except:
            PaginasRevisaAlDiaDesdeMan = " --- "  
        try:
            PaginasRevisaAlDiaDesdeMan = mates.redondea(PaginasRevisaAlDiaDesdeMan,0)
        except:
            PaginasRevisaAlDiaDesdeMan = " --- "  
        tituloLargo = ("Proyecto de "+TipoDeConteo+" "+proyectoSinExt)
        todasLasFechas = "Inicio: "+FechaInicioProyecto+" - Hoy: "+ FechaActual +" - Entrega: "+FechaEntrega
        
        
        listaDeDatos.append([tituloLargo,1200,1050,self.font_2])
        listaDeDatos.append([todasLasFechas,1200,975,self.font_2])
        listaDeDatos.append(["      Páginas",1200,900,self.font_2])
        listaDeDatos.append(["Totales:",1200,825,self.font_2])
        listaDeDatos.append([str(NumeroPaginasOriginales),990,825,self.font_2])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Traducidas: ",1200,725,self.font_2])
        else:
            listaDeDatos.append(["Corregidas: ",1200,725,self.font_2])
        listaDeDatos.append([str(NumeroPaginasTraducidas),990,725,self.font_2])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Por trad.: ",1200,675,self.font_2])
        else:
            listaDeDatos.append(["Por corr.: ",1200,675,self.font_2])
        listaDeDatos.append([str(NumeroPaginasPendientes),990,675,self.font_2])
        listaDeDatos.append(["Revisadas: ",1200,575,self.font_2])
        listaDeDatos.append([str(NumeroPaginasRevisadas),990,575,self.font_2])
        listaDeDatos.append(["Por revisar: ",1200,525,self.font_2])
        listaDeDatos.append([str(NumeroPaginasPorRevisar),990,525,self.font_2])
        
        listaDeDatos.append(["          Días",900,900,self.font_2])
        listaDeDatos.append(["Totales: ",900,825,self.font_2])
        listaDeDatos.append([str(DiasPosibles),585,825,self.font_2])
        listaDeDatos.append(["Pasados: ",900,775,self.font_2])
        listaDeDatos.append([str(DiasYaPasados),585,775,self.font_2])
        listaDeDatos.append(["Restantes: ",900,725,self.font_2])
        listaDeDatos.append([str(DiasRestantes),585,725,self.font_2])
        listaDeDatos.append(["Exentos: ",900,675,self.font_2])
        listaDeDatos.append([str(DiasExentos),585,675,self.font_2])
        listaDeDatos.append(["Reales: ",900,625,self.font_2])
        listaDeDatos.append([str(DiasReales),585,625,self.font_2])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Dedic. T. desde hoy:",900,575,self.font_2])
        else:
            listaDeDatos.append(["Dedic. C. desde hoy:",900,575,self.font_2])
        listaDeDatos.append([str(DiasADedicarTrad),585,575,self.font_2])
        listaDeDatos.append(["Dedic. R. desde hoy:",900,525,self.font_2])
        listaDeDatos.append([str(DiasADedicarRev),585,525,self.font_2])
        listaDeDatos.append(["Tradujiste:",900,475,self.font_2])
        listaDeDatos.append([str(DiasYaDedicadosTraduccion),585,475,self.font_2])
        listaDeDatos.append(["Revisaste:",900,425,self.font_2])
        listaDeDatos.append([str(DiasYaDedicadosRevision),585,425,self.font_2])
        listaDeDatos.append(["Ambos:",900,375,self.font_2])
        listaDeDatos.append([str(DiasDedicadosAmbos),585,375,self.font_2])
        
        listaDeDatos.append(["Tanto % sobre días",490,900,self.font_2])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Trad. Objetivo:",490,825,self.font_2])
        else:
            listaDeDatos.append(["Corr. Objetivo:",490,825,self.font_2])
        try:
            listaDeDatos.append([str(int(TantoCientoParaTraduccion))+"%",190,825,self.font_2])
        except:
            listaDeDatos.append([" --- ",190,825,self.font_2])
            
        listaDeDatos.append(["Rev. Objetivo:",490,775,self.font_2])
        try:
            listaDeDatos.append([str(int(TantoCientoParaRevision))+"%",190,775,self.font_2])
        except:
            listaDeDatos.append([" --- ",190,775,self.font_2])
        if Datos[0][7] == "T":
            listaDeDatos.append(["Traduc. Real:",490,675,self.font_2])
        else:
            listaDeDatos.append(["Correg. Real:",490,675,self.font_2])
        try:
            listaDeDatos.append([str(int(PorcientoTraduccionReal))+"%",190,675,self.font_2])
        except:
            listaDeDatos.append([" --- ",190,675,self.font_2])
        listaDeDatos.append(["Revisión Real:",490,625,self.font_2])
        try:
            listaDeDatos.append([str(int(PorcientoRevisionReal))+"%",190,625,self.font_2])
        except:
            listaDeDatos.append([" --- ",190,625,self.font_2])
        listaDeDatos.append(["Mixto Real:",490,575,self.font_2])
        try:
            listaDeDatos.append([str(int(PorcientoMixtoReal))+"%",190,575,self.font_2])
        except:
            listaDeDatos.append([" --- ",190,575,self.font_2])
            
        listaDeDatos.append([" Pág. trad/rev a partir de hoy: "+str(PaginasTraduceAlDiaDesdeHoy)+" / "+str(PaginasRevisaAlDiaDesdeHoy),1200,250,self.font_3])
        listaDeDatos.append([" Pág, trad/rev a partir mañana: "+str(PaginasTraduceAlDiaDesdeMan)+" / "+str(PaginasRevisaAlDiaDesdeMan) ,1200,180,self.font_3])
        
        return listaDeDatos
        
    def text(self,altura,anchura,textos):
        
        altura = int((self.width*altura)/3440)
        anchura = int((self.height*anchura)/1440)
        
        textos.insert(1,"")
        textos.insert(1,"0 - Salir")
        
        
        textos.append("")
        textos.append("Elige una opción")
                
        num_bucle = 0
        
        for i in textos:
            if num_bucle == 0:
                texto_escribe = self.font_1.render(i, True, (255, 0, 0))
            elif num_bucle == 1:
                texto_escribe = self.font_2.render(i, True, (0, 200, 100))
            elif num_bucle == len(textos)-1:
                texto_escribe = self.font_2.render(i, True, (0, 0, 255))
            else:
                texto_escribe = self.font_2.render(i, True, (0, 0, 0))
            text_rect = texto_escribe.get_rect(left= anchura, centery = altura)
            self.screen.blit(texto_escribe, text_rect)
            altura += int((self.height*71)/1440)
            num_bucle += 1
    
    def textAlone(self,altura,anchura,texto): 
        altura = int((self.width*altura)/3440)
        anchura = int((self.height*anchura)/1440)
        
        texto_escribe = self.font_2.render(texto, True, (0, 0, 200))
        text_rect = texto_escribe.get_rect(left= altura, centery = anchura)
        self.screen.blit(texto_escribe, text_rect)
        
    def animaLogoEntra(self):

        
        start_point = (self.logo_origen, int((self.height*150)/1440))
        end_point = (self.logo_destino, int((self.height*150)/1440))

        
        direction = (end_point[0] - start_point[0], end_point[1] - start_point[1])

        
        length = pygame.math.Vector2(direction).length()
        direction_normalized = (direction[0] / length, direction[1] / length)

        
        image_rect = self.logo.get_rect(center=start_point)

        
        speed = 40
        
        cotejo = True
        while cotejo:
           
            
            image_rect.x += direction_normalized[0] * speed
            image_rect.y += direction_normalized[1] * speed

            
            self.screen.blit(self.background_image, (0, 0))
            
            
            self.screen.blit(self.logo, image_rect) 
            
            
            self.updateScreen()
            
            
            time.sleep(0.03)
            
            
            if image_rect.x <= self.logo_destino:
                cotejo = False
        return
    
    def fadeIn(self):
        rectangulo = pygame.Rect(0,0, self.width,self.height)
        for i in range (255):
            pygame.draw.rect(self.screen, (0,0,0), rectangulo)    
            self.logoBig.set_alpha(i)            
            self.screen.blit(self.logoBig,((self.width/2)-int((self.width*335))/3440,(self.height/2)-int((self.height*305)/1440)))
            self.updateScreen()
            time.sleep(0.003)
        time.sleep(2)
        
    def fadeOut(self):
        rectangulo = pygame.Rect(0,0, self.width,self.height)
        pygame.draw.rect(self.screen, (0,0,0), rectangulo)    
        self.logoBig.set_alpha(255)
        self.screen.blit(self.logoBig,((self.width/2)-int((self.width*335))/3440,(self.height/2)-int((self.height*305)/1440)))
        self.updateScreen()
        time.sleep(1)                        
        for i in range (255, 0, -1):
            pygame.draw.rect(self.screen, (0,0,0), rectangulo)    
            self.logoBig.set_alpha(i)
            self.screen.blit(self.logoBig,((self.width/2)-int((self.width*335))/3440,(self.height/2)-int((self.height*305)/1440)))
            self.updateScreen()
            time.sleep(0.003)
        time.sleep(0.5)
        
    def pushAndCome(self):
        envio = ""
        cotejo = True
        while cotejo:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    tecla_pulsada = event.key
                    try:
                        envio += chr(tecla_pulsada)
                        aleatorio = random.randint(0,5)
                        self.typewriter[aleatorio].play()
                        if envio == "0":
                            cotejo = False
                        else:
                            for i in range(200):
                                time.sleep(0.0001)
                                keys = pygame.key.get_pressed()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        tecla_pulsada = event.key
                                        try:
                                            envio += chr(tecla_pulsada)
                                            aleatorio = random.randint(0,5)
                                            self.typewriter[aleatorio].play()                                        
                                            break
                                        except:
                                            pass
                        cotejo = False
                    except:
                        pass
        return envio
    
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

        while cotejo:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    tecla_pulsada = event.unicode
                    if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):    
                        shift_pressed = True
                    elif event.key == pygame.K_CAPSLOCK:
                        caps_pressed = not caps_pressed
                    elif event.key == pygame.K_RETURN:
                        if len(chain) > 0:
                            if chain[-1] == ">":
                                chain = chain[:-1]
                            elif chain == ">":
                                chain = ""
                        termina, chain = errores.Errores(chain, error)
                        if termina:
                            self.typewriter_carro.play()
                            cotejo = False
                        else:
                            self.wrong.play()
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
            self.screen.fill((247, 241, 238), (posicion[0], posicion[1] - int((self.height * 19) / 1440), posicion[2], posicion[3]))
            texto_escribe = self.font_2.render(chain, True, (0, 0, 200))
            text_rect = texto_escribe.get_rect(left=posicion[0], centery=posicion[1])
            self.screen.blit(texto_escribe, text_rect)
            ancho_texto = texto_escribe.get_width()
            self.updateScreen()

        if len(chain) > 1 and chain[-1] == ">" or chain == ">":
            chain = chain[:-1]

        return chain
    
    def SoundKillData(self):
        self.trash.play()
    
    def SoundWrongAnswer(self):
        self.wrong.play()
                   
    def end(self):
        pygame.quit()
            