#############################################################################
# Nome: Aula 26 (Laboratório) - GUI
# Autor: Rafael Machado                                               
# Data: 05/11/2021                                                    
# Resumo: Exercícios sobre GUI
#############################################################################
from tkinter import *
from tkinter import scrolledtext
from unidecode import unidecode
# Janela
window = Tk()
window.title("Algoritimos")
window.geometry("900x600")
# Labels
palavra = Label(window, text = "Palavra Suspeita: ", font = ("Arial", 14))
palavra.place (relx = 0.05, rely = 0.08)

quantidade = Label(window, text = "Frequência: ", font = ("Arial", 14))
quantidade.place(relx = 0.05, rely = 0.15)

quantidade = Label(window, text = "Ocorrências: ", font = ("Arial", 14))
quantidade.place(relx = 0.05, rely = 0.3)
# Scrolled text
txt = scrolledtext.ScrolledText(window, width = 100, height = 23, state = DISABLED)
txt.place(relx = 0.05, rely = 0.35)
# Entradas
palavraEntrada = Entry(window, width = 15, font = ("Arial", 14), justify = CENTER)
palavraEntrada.place(relx = 0.25, rely = 0.08)

frequencia = Entry(window, width = 15, font = ("Arial", 14), justify = CENTER, state = DISABLED)
frequencia.place(relx = 0.25, rely = 0.15)
# Botão
def buscaPalavras():
    # Abir o arquivo, ler o que tem nele e salvar na variavel linhas
    arquivo = open("chat.txt", "r", encoding = "utf-8")
    linhas = arquivo.readlines()
    arquivo.close()
    # 
    busca = unidecode( str(palavraEntrada.get()).lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "") )
    encontradas = []
    linhas_tratadas = linhas[::]
    # 
    vezes = 0
    for linha in range(len(linhas_tratadas)):
        linhas_tratadas[linha] = unidecode( linhas_tratadas[linha] ).lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace("(", "").replace(")", "").replace("/", "").split()
        for palavra in linhas_tratadas[linha]:
            if busca in palavra:
                if linha not in encontradas:
                    encontradas.append(linha)
                vezes += 1
    # Coloca as linhas na barra de scroll
    txt["state"] = NORMAL
    txt.delete(1.0, END)
    for item in encontradas:
        txt.insert(END, linhas[item])
    txt["state"] = DISABLED
    # Coloca a frequência
    frequencia["state"] = NORMAL
    frequencia.delete(0, END)
    frequencia.insert(0, vezes)
    frequencia["state"] = DISABLED 

pesquisar = Button(window, text = "Pesquisar", command = buscaPalavras)
pesquisar.place(relx = 0.5, rely = 0.08)
# Loop da Janela
window.mainloop()