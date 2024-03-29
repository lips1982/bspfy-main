# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


import os

dirnamePath = os.path.dirname(__file__)
service = Service(executable_path=r'/usr/bin/chromedriver')
#chromedriver = os.path.join(dirnamePath, 'chromedriver')

class BaseConexion():
    def __init__(self):
        
        self.options = webdriver.ChromeOptions()

        self.options.page_load_strategy = 'normal'        
        self.options.add_argument("--disable-xss-auditor")
        self.options.add_argument("--disable-web-security")
        #self.options.add_argument("--flag-switches-begin")
        #self.options.add_argument("--flag-switches-end")       
        self.options.add_argument("--allow-running-insecure-content")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-setuid-sandbox")
        self.options.add_argument("--disable-webgl")
        self.options.add_argument("--enable-popup-blocking")
        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')  
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-dev-shm-usage')    
        self.options.add_argument('--disable-infobars')
        self.options.add_argument('--user-data-dir=./opt/data-dir')
        self.options.add_argument('--user-profile-directory=./opt/data-dir/Default')

        #self.options.add_argument('--user-data-dir=./data-dir')
     
        #self.options.add_argument("--incognito")   
        self.options.add_argument('--disable-gpu')
        self.options.add_experimental_option("excludeSwitches", ["enable-logging","enable-automation"])
        prefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
        self.options.add_experimental_option("prefs", prefs)
        
        
        
    def conexionChromeHeadless(self) :
        self.options.add_argument("--headless")
        driver = webdriver.Chrome(options=self.options)
        
        return driver

    def conexionChrome(self) :        
        

        driver = webdriver.Chrome(service=service, options=self.options)
        
        return driver

class BaseAcciones():
    def __init__(self, driver):
        self.driver = driver

    def ir(self, url):
        self.driver.get(url)

    def salir(self):
        self.driver.quit()

    def findElement(self, el):
        elemento = self.driver.find_element(*el)
        return elemento
    def findElements(self, el):
        elemento = self.driver.find_elements(*el)
        return elemento
    def selecionarlista(self, el,valor):
        el.select_by_value(valor)
         

    def escribir(self, el, msj):
        self.findElement(el).send_keys(msj)
        self.sleep(1)

    def pagedown(self, el):
        self.sleep(1)        
        self.findElement(el).send_keys(Keys.PAGE_DOWN)
        self.sleep(1)  
    
    def pagedown(self, el):
        self.sleep(1)        
        self.findElement(el).send_keys(Keys.PAGE_UP)
        self.sleep(1)  

    def clear(self,el):
         self.findElement(el).clear()
        
    def refreshweb(self):
        self.driver.refresh()

    def ubicarscroll(self,el):
         self.findElement(el).location_once_scrolled_into_view

    def pantallazo(self,filename):
         self.save_screenshot(filename)



    def maximizar(self):
        self.driver.maximize_window()

    def click(self, el):
        self.findElement(el).click()
        self.sleep(0.8)
    def elementos(self, el):
        return self.findElements(el)
        self.sleep(0.8)
    def cantidadWindowHandle(self):
        return self.driver.window_handles

    def cambiarTabEspecifico(self, tab):
        self.driver.switch_to.window(tab)

    def sleep(self, sec):
        time.sleep(sec)

    def executeScript(self, script):
        self.driver.execute_script(script)

    def explicitWaitElementoVisibility(self,time,el):
        try:
            elemento = WebDriverWait(self.driver, timeout=time).until(expected_conditions.visibility_of_element_located(el))
            return elemento
        except:
            return False

    def explicitWaitElementoInvisibility(self,time,el):
        try:
            elemento = WebDriverWait(self.driver, timeout=time).until(expected_conditions.invisibility_of_element_located(el))
            return elemento
        except:
            return False

    def explicitWaitUrl(self,time,url):
        try:
            url = WebDriverWait(self.driver, timeout=time).until(expected_conditions.url_to_be(url))
            return url
        except:
            return False


    def executeScript(self, script):
        return self.driver.execute_script(script)

    def switchToIframe(self, el):
        iframe = self.findElement(el)
        self.driver.switch_to.frame(iframe)

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()            

    def texto(self, el):
        textoelemento = self.driver.find_element(el)
        txt = textoelemento.text
        print(txt)
        return txt