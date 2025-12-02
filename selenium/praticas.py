from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

navegador = webdriver.Chrome()
print("Navegador Aberto")

navegador.maximize_window()
print("Janela colocada em tela cheia")

navegador.get("https://g1.com.br")
print("Site acessado")

time.sleep(3)

manchetes = navegador.find_elements(By.CLASS_NAME, "feed-post-link")
print("Títulos pegados")

for manch in manchetes:
    print(manch.text)

time.sleep(10)
