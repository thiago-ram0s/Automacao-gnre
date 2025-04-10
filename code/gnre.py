import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time


driver = None
primeira_execucao = True


def iniciar_driver():
    global driver
    if driver is None:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.gnre.pe.gov.br:444/gnre/v/guia/index")
        driver.maximize_window()
        time.sleep(2)

def preencher_gnre():
    global driver, primeira_execucao

    numero_nota = entry_nota.get()
    valor_principal = entry_valor.get()

    if not numero_nota or not valor_principal:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
        return

    iniciar_driver() 

    data_atual = datetime.now().strftime("%d/%m/%Y")

    if not primeira_execucao:
        try:
            driver.find_element(By.ID, "novaGuia").click()
            time.sleep(1)
            driver.refresh()
            time.sleep(2)
        except:
            driver.get("https://www.gnre.pe.gov.br:444/gnre/v/guia/index")
            time.sleep(2)

    # Seleciona dados
    uf = Select(driver.find_element(By.ID, "ufFavorecida"))
    uf.select_by_value('PR')

    driver.find_element(By.ID, "optGnreSimples").click()
    driver.find_element(By.ID, "optNaoInscrito").click()
    driver.find_element(By.ID, "tipoCNPJ").click()
    driver.find_element(By.ID, "documentoEmitente").clear()
    driver.find_element(By.ID, "documentoEmitente").send_keys("65391791000173")
    driver.find_element(By.ID, "razaoSocialEmitente").clear()
    driver.find_element(By.ID, "razaoSocialEmitente").send_keys("Carlos Eduardo e Luana Advocacia ME")
    driver.find_element(By.ID, "enderecoEmitente").clear()
    driver.find_element(By.ID, "enderecoEmitente").send_keys("Rua Mar Vermelho")

    uf_emitente = Select(driver.find_element(By.ID, "ufEmitente"))
    uf_emitente.select_by_value('SC')
    mun_emitente = Select(driver.find_element(By.ID, "municipioEmitente"))
    mun_emitente.select_by_value('02404')

    driver.find_element(By.ID, "cepEmitente").clear()
    driver.find_element(By.ID, "cepEmitente").send_keys("89040-490")
    driver.find_element(By.ID, "telefoneEmitente").clear()
    driver.find_element(By.ID, "telefoneEmitente").send_keys("47981466367")

    tp_receita = Select(driver.find_element(By.ID, "receita"))
    tp_receita.select_by_value("100099")

    sel_nota_fiscal = Select(driver.find_element(By.ID , "tipoDocOrigem"))
    sel_nota_fiscal.select_by_value("10")
    driver.find_element(By.ID , "numeroDocumentoOrigem").clear()
    driver.find_element(By.ID , "numeroDocumentoOrigem").send_keys(numero_nota)
    driver.find_element(By.ID, "dataVencimento").clear()
    driver.find_element(By.ID, "dataVencimento").send_keys(data_atual)
    driver.find_element(By.ID ,"valor").clear()
    driver.find_element(By.ID ,"valor").send_keys(valor_principal)
    driver.find_element(By.ID , "campoAdicional00").clear()
    driver.find_element(By.ID , "campoAdicional00").send_keys("CONFORME A NOTA FISCAL N " + numero_nota)

    driver.find_element(By.ID , "validar").click()

    messagebox.showinfo("Concluído", "Formulário preenchido com sucesso!")

    entry_nota.delete(0, tk.END)
    entry_valor.delete(0, tk.END)

    primeira_execucao = False


janela = tk.Tk()
janela.title("Preenchimento GNRE")
janela.geometry("400x250")
janela.attributes("-topmost", True)
janela.after(6000, lambda: janela.attributes("-topmost", False)) 

tk.Label(janela, text="Número da Nota Fiscal:").pack(pady=5)
entry_nota = tk.Entry(janela, width=40)
entry_nota.pack()

tk.Label(janela, text="Valor Principal:").pack(pady=5)
entry_valor = tk.Entry(janela, width=40)
entry_valor.pack()

tk.Button(janela, text="Preencher GNRE", command=preencher_gnre, bg="#4CAF50", fg="white").pack(pady=20)

janela.mainloop()
