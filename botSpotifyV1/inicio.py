# -- coding: utf-8 --
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


# Borrar despues:
# Cuando borre debe cambiar "def _main():" por "def main():"

def main():
    print(os.environ['DISPLAY'])
    
    if os.environ['DISPLAY'] == ":0":
        print("display pc")
        display = Display(visible=True, size=(1900,1268))
        display.start()
        pyautogui._pyautogui_x11._display = Xlib.display.Display(":0")
    else:
        print("sin display")
        display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)
        display.start()
        pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])

    time.sleep(5)
    email="GMAILS"
    passw="PASW"

    print("ingresando a spotify")
        #driver = BaseConexion().conexionChromeHeadless()
    def iniciarSpotify(email,passw):
        try:
            driver = BaseConexion().conexionChrome()
            print ("Driver iniciado")
            acciones = Acciones(driver)
            acciones.maximizar()
            time.sleep(13)
        except Exception as e:
            print (e)

        acciones.ingresarSpotify()
        #acciones.ir("chrome://version/")
        acciones.sleep(5)    
        print("Linea 48")
        #acciones.refreshweb()
        print("Linea 51")
        #acciones.sleep(20)
        #driver.save_screenshot('Almacenamiento/img/loging.png')
        pyautogui.screenshot(os.path.join(pathImg,f"loging.png"))      
        mensaje= f"loging.png"
        enviaremailmensaje(email,mensaje)     
        print("Primera captura enviada")   
        acciones.sleep(20)
        #pyautogui.moveTo(1866, 1223)
        #pyautogui.click()
        valor=1
        valor= random.randint(1,3)
        if valor == 1:  #reproducir lista
            print("INICIANDO REPRODUCCIÓN POR LISTA")  
            with open(os.path.join(pathImg,f"mensaje1.txt"), 'w') as f:
                f.write("Reproduciendo la lista ") 
            mensaje= "mensaje1.txt"
            enviaremailmensaje(email,mensaje)
            acciones.abrirlistareproduccion()
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
            #pyautogui.screenshot(os.path.join(pathImg,f"PlayList.png"))
            #time.sleep(15)
            #imagen= "PlayList.png"
            #enviaremailreproduccion(email,imagen)
            #time.sleep(500)            
        
        elif valor==2: #reproducir directamente del album
            print("INICIANDO REPRODUCCIÓN POR ALBUM")  
            acciones.reproducir2(email)
            
        elif valor ==3:
            print("INICIANDO REPRODUCCIÓN POR LISTA DE AMIGO")  
            acciones.reproducir3(email)

        


    iniciarSpotify (email,passw)



     
    display.stop()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open(os.path.join(pathImg,f"logerror.txt"), 'w') as f:
            f.write(str(e))
        print (e)
        error= "logerror.txt"