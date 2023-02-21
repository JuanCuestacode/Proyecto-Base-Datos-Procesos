

from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import time
import pandas as pd

import chromedriver_autoinstaller

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'D:\Proyectos Curriculum\Pryecto Procesos\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)
# Inicializamos el navegador
driver.get("https://eltiempo.es")

#Asi se oprime un boton
button = driver.find_element("id","didomi-notice-agree-button")
button.click()


#Buscar en una barra de busqueda
searchbar= driver.find_element("id","term")
searchbar.send_keys("Madrid")
time.sleep(10)

#Asi se oprime un boton
button2 = driver.find_element("id","didomi-notice-agree-button")
button2.click()

