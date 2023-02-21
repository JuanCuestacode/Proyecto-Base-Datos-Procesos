import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the website
driver.get("http://www.google.com")

# Find the search box
search_box = driver.find_element_by_name("q")

# Enter a search term
search_box.send_keys("Selenium WebDriver")

# Submit the search form
search_box.submit()

# Wait for the results to load
driver.implicitly_wait(10) # seconds

# Get the results
results = driver.find_elements_by_css_selector("h3 > a")

# Print the results
for result in results:
    print(result.text)

# Close the browser
driver.quit()











df = pd.read_excel(r'D:\Proyectos Curriculum\Pryecto Procesos\BASE DATOS PROCESOS.xlsx')


columEdificio=df['EDIFICIO']
df = df.astype({'EDIFICIO':'string'})
print(df.dtypes)
print(columEdificio[1])


def NEMQUETEBA(num):
    print(df.at[num,'N°'])
    print('NEMQUETEBA')
    
    

def VIRREY(num):
    print(df.at[num,'N°'])
    print('VIRREY')
    

def VIRREY_NORTE(num):
    print(df.at[num,'N°'])
    print('VIRREY NORTE')
    

def JARAMILLO(num):
    print(df.at[num,'N°'])
    print('JARAMILLO')

def HERNANDO_MORALES(num):
    print(df.at[num,'N°'])
    print('HERNANDO MORALES')
       

def CAMACOL(num):
    print(df.at[num,'N°'])
    print('CAMACOL')
    

def SAN_REMO(num):
    print(df.at[num,'N°'])
    print('SAN REMO')
    

def KAYSSER(num):
    print(df.at[num,'N°'])
    print('KAYSSER')
    

def HERNANDO_MORALES_EJECUCIÓN(num):
    print(df.at[num,'N°'])
    print('HERNANDO MORALES EJECUCIÓN')
    
    
def error(num):
    print(df.at[num,'N°'])
    print('NO EDIFICIO')
    
    

switch_edificio = {
        'NEMQUETEBA': NEMQUETEBA,
        'VIRREY': VIRREY,
        'VIRREY NORTE': VIRREY_NORTE,
        'JARAMILLO': JARAMILLO,
        'HERNANDO MORALES': HERNANDO_MORALES,
        'CAMACOL': CAMACOL,
        'SAN REMO': SAN_REMO,
        'KAYSSER': KAYSSER,
        'HERNANDO MORALES EJECUCIÓN': HERNANDO_MORALES_EJECUCIÓN,
        'nan': 'nan'
    }
     




def main(fn,op):
    try:
        switch_edificio[fn](op)
    except KeyError:
        error(op)
    
#Secciono los Edificios de los procesos en Bogotá 



for i in range(len(df)):
    main(columEdificio[i],i)
