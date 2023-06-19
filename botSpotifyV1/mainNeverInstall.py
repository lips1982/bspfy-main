# -*- coding: utf-8 -*-
import datetime
import Xlib.display
from pyvirtualdisplay import Display
import pyautogui
import os
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Paths import pathMensaje
import time
import random
from PQTs.Selenium.Acciones.AccionesReproducir import *
from PQTs.Selenium.Acciones.enviaremail import *
from datetime import datetime
import pyscreeze
from PIL import ImageGrab

def main():

    print ("INICIANDO PYTHON")
    #--> Descomentar para ver en PC
    #display = Display(visible=True, size=(1200,768))

    display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)

    display.start()

    #--> Descomentar para ver en PC
    #pyautogui._pyautogui_x11._display = Xlib.display.Display(":0")

    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ["DISPLAY"])
    screenshot = ImageGrab.grab()
    time.sleep(5)
    
    try: 
        driver = BaseConexion().conexionChrome()

        print ("Driver iniciado")
        acciones = Acciones(driver)
        time.sleep(15)
        acciones.ingresarSpotify()
        time.sleep(3)
        acciones.maximizar()
        time.sleep(5)        
    except Exception as e:
        print(f"{e}")
    print ("Maximizar ok")

    USERDATADIR ="USERDATADIRXXX"
    datestamp=time.strftime("/%Y%m%d%H%M%S")
    print ("Tomando capture")
    screenshot.save(os.path.join(pathImg, f"{datestamp}-loging.png"))
    adjunto= f"{datestamp}-loging.png"
    enviaremailerror("INICIO BOT",adjunto, "INICIO","CONECTADO")  
    
    acciones.refreshweb()
    acciones.sleep(10)
      
    pyautogui.moveTo(1866, 1223)
    pyautogui.click()
    #valor=2
    print ("ELIGIENDO METODO DE REPRODUCCIÓN")
    valor= random.randint(1,3)
    if valor == 1:  #reproducir lista
        
        with open(pathMensaje, 'w') as f:
            f.write("Reproduciendo la lista ") 
        mensaje= "mensaje.txt"
        enviaremailmensaje(USERDATADIR,mensaje)
        print ("Reporte de email enviado linea 69")
        reproducir = acciones.abrirlistareproduccion()
        #pyautogui.screenshot(os.path.join(pathImg,f"01-{USERDATADIR}-loging.png"))
        
        #loging= f"01-{email}-loging.png"
        #enviaremailerror(email,loging, password)  

        time.sleep(10)
            #pyautogui.moveTo(1065, 745)
            #pyautogui.moveTo(1065, 745)
            #pyautogui.click(1065, 745)            
            #time.sleep(2)
            #pyautogui.moveTo(100, 700)
            #pyautogui.click(100,700)              
            #pyautogui.click(100,700)  
            #time.sleep(2)            
            #pyautogui.screenshot(os.path.join(pathImg,f"abrirlista.png"))
            #time.sleep(15)
            #imagen= "abrirlista.png"
            #enviaremailreproduccion(email,imagen)            
        pyautogui.screenshot(os.path.join(pathImg,f"PlayList.png"))
        time.sleep(15)
        imagen= "PlayList.png"
        enviaremailreproduccion(USERDATADIR,imagen)
        time.sleep(500)            
        
    elif valor==2: #reproducir directamente del album
        print ("Iniciando Reproducir album de artista")
        acciones.reproducir2(USERDATADIR)
            
    elif valor ==3:

            acciones.reproducir3(USERDATADIR)

        
     
    display.stop()

if __name__ == '__main__':
    "try:"
    main()
    """except Exception as e:
        with open(os.path.join(pathImg,f"logerror.txt"), 'w') as f:
            f.write(str(e))
        error= "logerror.txt"
"""



