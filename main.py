#Importando a biblioteca 'Selenium' no python
from selenium import webdriver

#Para não fechar a janela aberta
import time

#Aqui ele vai abrir o chrome e abrir diretamente no site pedido
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(120)