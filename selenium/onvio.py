from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import TimeoutException
import time
import pyautogui


ano_atual = datetime.now().year
print(ano_atual)


# ===============================================
#                                               |
# Fase 1: Acessar o site da Onvio e fazer login |
#                                               |    
# ===============================================


# Abre o navegador
navegador = webdriver.Chrome()
print("Abriu o navegador")

# Acessa o site da Onvio
navegador.get("https://onvio.com.br/#/login")
print("Acessou o site da onvio")

# Coloca a janela em tela cheia
navegador.maximize_window()
print("Botou em tela cheia")


# Pede ao navegador que espere até 10 segundos até que tal elemento esteja presente e clicável na tela (nesse caso o botão de entrar)
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "  /html/body/div/div[1]/div/main/div/onvio-login/div/div[1]/fieldset/div/div/section/form[3]/div/button")))
print("Esperou até o botão de entrar aparecer na tela")


# Procura o botão de entrar até encontrá-lo
entrar1 = navegador.find_element(By.XPATH, "/html/body/div/div[1]/div/main/div/onvio-login/div/div[1]/fieldset/div/div/section/form[3]/div/button")
print("Botão de entrar encontrado.")

# Clica no botão de entrar assim que ele se encontra presente na tela
entrar1.click()
print("Botão de entrar clicado")


# Espera até que a caixa de inserir o email esteja presente na tela
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input")))
print("Esperou até a caixa de email aparecer na tela")


# Procura a caixa de inserir o email até encontrá-la
caixa_email = navegador.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input")
print("Caixa de email encontrada na tela de login")

# Preenche a caixa de inserir o email com o email especificado (cainacavalcante352@gmail.com)
caixa_email.send_keys("cainacavalcante352@gmail.com")
print("Caixa de email preenchida")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de entrar até encontrá-lo
entrar2 = navegador.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/div[1]/div/form/div[2]/button")
print("Botão de entrar encontrado")

# Clica no botão de entrar assim que ele é encontrado
entrar2.click()
print("Botão de entrar clicado")


# Espera até que a caixa de inserir a senha esteja presente na tela
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/form/div[1]/div/div[2]/div/input")))
print("Esperou a caixa de senha aparecer na tela")


# Procura a caixa de inserir a senha até encontrá-la
caixa_senha = navegador.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/form/div[1]/div/div[2]/div/input")
print("Caixa de senha encontrada")

# Preenche a caixa de senha, assim que é encontrada, com a senha especificada (Ca090708!!) 
caixa_senha.send_keys("Ca090708!!")
print("Caixa de senha preenchida")


# Espera 2 segundos 
time.sleep(2)


# Procura o botão de entrar até encontrá-lo
entrar3 = navegador.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/section/div/div/div/form/div[2]/button")
print("Botão de entrar encontrado") 

# Clica no botão de entrar assim que ele é encontrado
entrar3.click()
print("Botão de entrar clicado")


# ======================================================================================
#                                                                                      |
# Fase 2: Acessar os documentos, acessar a empresa e o setor pessoal dela              |
#                                                                                      |    
# ======================================================================================



# Espera até que o botão de acessar os documentos esteja presente na tela
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/bm-optional-header/bm-staff-custom-header/bm-header/header/ul[2]/li[2]/li/a/i")))
print("Esperou até o botão de documentos aparecer")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de acessar os documentos até encontrá-lo
documentos = navegador.find_element(By.XPATH, "/html/body/bm-optional-header/bm-staff-custom-header/bm-header/header/ul[2]/li[2]/li/a/i")
print("Botão de documentos encontrado")

# Clica no botão de acessar os documentos assim que ele é encontrado
documentos.click()
print("Botão de documentos clicado")

# Lista as abas do navegador
abas = navegador.window_handles
print("Retorna uma lista com os ids das abas")

# Informa ao navegador que para continuar o código ele primeiro deve mudar para a segunda aba
navegador.switch_to.window(abas[1])
print("Navegador mudou para a segunda aba")


# Espera até que a caixa de procurar empresas esteja presente na tela
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[1]/div/div[1]/navbar-left/dms-clients-combobox/div/div[2]/div[1]/div[2]/i")))
print("Esperou até a caixa de procurar empresas aparecer na tela")


