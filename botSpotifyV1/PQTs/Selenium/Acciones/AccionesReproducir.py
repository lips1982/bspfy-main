# -*- coding: utf-8 -*-

import datetime
import os
from re import L
import time

from PQTs.Selenium.Base import BaseAcciones
from PQTs.Utilizar import urlSpotifysinginUS, sendermail, miscaciones
from selenium.webdriver.common.by import By
from PQTs.Paths import pathImg
import pyautogui
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PQTs.Utilizar import poollistas, poolartista
from PQTs.Selenium.Acciones.enviaremail import enviaremailreproduccion


class Acciones(BaseAcciones):
    def ingresarSpotify(self):
        try:
            self.maximizar()
            print ("Maximizar ventana")
            #self.ir("chrome://version/")

            self.ir(urlSpotifysinginUS)
            self.sleep(2)
            return True
        except:
            self.salir()
            return False

    def abrirlistareproduccion(self):

        xpathlistadereproduccion= (By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/nav/div[2]/div[1]/div[2]/div[4]/div/div/div/div[2]/ul/div/div[2]/li[2]/div/div[1]") 
        xpathbotonplay= (By.XPATH,"//button[@data-testid = 'play-button' and @class = 'Button-sc-qlcn5g-0 DjJKP']")
        xpathcorazones=(By.XPATH,"//span[@class='Type__TypeElement-goli3j-0 eDbSCl']") 
        
        listadereproduccion = self.explicitWaitElementoVisibility(15,xpathlistadereproduccion)
        
        if listadereproduccion:
            try:
                self.click(xpathlistadereproduccion)
            except Exception as e:
                print (e)
                pass
            listaxpathbotonplay = self.explicitWaitElementoVisibility(15,xpathbotonplay)
            if listaxpathbotonplay:
                try:
                    self.click(xpathbotonplay)
                    print("reproduciendo lista OK")
                    time.sleep(7200)
                except Exception as e:
                    print (e)
                    pass
            else:
                self.refreshweb()
                print ("no encontro el xpath play de reproducción")
                time.sleep(5)
                self.abrirlistareproduccion()    
        else:  
            print ("no encontro el xpath lista  de reproducción")
            time.sleep(5)                    
            self.refreshweb()
            self.abrirlistareproduccion()
        time.sleep(10)
        print("entrando a lista de cannciones")
        
        listacanciones = self.explicitWaitElementoInvisibility(15,xpathcorazones)
        corazones = False

        if listacanciones:
            print ("visible lista de canciones")
            listacancio= self.findElements(xpathcorazones)
            print (listacancio)
            if len(listacancio) < 8:  # OJO PARA NUEVOS ALBUNES SE DEBE AJUSTAR EL VALOR
                return False
            for elem in listacancio:
                print(elem)

                elem.click()
                time.sleep(60)
                #print("me gusta", i)
                #i+=1
            corazones=True
        print ("Saliendo ....")
        if corazones:
            time.sleep(900)
        else:
            time.sleep(1500)



    def reproducir2(self,email):
        albumartista =random.choices(poolartista, k=4)
        self.ir(albumartista[0][0])
        time.sleep(10)
        pyautogui.moveTo(1065, 745)
        pyautogui.click(1065, 745)    
        time.sleep(2)
        pyautogui.moveTo(100, 700)
        pyautogui.moveTo(100, 700)
        pyautogui.click(100,700)    
        pyautogui.click(100,700)       

        time.sleep(4)                      
        xpathfollow=(By.XPATH,"//button[@class='idI9vydtCzXVhU1BaKLw']")
        xpathplay= (By.XPATH,"//button[@data-testid='play-button'and @class='Button-sc-qlcn5g-0 DjJKP']")

        follow = self.explicitWaitElementoVisibility(15,xpathfollow)
        try:
            if follow:
                self.click(xpathfollow)
                print("Seguidor nuevo ok")
        except:
                print("Ya es seguidor")            
        play = self.explicitWaitElementoVisibility(15,xpathplay)
        if play:
            self.click(xpathplay)
            print("INICIA REPRODUCIR ARTISTA 1") 
        else:
            print("no se pudo dar play")   
            self.reproducir2(email)

        time.sleep(albumartista[0][1])
        
        print("INICIA ARTISTA 2") 
        
        self.ir(albumartista[1][0])
        time.sleep(10)
        pyautogui.moveTo(1065, 745)
        pyautogui.click(1065, 745)    
        time.sleep(2)
        pyautogui.moveTo(100, 700)
        pyautogui.moveTo(100, 700)
        pyautogui.click(100,700)    
        pyautogui.click(100,700)       

        time.sleep(4)                      
        xpathfollow=(By.XPATH,"//button[@class='idI9vydtCzXVhU1BaKLw']")
        xpathplay= (By.XPATH,"//button[@data-testid='play-button'and @class='Button-sc-qlcn5g-0 DjJKP']")

        follow = self.explicitWaitElementoVisibility(15,xpathfollow)
        try:
            if follow:
                self.click(xpathfollow)
                print("Seguidor nuevo ok")
        except:
                print("Ya es seguidor")            
        play = self.explicitWaitElementoVisibility(15,xpathplay)
        if play:
            self.click(xpathplay)
            print("INICIA REPRODUCIR ARTISTA 2") 
        else:
            print("no se pudo dar play")   
            self.reproducir2(email)

        time.sleep(albumartista[1][1])

        self.ir(albumartista[2][0])
        time.sleep(10)
        pyautogui.moveTo(1065, 745)
        pyautogui.click(1065, 745)    
        time.sleep(2)
        pyautogui.moveTo(100, 700)
        pyautogui.moveTo(100, 700)
        pyautogui.click(100,700)    
        pyautogui.click(100,700)       

        time.sleep(4)                      
        xpathfollow=(By.XPATH,"//button[@class='idI9vydtCzXVhU1BaKLw']")
        xpathplay= (By.XPATH,"//button[@data-testid='play-button'and @class='Button-sc-qlcn5g-0 DjJKP']")

        follow = self.explicitWaitElementoVisibility(15,xpathfollow)
        try:
            if follow:
                self.click(xpathfollow)
                print("Seguidor nuevo ok")
        except:
                print("Ya es seguidor")            
        play = self.explicitWaitElementoVisibility(15,xpathplay)
        if play:
            self.click(xpathplay)
            print("INICIA REPRODUCIR ARTISTA 3")             
        else:
            print("no se pudo dar play")   
            self.reproducir2(email)

        time.sleep(albumartista[2][1])

        self.ir(albumartista[3][0])
        time.sleep(10)
        pyautogui.moveTo(1065, 745)
        pyautogui.click(1065, 745)    
        time.sleep(2)
        pyautogui.moveTo(100, 700)
        pyautogui.moveTo(100, 700)
        pyautogui.click(100,700)    
        pyautogui.click(100,700)       

        time.sleep(4)                      
        xpathfollow=(By.XPATH,"//button[@class='idI9vydtCzXVhU1BaKLw']")
        xpathplay= (By.XPATH,"//button[@data-testid='play-button'and @class='Button-sc-qlcn5g-0 DjJKP']")

        follow = self.explicitWaitElementoVisibility(15,xpathfollow)
        try:
            if follow:
                self.click(xpathfollow)
                print("Seguidor nuevo ok")
        except:
                print("Ya es seguidor")            
        play = self.explicitWaitElementoVisibility(15,xpathplay)
        if play:
            self.click(xpathplay)
            print("INICIA REPRODUCIR ARTISTA 4")             
        else:
            print("no se pudo dar play")   
            self.reproducir2(email)

        time.sleep(albumartista[3][1])


        pyautogui.screenshot(os.path.join(pathImg,f"PlayAlbum.png"))
        time.sleep(10)
        imagen= "PlayAlbum.png"
        enviaremailreproduccion(email,imagen)


    def reproducir3(self,email):

        urlLista =random.choices(poollistas)
        
        
        self.ir(urlLista[0])
        time.sleep(10)
        pyautogui.moveTo(1065, 745)
        pyautogui.click(1065, 745)    
        time.sleep(2)
        pyautogui.moveTo(100, 700)
        pyautogui.moveTo(100, 700)
        pyautogui.click(100,700)    
        pyautogui.click(100,700)    
                            
        xpathplay= (By.XPATH,"//button[@data-testid = 'play-button' and @class = 'Button-sc-qlcn5g-0 DjJKP']")
     
        play = self.explicitWaitElementoVisibility(15,xpathplay)
        if play:
            self.click(xpathplay)
        else:
            print("no se pudo dar play")   
            self.reproducir3(email)
        time.sleep(1500)
        pyautogui.screenshot(os.path.join(pathImg,f"FriendPlayList.png"))
        time.sleep(15)
        imagen= "FriendPlayList.png"
        enviaremailreproduccion(email,imagen)
        time.sleep(500)


    def enviardatos(self,email):
        remitente = 'azuresilk02@gmail.com'
        destinatarios = ['azuresilkmain@gmail.com']
        asunto = f'Lista de reproduccion : {email}'
        cuerpo = f"{str(datetime.datetime.now().strftime('%H-%M-%S'))}"
        ruta_adjunto = (os.path.join(pathImg,f"{email}.png"))
        nombre_adjunto = f'{email}.png'

        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()
        
        # Establecemos los atributos del mensaje
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open(ruta_adjunto, 'rb')
        
        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)
        
        # Creamos la conexión con el servidor
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        
        # Ciframos la conexión
        sesion_smtp.starttls()

        # Iniciamos sesión en el servidor
        #sesion_smtp.login('mayfeljonas1229@gmail.com','dudwvopyazvtxtun')
        emailsender=random.choice(sendermail)
        corre, contrase = emailsender
        sesion_smtp.login(corre,contrase)

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios, texto)

        # Cerramos la conexión
        sesion_smtp.quit()





