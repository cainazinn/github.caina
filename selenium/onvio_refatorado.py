from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from pyautogui import moveTo, click
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


                            # | ---------> Função: Mudar aba <--------- |

def mudar_aba(navegador, indice):
    abas = navegador.window_handles
    navegador.switch_to.window(abas[indice])

    
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
    
    navegador.maximize_window()
    navegador.switch_to.window(navegador.window_handles[1])
    navegador.execute_script("window.focus();")

    time.sleep(1)

    moveTo(143, 622)

    click()
    print(f"Acessando setor pessoal da empresa")

    time.sleep(5)


                            # | ---------> Função: Criar pasta se não existir <---------

def criar_pasta_seNãoExistir(navegador, ano_atual):

    print(f"Verificando se a pasta do ano {ano_atual + 1} existe")
    try:
        # Tenta encontrar a pasta 2026
        xpath_pasta2026 = f"//a[contains(text(), '{ano_atual + 1}')]"

        esperar_presenca(navegador, xpath_pasta2026, 5)

        # Se encontrar diz que a pasta já existe 
        print(f"Pasta {ano_atual + 1} já existe!")

        
        return
    
    # Se não encontrar cria uma nova pasta    

    except:
        print(f"Pasta {ano_atual + 1} não encontrada, criando...")

        time.sleep(2)

        xpath_criarNovo = "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[1]/a"
        clicar(navegador, xpath_criarNovo)
        print("Criando nova pasta")

        time.sleep(2)

        xpath_novoPasta = "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[1]/ul/li[1]/a"
        clicar(navegador, xpath_novoPasta)

        xpath_nomearPasta = "/html/body/div[1]/div/div/div/div[1]/form/div[1]/input"
        esperar_presenca(navegador, xpath_nomearPasta)

        time.sleep(2)

        digitar(navegador, xpath_nomearPasta, f"{ano_atual + 1}")
        print(f"Pasta nomeada com o ano {ano_atual + 1}")

        time.sleep(2)

        xpath_salvar = "/html/body/div[1]/div/div/div/div[2]/button[1]"
        clicar(navegador, xpath_salvar)
        print(f"Pasta {ano_atual + 1} criada")

        time.sleep(2)

        xpath_pasta2025 = "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[2]/div[1]/div[3]/div[2]/div/span/dms-grid-text-cell/div/span[1]/a"
        xpath_gerenc = "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[4]/a"
        xpath_copy = "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[4]/ul/li[4]/a"
        xpath_setaVoltar_copiarPara = "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/div/span[1]"
        xpath_selec2026_copiarPara = "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/ul/li[3]"
        xpath_confirmCopy = "/html/body/div[1]/div/div/div/div[3]/button[1]"

        esperar_presenca(navegador, xpath_pasta2025)

        time.sleep(2)

        clicar(navegador, xpath_pasta2025)
        print("Pasta 2025 acessada")

        xpath_selecSubpastas = "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[7]/div/div/div/div/i"
        esperar_presenca(navegador, xpath_selecSubpastas)

        time.sleep(2)

        clicar(navegador, xpath_selecSubpastas)
        print("Subpastas selecionadas")
        time.sleep(2)

        clicar(navegador, xpath_gerenc)
        print("Gerenciando subpastas...")

        time.sleep(2)

        clicar(navegador, xpath_copy)
        print("Copiando subpastas")

        time.sleep(2)

        esperar_presenca(navegador, xpath_setaVoltar_copiarPara)

        time.sleep(2)

        clicar(navegador, xpath_setaVoltar_copiarPara)

        time.sleep(2)

        esperar_presenca(navegador, xpath_selec2026_copiarPara)

        time.sleep(2)

        clicar(navegador, xpath_selec2026_copiarPara)

        time.sleep(2)

        clicar(navegador, xpath_confirmCopy)

                            # | ---------> Fluxo Principal <---------

navegador = webdriver.Chrome()

login_onvio(navegador)      # Chama a função que realiza o login no site
acessar_documentos(navegador)       # Chama a função que acessa a área de documentos do site 
mudar_aba(navegador, 1)     # Chama a função que muda a aba para continuar executando o código 
selecionar_empresa(navegador, "Empresa exemplo simples nacional")       # Chama a função que procura a empresa e a acessa
acessar_setorPessoal(navegador)     # Chama a função que acessa o setor pessoal da empresa atualmente acessada
criar_pasta_seNãoExistir(navegador, ano_atual)
acessar_setorPessoal(navegador)






time.sleep(10)