# Espera 2 segundos
time.sleep(2)


# Procura a caixa de procurar empresas até encontrá-la
procurar_empresa = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[1]/div/div[1]/navbar-left/dms-clients-combobox/div/div[2]/div[1]/input")
print("Caixa de procurar empresas encontrada")

# Preenche a caixa de procurar empresas, assim que é encontrada, com o código da empresa especificado (9999) 
procurar_empresa.send_keys("9999")
print("Caixa de procurar empresas preenchida")


# Espera 5 segundos 
time.sleep(3)


# Procura o campo referente a empresa desejada até encontrá-la
empresa_desejada = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[1]/div/div[1]/navbar-left/dms-clients-combobox/div/div[2]/div[2]/div/ul/li[1]/bento-combobox-row-template/span[2]")
print("Empresa desejada encontrada")

# Seleciona a empresa desejada assim que ela é encontrada
empresa_desejada.click()
print("Clicou na empresa desejada")


# Espera até que o link referente ao setor pessoal da empresa desejada esteja presente na tela
WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-storage-grid/div/div/div[9]/div[2]/div[1]/div[7]/div[3]/div/div/dms-grid-text-cell/div/span[1]/a")))
print("Esperou até o link do setor pessoal aparecer")


# Espera 2 segundos
time.sleep(2)


# Procura o link referente ao setor pessoal da empresa desejada até encontrá-lo
setor_pessoal = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-storage-grid/div/div/div[9]/div[2]/div[1]/div[7]/div[3]/div/div/dms-grid-text-cell/div/span[1]/a")
print("Link do setor pessoal encontrado")

# Clica no link referente ao setor pessoal assim que é encontrado
setor_pessoal.click()
print("Setor pessoal acessado")


# Espera 2 segundos
time.sleep(5)


# ===================================================================================
#                                                                                   |
# Fase 3: Criar uma nova pasta referente ao ano de 2026 no setor pessoal da empresa |
#                                                                                   |    
# ===================================================================================


# Procura o botão de criar novo até encontrá-lo
criar_novo = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[1]/a")
print("Botão de criar novo encontrado")

# Clica no botão de criar novo assim que ele é encontrado
criar_novo.click()
print("Botão de criar novo clicado")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de criar nova pasta até encontrá-lo
botao_nova_pasta = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[1]/ul/li[1]/a")
print("Botão de criar nova pasta encontrado")

# Clica no botão de criar nova pasta assim que ele é encontrado
botao_nova_pasta.click()
print("Botão de criar nova pasta clicado")


# Espera até que a caixa de nomear a nova pasta esteja presente na tela
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/div[1]/input")))
print("Esperou caixa de nomear nova pasta aparecer")


# Procura a caixa de nomear a nova pasta até encontrá-la
nomear_nova_pasta = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/div[1]/input")
print("Caixa de nomear nova pasta encontrada")

# Preenche a caixa de nomear nova pasta, assim que é encontrada, com o nome especificado (2026)
nomear_nova_pasta.send_keys("2026")
print("Pasta nomeada")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de salvar nova pasta até encontrá-lo 
salvar_nova_pasta = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/button[1]")
print("Botão de salvar nova pasta encontrada")


# Clica no botão de salvar nova pasta assim que ele é encontrado
salvar_nova_pasta.click()
print("Nova pasta salva")


# Espera até que o botão de acessar a pasta 2025 esteja clicável na tela
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[2]/div[1]/div[3]/div[2]/div/span/dms-grid-text-cell/div/span[1]/a")))


# Espera 3 segundos
time.sleep(3)


# Procura a pasta 2025 e a acessa
pasta_2025 = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[2]/div[1]/div[3]/div[2]/div/span/dms-grid-text-cell/div/span[1]/a")
print("Pasta 2025 encontrada")

# Acessa a pasta 2025 assim que é encontrada
pasta_2025.click()
print("Pasta 2025 acessada")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de selecionar a subpasta "folha de pagamento" até encontrá-lo
subpasta_folhaPagamento2025 = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[4]/div/div[2]/div/div/i")
print("Botão de selecionar a subpasta folha de pagamento encontrado")

