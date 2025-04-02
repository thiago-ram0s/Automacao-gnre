from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from datetime import datetime
from PyInstaller.__main__ import _console_script_run
from PyInstaller import _recursion_too_deep_message
import PyInstaller.log


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.gnre.pe.gov.br:444/gnre/v/guia/index")

driver.maximize_window() #Utilizado para aumentar a tela

data_atual = datetime.now().strftime("%d/%m/%Y")
while True:
    time.sleep(2)
    uf = Select(driver.find_element(By.ID, "ufFavorecida"))

    uf.select_by_value('PR')  #Selecionar o UF desejado


    #   Selecione o tipo de GNRE desejado e comente os que não deseja utilizar

    gnre_simples = driver.find_element(By.ID, "optGnreSimples").click()
    # gnre_com_multiplas_Documentos_de_Origem = driver.find_element(By.ID, "optGnreMultDoc").click() 
    # gnre_com_multiplas_receitas = driver.find_element(By.ID, "optGnreMultRec").click()

    
    # Contribuinte Emitente (Responsável pelo Pagamento do Tributo
    # Inscrito UF Favorecida?

    #Se caso for inscrito, descomente as linhas abaixo e comente as linhas de não inscrito 65 ate 96

    #sim_inscrito = driver.find_element(By.ID, "optInscrito").click()
    #inscricao_estadual = driver.find_element(By.ID, "inscricaoEstadualEmitente")
    #inscricao = input("Digite a Inscrição Estadual: ")
    #inscricao_estadual.send_keys(inscricao)
    

    nao_inscrito = driver.find_element(By.ID, "optNaoInscrito").click()
    cnpj = driver.find_element(By.ID, "tipoCNPJ").click()

    Documento = driver.find_element(By.ID, "documentoEmitente")

    Documento.send_keys("65391791000173") #CNPJ da empresa

    RazaoSocial = driver.find_element(By.ID, "razaoSocialEmitente")
    RazaoSocial.send_keys("Carlos Eduardo e Luana Advocacia ME") #Razão Social da empresa

    Endereco = driver.find_element(By.ID, "enderecoEmitente")
    Endereco.send_keys("Rua Mar Vermelho") #Endereço da empresa

  

    UfEmitente = Select(driver.find_element(By.ID, "ufEmitente"))

    UfEmitente.select_by_value('SC') #Selecionar o UF desejado

    MunEmitente = Select(driver.find_element(By.ID, "municipioEmitente"))
    MunEmitente.select_by_value('02404') #Para saber o código do município, acesse o site do IBGE
    #https://www.ibge.gov.br/explica/codigos-dos-municipios.php

    #4202404 - Blumenau - SC 
    #02404 - Código do Município
    #42 - Código do Municípios de Santa Catarina

    CepEmitente = driver.find_element(By.ID, "cepEmitente")
    CepEmitente.send_keys("89040-490") #CEP da empresa

    telefoneEmitente =driver.find_element(By.ID, "telefoneEmitente")
    telefoneEmitente.send_keys("47981466367") #Telefone da empresa

    TpReceita = Select(driver.find_element(By.ID, "receita"))
    TpReceita.select_by_value("100099") #Código da Receita

    SelNotaFiscal = Select(driver.find_element(By.ID , "tipoDocOrigem"))
    SelNotaFiscal.select_by_value("10")

    NumeroNota = driver.find_element(By.ID , "numeroDocumentoOrigem")
    NumeroNota_value = input("Digite o Numeo do Documento de Origem: ")
    NumeroNota.send_keys(NumeroNota_value)
    
    DtVencimento = driver.find_element(By.ID, "dataVencimento")
    #Se caso quiser digitar a data de vencimento as duas linhas a baixo e comente a 112 ate 114
    #Vencimento = input("Digite a Data de Vencimento: ")
    #DtVencimento.send_keys(Vencimento)
    data_hoje =data_atual
    data_hoje = DtVencimento
    DtVencimento.send_keys(data_atual)

    
    VlPrincipal = driver.find_element(By.ID ,"valor")
    Valor = input ("Digite o Valor Principal: ")
    VlPrincipal.send_keys(Valor)

    InfoComplementares = driver.find_element(By.ID , "campoAdicional00")
    InfoComplementares.send_keys("CONFORME A NOTA FISCAL N " + NumeroNota_value)

    Validar =driver.find_element(By.ID , "validar").click()


    input("Pressione Enter para repetir o preenchimento ou Ctrl+C para sair...")
    novo = driver.find_element(By.ID, "novaGuia").click()
    driver.refresh()

driver.quit()





#pyinstaller --onefile gnre.py