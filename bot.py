#Primeiro chamamos a biblioteca do selenium
from selenium import webdriver

#Depois baixamos mais duas bibliotecas que é a do 'Tempo' e a do 'Sitema operacional'
import time
import os

#Essa será a biblioteca para salvar a sessão
from selenium.webdriver.chrome.options import Options

#criamos uma variavel chamada 
dir_path = os.getcwd()

#criamos uma outra variavel com uma funcao chamada options
chrome_options2 = Options()

chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")

#driver = webdriver.Chrome(chrome_options=chrome_options2)
#em versões mais recentes do Selenium, a nomenclatura foi alterada de chrome_options para options.

driver = webdriver.Chrome(options=chrome_options2)

driver.get('https://web.whatsapp.com/')
time.sleep(120)