# Clica no botão de selecionar a subpasta "folha de pagamento" assim que é encontrado
subpasta_folhaPagamento2025.click()
print("Subpasta 'folha de pagamento' selecionada")

# Procura o botão de selecionar a subpasta "adiantamento" até encontrá-lo
subpasta_adiantamento2025 = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[4]/div/div[1]/div/div/i")
print("Botão de selecionar a subpasta 'adiantamento' encontrado")

# Clica no botão de selecionar a subpasta "adiantamento" assim que é encontrado
subpasta_adiantamento2025.click()
print("Subpasta 'adiantamento' selecionada")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de gerenciar pasta até encontrá-lo
gerenc_pasta = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[4]/a")
print("Botão de gerenciar a pasta encontrado")


# Clica no botão de gerenciar pasta assim que é encontrado
gerenc_pasta.click()
print(" Botão de gerenciar a pasta clicado")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de copiar até encontrá-lo
copiar_subpastas = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[4]/ul/li[4]/a")
print("Botão de copiar subpastas encontrado")


# CLica no botão de copiar assim que é encontrado
copiar_subpastas.click()
print("Botão de copiar subpastas clicado")


# Espera até que o botão de voltar na área de 'copiar para' esteja presente na tela
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/div/span[1]")))


# Espera 2 segundos
time.sleep(2)


# Na área de "copiar para" procura o botão de voltar para o setor pessoal até encontrá-lo
voltar_copiarPara = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/div/span[1]")
print("Botão de voltar na área de 'copiar para' encontrado")

# Clica no botão de voltar na área de 'copiar para' assim que é encontrado
voltar_copiarPara.click()
print("Botão de voltar na área de 'copiar para' clicado")


# Espera até que o botão de selecionar a pasta 2026 na área de 'copiar para' esteja presente na tela
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/ul/li[3]")))


# Espera 2 segundos
time.sleep(2)


# Procura o botão que seleciona a pasta 2026 na área de 'copiar para' até encontrá-lo
selecPasta2026_copiarPara = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/ul/li[3]")
print("Botão de selecionar a pasta 2026 na área de 'copiar para' encontrado")


# Clica no botão de selecionar a pasta 2026 na área de 'copiar para' assim que é encontrado
selecPasta2026_copiarPara.click()
print("Botão de selecionar pasta 2026 na área de 'copiar para' clicado")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de confirmar para copiar até encontrá-lo
confirm_copiar = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/button[1]")
print("Botão de confirmar para copiar encontrado")

# Clica no botão de confirmar para copiar assim que é encontrado
confirm_copiar.click()
print("Subpastas copiadas para a pasta 2026")


# WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "")))


# Espera 3 segundos
time.sleep(3)

pyautogui.moveTo(145, 630)
pyautogui.click()



# Espera 3 segundos
time.sleep(3)

# Procura o botão de selecionar a pasta 2026 até encontrá-lo
selecPasta2026 = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/div/dms-document-grid/div/div/div[14]/div[4]/div/div[1]/div/div/i")
print("Botão de selecionar a pasta 2026 encontrado")

# Clica no botão de selecionar a pasta 2026 assim que ele é encontrado
selecPasta2026.click()
print("Pasta 2026 selecionada")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de gerenciar pasta até encontrá-lo
gerenc_pasta = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[4]/a")
print("Botão de gerenciar a pasta encontrado")


# Clica no botão de gerenciar pasta assim que é encontrado
gerenc_pasta.click()
print("Botão de gerenciar a pasta clicado")


# Espera 2 segundos
time.sleep(2)


# Procura o botão de copiar até encontrá-lo
copiar_pasta2026 = navegador.find_element(By.XPATH, "/html/body/bm-main/main/div[1]/ui-view/div[2]/div/div[2]/div/section/div/documents-detail-pane/div/dms-document-grid-toolbar/dms-toolbar/div/ul/li[4]/ul/li[4]/a")
print("Botão de copiar pasta encontrado")


# CLica no botão de copiar assim que é encontrado
copiar_pasta2026.click()
print("Botão de copiar pasta clicado")


# Espera 10 segundos
time.sleep(10)

