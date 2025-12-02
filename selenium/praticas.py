from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

# =========================
# PEGAR NOTÍCIAS          |
# =========================


# navegador = webdriver.Chrome()
# print("Navegador Aberto")

# navegador.maximize_window()
# print("Janela colocada em tela cheia")

# navegador.get("https://g1.com.br")
# print("Site acessado")

# time.sleep(3)

# manchetes = navegador.find_elements(By.CLASS_NAME, "feed-post-link")
# print("Títulos pegados")

# for manch in manchetes:
#     print(manch.text)

# time.sleep(10)


# ======================================================================================================================

# =================================
# PEGAR PREÇO DE PRODUTOS         |
# =================================

navegador = webdriver.Chrome()
print("Navegador aberto")

navegador.maximize_window()
print("Janela colocada em tela cheia")

navegador.get("https://amazon.com.br")
print("Site amazon acessado")

time.sleep(2)

# Seção de livros
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-xshop']/ul/li[5]/div/a")))

navegador.find_element(By.XPATH, "//*[@id='nav-xshop']/ul/li[5]/div/a").click()
print("Seção de livros acessada")

time.sleep(10)


