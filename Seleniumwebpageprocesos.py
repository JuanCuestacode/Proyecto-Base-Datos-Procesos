

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time
import pandas as pd
import numpy

import chromedriver_autoinstaller
def choose_especiality(especialidad, numjuz):
    switch = {
        1: {
            "A": "Case 1A",
            "B": "Case 1B",
        },
        2: {
            "A": "Case 2A",
            "B": "Case 2B",
        },
        3: {
            "A": "Case 3A",
            "B": "Case 3B",
        },
    }
    return switch.get(especialidad, {}).get(numjuz, "No se encontro")



    
#JUZGADOS CIVILES MUNICIPALES DE BOGOTA(CRA 10)                                                                                                                                                                                                                 





# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver_path = 'D:\Proyectos Curriculum\Pryecto Procesos\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(options=options)
# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()


# Inicializamos el navegador
driver.get('https://procesos.ramajudicial.gov.co/procesoscs/ConsultaJusticias21.aspx?EntryId=%2f%2bm1IAoCqpHB6Lz7RfpRQe3TGlQ%3d')
dropdown = driver.find_element("id","ddlCiudad")
# Create a Select object
select = Select(dropdown)
# Select the option by its value
select.select_by_value("11001") #BOGOTA DC
time.sleep(5) 


WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ddlCiudad"))
    )

# Create a Select object
dropdown2 = driver.find_element(By.XPATH,"//select[@id='ddlEntidadEspecialidad']")
stale_element = True
while stale_element:
    try:
        driver.find_element(By.XPATH, "//option[@value='608-True-3110-11001-JUZGADO DE CIRCUITO-FAMILIA']")
        stale_element = False
    except StaleElementReferenceException:
        stale_element = True
        
        
select2 = Select(dropdown2)
# Select the option by its value
select2.select_by_value('608-True-3110-11001-JUZGADO DE CIRCUITO-FAMILIA') # Seleccion de juzgado
#
# Seleccionar Campo de Radicación

numRad = driver.find_element(By.XPATH,"/html/body/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div[3]/table/tbody/tr[4]/td/div[1]/table/tbody/tr[2]/td/div/input")
numRad.send_keys("11001311000720150052100") # Numero de Radicado

sliderNumProceso= driver.find_element(By.XPATH,"//*[@id='sliderBehaviorNumeroProceso_railElement']/div")

actions = ActionChains(driver)
actions.click_and_hold(sliderNumProceso).pause(1).move_by_offset(200,0).release().perform()

button2 = driver.find_element(By.XPATH,"/html/body/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div[3]/table/tbody/tr[4]/td/div[1]/table/tbody/tr[3]/td/input[1]")
button2.click()
time.sleep(10)


#Tabla de actuaciones 
rows = driver.find_elements(By.XPATH,"//*[@id='divActuacionesDetalle']/table/tbody/tr[2]/td/table/tbody/tr")

print(len(rows))
# create a list to store the data
data = []

# extract the data from each row
for row in rows:
    cells = row.find_elements(By.XPATH,"//*[@id='divActuacionesDetalle']/table/tbody/tr[2]/td/table/tbody/tr/td")
    text_list = []
    for i, cell in enumerate(cells):
        text_list.append(cell.text)
        

driver.quit()

