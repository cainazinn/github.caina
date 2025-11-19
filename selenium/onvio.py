from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import time


navegador = webdriver.Chrome()
print("Abriu o navegador")

navegador.get("https://onvio.com.br/#/login")
print("Acessou o site da onvio")

navegador.maximize_window()
print("Botou em tela cheia")


WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/main/div/onvio-login/div/div[1]/fieldset/div/div/section/form[3]/div/button")))
print("Esperou até o botão iniciar aparecer na tela")


entrar1 = navegador.find_element(By.XPATH, "/html/body/div/div[1]/div/main/div/onvio-login/div/div[1]/fieldset/div/div/section/form[3]/div/button")
print("Botão de entrar encontrado.")

entrar1.click()
print("Botão de entrar clicado")


WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input")))
print("Esperou até a caixa de email aparecer na tela")


caixa_email = navegador.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input")
print("Caixa de email encontrada na tela de login")

caixa_email.send_keys("cainacavalcante352@gmail.com")
print("Caixa de email preenchida")


time.sleep(2)


entrar2 = navegador.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/div[1]/div/form/div[2]/button")
print("Botão de entrar encontrado")

entrar2.click()
print("Botão de entrar clicado")


WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/form/div[1]/div/div[2]/div/input")))
print("Esperou a caixa de senha aparecer na tela")


caixa_senha = navegador.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/form/div[1]/div/div[2]/div/input")
print("Caixa de senha encontrada")

caixa_senha.send_keys("Ca090708!!")
print("Caixa de senha preenchida")


time.sleep(2)


entrar3 = navegador.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/form/div[2]/button")
print("Botão de entrar encontrado") 

entrar3.click()
print("Botão de entrar clicado")


WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/bm-optional-header/bm-staff-custom-header/bm-header/header/ul[2]/li[2]/li/a/i")))
print("Esperou até o botão de documentos aparecer")


documentos = navegador.find_element(By.XPATH, "/html/body/bm-optional-header/bm-staff-custom-header/bm-header/header/ul[2]/li[2]/li/a/i")
print("Botão de documentos encontrado")

documentos.click()
print("Botão de documentos clicado")


abas = navegador.window_handles
print("Retorna uma lista com os ids das abas")

navegador.switch_to.window(abas[1])
print("Navegador mudou para a segunda aba")


WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[1]/div/div[1]/navbar-left/dms-clients-combobox/div/div[2]/div[1]/div[2]/i")))
print("Esperou até a caixa de procurar empresas aparecer na tela")


procurar_empresa = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[1]/div/div[1]/navbar-left/dms-clients-combobox/div/div[2]/div[1]/input")
print("Caixa de procurar empresas encontrada")

procurar_empresa.send_keys("9999")
print("Caixa de procurar empresas preenchida")


time.sleep(5)


empresa_desejada = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[1]/div/div[1]/navbar-left/dms-clients-combobox/div/div[2]/div[2]/div/ul/li[1]/bento-combobox-row-template/span[2]")
print("Empresa desejada encontrada")

empresa_desejada.click()
print("Clicou na empresa desejada")


WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-storage-grid/div/div/div[9]/div[2]/div[1]/div[7]/div[3]/div/div/dms-grid-text-cell/div/span[1]/a")))
print("Esperou até o link do setor pessoal aparecer")


setor_pessoal = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-storage-grid/div/div/div[9]/div[2]/div[1]/div[7]/div[3]/div/div/dms-grid-text-cell/div/span[1]/a")
print("Link do setor pessoal encontrado")

setor_pessoal.click()
print("Setor pessoal acessado")


time.sleep(2)


criar_novo = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[1]/a")
print("Botão de criar novo encontrado")

criar_novo.click()
print("Botão de criar novo clicado")


time.sleep(2)


botao_nova_pasta = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[1]/ul/li[1]/a")
print("Botão de criar nova pasta encontrado")

botao_nova_pasta.click()
print("Botão de criar nova pasta clicado")


WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/div[1]/input")))
print("Esperou caixa de nomear nova pasta aparecer")


nomear_nova_pasta = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/div[1]/input")
print("Caixa de nomear nova pasta encontrada")

nomear_nova_pasta.send_keys("2026")
print("Pasta nomeada")


time.sleep(2)


salvar_nova_pasta = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/button[1]")
print("Botão de salvar nova pasta encontrada")

salvar_nova_pasta.click()
print("Nova pasta salva")


time.sleep(2)


copiar_pasta = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[4]/div/div[3]/div/div/i")
print("Botão de copiar pasta encontrado")

copiar_pasta.click()
print("Botão de copiar pasta clicado")


time.sleep(2)


selecionar_nova_pasta = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/ul/li[3]/span[2]")
print("Botão selecionar nova pasta encontrado")

selecionar_nova_pasta.click()
print("Botão selecionar nova pasta clicado")


time.sleep(2)


botao_copiar = navegador.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/button[1]")
print("Botão copiar encontrado")

botao_copiar.click()
print("Botão copiar clicado")

time.sleep(3)




# selecionar_pasta = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[4]/div/div[3]/div/div/i")
# print("Botão de selecionar pasta encontrado")

# selecionar_pasta.click()
# print("Pasta selecionada")


# time.sleep(2)


# gerenciar_pasta = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[4]/a")
# print("Botão de gerenciar encontrado")

# gerenciar_pasta.click()
# print("Botão de gerenciar clicado")


# time.sleep(2)


# copiar_pasta = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[4]/ul/li[4]/a")
# print("Botão de copiar pasta encontrado")

# copiar_pasta.click()
# print("Pasta copiada")


# WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/button[1]")))
# print("Esperou até o botão de confirmação para copiar aparecer")


# confirm_copiar = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/button[1]")
# print("Botão de coonfirmação para copiar encontrado")

# confirm_copiar.click()


# time.sleep(10)


