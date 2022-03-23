#############################################################################
# Nome: Aula 22 (Laboratório) - Módulos
# Autor: Rafael Machado                                               
# Data: 22/10/2021                                                    
# Resumo: Tarefa sobre Módulos
#############################################################################

##############
# Exercício 1
# Resumo: 
import random
def criarLetras ():
    letras = []
    for n in range (4):
        letras.append (chr (random.randint(65,90)) )
    return letras
def criarNumeros ():
    numeros = []
    for n in range (3):
        numeros.append (str( random.randint(0, 9) ))
    return numeros
def arrumarPlaca (letras, numeros):
    placa = letras[0] + letras[1] + letras[2] + numeros[0] + letras[3] + numeros[1] + numeros[2]
    return placa
##############
# Exercício 2
# Resumo: 
def crivo (limite):
    primos = [0, 0]
    for n in range(2, limite+1):
        primos.append(n)
    for numero in range( len(primos) ):
        if primos[numero] != 0:
            for teste in range( len(primos) ):
                if primos[numero] != primos[teste] and primos[teste] != 0 and primos[teste] % primos[numero] == 0:
                    primos[teste] = 0
    return primos
##############
# Exercício 3
# Resumo: 
def remover (arquivo):
    arquivo = open(arquivo, "r")
    lista = arquivo.readlines()
    del lista[0]
    for n in range ( len(lista) ):
        lista[n] = lista[n].split(",")
    n = 0
    while n < len(lista):
        if lista[n][3] != "ball":
            del lista[n]
            n -= 1
        n += 1
    for n in range ( len(lista) ):
        del lista[n][2]
        del lista[n][1]
    for n in range ( len(lista) ):
        lista[n] = lista[n][0] + "," + lista[n][1] + "," + lista[n][2] + "," + lista[n][3] + "," + lista[n][4] + "," + lista[n][5]
        print(lista[n])
##############
# Exercício 4
# Resumo: 
def ordenar (palavras):
    palavras = sorted(palavras.split("-"))
    n_palavras = ""
    for n in range ( len(palavras) ):
        if n == len(palavras) - 1:
            n_palavras = n_palavras + str(palavras[n])
        else:
            n_palavras = n_palavras + str(palavras[n]) + "-"
    return n_palavras
def calcular (palavras):
    palavras = palavras.replace("-", "")
    minusculas = 0
    maiusculas = 0
    for n in range ( len(palavras) ):
        if palavras[n].isupper():
            maiusculas += 1
        else:
            minusculas += 1
    print(maiusculas)
    print(minusculas)