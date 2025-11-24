from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# ========================================================
# Funções auxiliares
# ========================================================


def esperar_click(navegador, xpath, tempo = 10):
    WebDriverWait(navegador, tempo).until(EC.element_to_be_clickable((By.XPATH, xpath)))

def esperar_presenca(navegador, xpath, tempo = 10):
    WebDriverWait(navegador, tempo).until(EC.presence_of_element_located((By.XPATH, xpath)))

def clicar(navegador, xpath):
    navegador.find_element(By.XPATH, xpath).click()

def digitar(navegador, xpath, texto):
    navegador.find_element(By.XPATH, xpath).send_keys(texto)

    
# ========================================================
# Função: Login na Onvio
# ========================================================


def login_onvio(navegador):
    print("Abriu o navegador")
    navegador.get("https://onvio.com.br/#/login")
    print("Acessou o site da onvio")

    navegador.maximize_window()
    print("Botou em tela cheia")

    time.sleep(2)

    # Entrar 1

    esperar_click(navegador, "/html/body/div/div[1]/div/main/div/onvio-login/div/div[1]/fieldset/div/div/section/form[3]/div/button")

    clicar(navegador, "/html/body/div/div[1]/div/main/div/onvio-login/div/div[1]/fieldset/div/div/section/form[3]/div/button")
    print("Primeiro botão de entrar clicado")

    # E-mail
    esperar_presenca(navegador, "")


























navegador = webdriver.Chrome()
login_onvio(navegador)

time.sleep(2)
