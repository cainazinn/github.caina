from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import pyautogui
import time

ano_atual = datetime.now().year
print(ano_atual)


                            # | ---------> Funções auxiliares <--------- |

def esperar_click(navegador, xpath, tempo = 10):
    WebDriverWait(navegador, tempo).until(EC.element_to_be_clickable((By.XPATH, xpath)))

def esperar_presenca(navegador, xpath, tempo = 10):
    WebDriverWait(navegador, tempo).until(EC.presence_of_element_located((By.XPATH, xpath)))

def clicar(navegador, xpath):
    navegador.find_element(By.XPATH, xpath).click()

def digitar(navegador, xpath, texto):
    esperar_presenca(navegador, xpath)
    navegador.find_element(By.XPATH, xpath).send_keys(texto)

def mudar_aba(navegador, indice):
    abas = navegador.window_handles
    navegador.switch_to.window(abas[indice])


                            # | ---------> Função: Login na Onvio <--------- |

def login_onvio(navegador):
    
    print("Abriu o navegador")
    navegador.get("https://onvio.com.br/#/login")
    print("Acessou o site da onvio")

    navegador.maximize_window()
    print("Botou em tela cheia")

    time.sleep(2)

    # Botão de entrar 1
    
    xpath_botaoEntrar1 = "/html/body/div/div[1]/div/main/div/onvio-login/div/div[1]/fieldset/div/div/section/form[3]/div/button"
    esperar_click(navegador, xpath_botaoEntrar1)

    clicar(navegador, xpath_botaoEntrar1)
    print("Primeiro botão de entrar clicado")

    # E-mail

    xpath_caixaEmail = "/html/body/div/div/div/div[2]/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input"
    esperar_presenca(navegador, xpath_caixaEmail)

    digitar(navegador, xpath_caixaEmail, "cainacavalcante352@gmail.com")
    print("Email digitado")

    time.sleep(2)

    # Botão de entrar 2

    xpath_botaoEntrar2 = "/html/body/div/div/div/div[2]/main/section/div/div/div/div[1]/div/form/div[2]/button"
    esperar_click(navegador, xpath_botaoEntrar2)

    clicar(navegador, xpath_botaoEntrar2)
    print("Segundo botão de entrar clicado")

    # Senha

    xpath_caixaSenha = "/html/body/div/div/div/div[2]/main/section/div/div/div/form/div[1]/div/div[2]/div/input"
    esperar_click(navegador, xpath_caixaSenha)

    digitar(navegador, xpath_caixaSenha, "Ca090708!!")
    print('Senha digitada')

    time.sleep(2)

    # Botão de entrar 3

    xpath_botaoEntrar3 = "/html/body/div/div/div/div[2]/main/section/div/div/div/form/div[2]/button"
    esperar_click(navegador, xpath_botaoEntrar3)

    clicar(navegador, xpath_botaoEntrar3)
    print("Terceiro botão de entrar clicado")


                            # | ---------> Função: Acessar documentos <--------- |

def acessar_documentos(navegador):
    xpath_documentos = "/html/body/bm-optional-header/bm-staff-custom-header/bm-header/header/ul[2]/li[2]/li/a/i"
    esperar_click(navegador, xpath_documentos)

    time.sleep(2)

    clicar(navegador, xpath_documentos)
    print("Área de documentos acessada")



                            # | ---------> Função: Selecionar empresa <---------

def selecionar_empresa(navegador, nome_empresa):
    print(f"Acessando empresa: {nome_empresa}")

    xpath_caixaProcurarEmpresa = "//input[@placeholder = 'Selecione um cliente']"
    esperar_click(navegador, xpath_caixaProcurarEmpresa)

    digitar(navegador, xpath_caixaProcurarEmpresa, nome_empresa)
    print(f"Procurando a empresa {nome_empresa}")

    time.sleep(2)

    xpath_empresaDesejada = "//*[contains(@class, 'combobox-grid-column')]"
    esperar_click(navegador, xpath_empresaDesejada)

    time.sleep(2)

    clicar(navegador, xpath_empresaDesejada)
    print(f"Entrando na empresa {nome_empresa}")


                            # | ---------> Função: Acessar setor pessoal <---------

def acessar_setorPessoal(navegador):

    xpath_setorPessoal = "//span[contains(text(), 'Pessoal')]/ancestor::div[1]"
    esperar_click(navegador, xpath_setorPessoal)

    time.sleep(2)

    clicar(navegador, xpath_setorPessoal)
    print("Setor pessoal da empresa acessado")


                            # | ---------> Fluxo Principal <---------

navegador = webdriver.Chrome()

login_onvio(navegador)      # Chama a função que realiza o login no site
acessar_documentos(navegador)       # Chama a função que acessa a área de documentos do site 
mudar_aba(navegador, 1)     # Chama a função que muda a aba para continuar executando o código 
selecionar_empresa(navegador, "Empresa exemplo simples nacional")       # Chama a função que procura a empresa e a acessa
acessar_setorPessoal(navegador)     # Chama a função que acessa o setor pessoal da empresa atualmente acessada
    






time.sleep(10)
