#############################################################################
# Nome: Aula 28 (Laboratório) - GUI
# Autor: Rafael Machado 
# Data: 19/11/2021
# Resumo: Exercícios sobre GUI
#############################################################################
from tkinter import *
import os
from random import randint
from datetime import date
# Janela
window = Tk()
window.title("Algoritimos")
window.geometry("900x600")

# Labels
# ID #
usrID = Label(window, text = "ID: ", font = ("Arial", 14))
usrID.place (relx = 0.5, rely = 0.08, anchor = E)
# Nome #
nome = Label(window, text = "Nome: ", font = ("Arial", 14))
nome.place (relx = 0.5, rely = 0.16, anchor = E)
# Data de Nascimento #
nascimento = Label(window, text = "Data de Nascimento: ", font = ("Arial", 14))
nascimento.place (relx = 0.5, rely = 0.24, anchor = E)
# Endereço #
endereco = Label(window, text = "Endereço: ", font = ("Arial", 14))
endereco.place (relx = 0.5, rely = 0.32, anchor = E)
# Profissão #
profissao = Label(window, text = "Profissão: ", font = ("Arial", 14))
profissao.place (relx = 0.5, rely = 0.40, anchor = E)
# Retorno #
retorno = Label(window, text = "", font = ("Arial", 14))
retorno.place (relx = 0.55, rely = 0.56, anchor = CENTER)

# Entradas
# ID #
EntradaID = Entry(window, width = 15, font = ("Arial", 14), justify = CENTER, state = DISABLED)
EntradaID.place(relx = 0.5, rely = 0.08, anchor = W)
# Nome #
nomeEntrada = Entry(window, width = 15, font = ("Arial", 14), justify = CENTER)
nomeEntrada.place(relx = 0.5, rely = 0.16, anchor = W)
# Data de Nascimento #
def digitarDia(*args):
    s = dia.get()
    if len(s) > 0:
        if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
            dia.set(s[:-1])
        else: # aproveitar apenas os primeiros 5 chars
            dia.set(s[:2])
dia = StringVar()
dia.trace("w", digitarDia )
nascimentoDia = Entry(window, width = 5, font = ("Arial", 14), textvariable=dia, justify = CENTER)
nascimentoDia.place(relx = 0.5, rely = 0.24, anchor = W)
#
def digitarMes(*args):
    s = mes.get()
    if len(s) > 0:
        if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
            mes.set(s[:-1])
        else: # aproveitar apenas os primeiros 5 chars
            mes.set(s[:2])
mes = StringVar()
mes.trace("w", digitarMes )
nascimentoMes = Entry(window, width = 5, font = ("Arial", 14), textvariable=mes, justify = CENTER)
nascimentoMes.place(relx = 0.57, rely = 0.24, anchor = W)
#
def digitarAno(*args):
    s = ano.get()
    if len(s) > 0:
        if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
            ano.set(s[:-1])
        else: # aproveitar apenas os primeiros 5 chars
            ano.set(s[:4])
ano = StringVar()
ano.trace("w", digitarAno )
nascimentoAno = Entry(window, width = 5, font = ("Arial", 14), textvariable=ano, justify = CENTER)
nascimentoAno.place(relx = 0.64, rely = 0.24, anchor = W)
# Endereço #
enderecoEntrada = Entry(window, width = 15, font = ("Arial", 14), justify = CENTER)
enderecoEntrada.place(relx = 0.5, rely = 0.32, anchor = W)
# Profissão #
profissaoEntrada = Entry(window, width = 15, font = ("Arial", 14), justify = CENTER)
profissaoEntrada.place(relx = 0.5, rely = 0.40, anchor = W)

# Funções
def retornar (texto):
    retorno["text"] = texto
def criarID ():
    userID = str( randint(0, 9) )
    for n in range (4):
        userID += str( randint(0, 9) )
    return userID
def definirIdade ():
    # Pegar a data atual
    data = date.today() # Pega a data e hora
    data = data.strftime(r"%d-%m-%Y")
    data = data.split("-")
    # Pegar data de nascimento
    ano = nascimentoAno.get()
    mes = nascimentoMes.get()
    dia = nascimentoDia.get()
    # Resto da função para encontrar a idade
    if dia != "" and mes != "" and ano != "":
        idade = ( int(data[2]) - int(ano) )
        if int(mes) > int(data[1]) or ( int(mes) == int(data[1]) and int(dia) > int(data[0]) ):
            idade -= 1
    else:
        idade = ""
    return ( idade, ( str(dia) + "/" + str(mes) + "/" + str(ano) ) )
def mostrarID (userID):
    EntradaID["state"] = NORMAL
    EntradaID.insert(0, userID)
    EntradaID["state"] = DISABLED 
def verificarDuplicata (infos):
    novoArquivo = []
    for item in infos.keys():
        novoArquivo.append( item + ": " + str(infos[item]) + "\n" )
    # Ler cada arquivo da pasta users para ver se não existe nenhum igual
    os.chdir("./users/")
    repetido = False
    for file in os.listdir():
        arq = open( file , "r")
        arquivo = arq.readlines()
        arq.close()
        if arquivo == novoArquivo:
            repetido = True
            break
    os.chdir("..")
    return repetido
def criarUsuario ():
    # Apagar o campo ID
    EntradaID["state"] = NORMAL
    EntradaID.delete(0, END)
    EntradaID["state"] = DISABLED 
    # Pegar os valores das entradas
    idade,nascimento = definirIdade()
    nome = nomeEntrada.get()
    endereco = enderecoEntrada.get()
    profissao = profissaoEntrada.get()
    if profissao  == "" or endereco  == "" or nome  == "" or idade  == "" or nascimento == "":
        retornar("Preencha todas as informações!")
    else:
        infos = {
            "Nome" : nome, 
            "Data de Nascimento" : nascimento, 
            "Idade" : idade, 
            "Endereço" : endereco, 
            "Profissão" : profissao
            }
        # Criar ID único para cada usuário
        while True:
            userID = criarID()
            if os.path.isfile("./users/" + userID + ".txt"):
                pass
            else:
                break
        # Checar por duplicatas e se não existir nenhuma cria o novo usuário
        repetido = verificarDuplicata(infos)
        if repetido:
            retornar("Usuário Repetido!")
        else:
            mostrarID(userID)
            arquivo = open("./users/" + userID + ".txt", "w")
            for item in infos.keys():
                arquivo.write( item + ": " + str(infos[item]) + "\n" )
            arquivo.close()
            retornar("Usuário Cadastrado com Sucesso!")

# Botão
pesquisar = Button(window, text = "Pesquisar", command = criarUsuario)
pesquisar.place(relx = 0.55, rely = 0.48, anchor = CENTER)

# Loop da Janela
window.mainloop()