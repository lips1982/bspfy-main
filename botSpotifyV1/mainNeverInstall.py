# -*- coding: utf-8 -*-
import datetime
import Xlib.display
from pyvirtualdisplay import Display
import pyautogui
import os
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Paths import pathImg
import time
import random
from PQTs.Selenium.Acciones.AccionesReproducir import Acciones
from PQTs.Selenium.Acciones.enviaremail import *
from datetime import datetime


def main():


    #--> Descomentar para ver en PC
    #display = Display(visible=True, size=(1200,768))

    display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)

    display.start()

    #--> Descomentar para ver en PC
    #pyautogui._pyautogui_x11._display = Xlib.display.Display(":0")

    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    time.sleep(10)
    email="GMAILS"
    passw="PASW"
    
    
    print("Iniciando driver")
    try:
        driver = BaseConexion().conexionChrome()
        time.sleep(5)
    except Exception as e:
        print (e)
    
    print("ingresando a spotify")
        #driver = BaseConexion().conexionChromeHeadless()
   
    def iniciarSpotify(email,driver):
        acciones = Acciones(driver)

        acciones.ingresarSpotify()

        print("Linea 48")

        acciones.refreshweb()
        print("Linea 51")
        print("Primera captura iniciando")
        acciones.sleep(10)
        pyautogui.screenshot(os.path.join(pathImg,"loging.png"))
        acciones.sleep(15)
        mensaje= f"loging.png"
        enviaremailmensaje(email,mensaje)     
        print("Primera captura enviada")   
        pyautogui.moveTo(1866, 1223)
        pyautogui.click()
        valor= random.randint(1,3)
        if valor == 1:  #reproducir lista
            with open(os.path.join(pathImg,f"mensaje1.txt"), 'w') as f:
                f.write("Reproduciendo la lista ") 
            mensaje= "mensaje1.txt"
            enviaremailmensaje(email,mensaje)
            reproducir = acciones.abrirlistareproduccion()
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
            enviaremailreproduccion(email,imagen)
            time.sleep(500)            
        
        elif valor==2: #reproducir directamente del album

            acciones.reproducir2(email)
            
        elif valor ==3:

            acciones.reproducir3(email)

        


    iniciarSpotify (email,driver)



     
    display.stop()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open(os.path.join(pathImg,f"logerror.txt"), 'w') as f:
            f.write(str(e))
        print (e)
        error= "logerror.txt"