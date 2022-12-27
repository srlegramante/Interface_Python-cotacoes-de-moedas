import requests
from tkinter import *



def pegar_cotacoes():
    requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BitCoin: {cotacao_btc}
    '''

    texto_cotacoes["text"] = texto


janela = Tk()
janela.title("Cotações Atual das moedas")
janela.geometry("280x180")

texto_orientacao = Label(janela, text="Clique no botão para ver as cotações da moedas")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar Cotações Atuais", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2,  padx=10, pady=10)


janela.mainloop()

'''
Como criar um sistema com interface grafica

importar dependentes 

jogar os codigos para dentro de funções 

e criar a janela para alocar os botões, txt, etc...
'''