#############################################################################
# Nome: Aula 23 (Teoria) - Dicionários
# Autor: Rafael Machado                                               
# Data: 27/10/2021                                                    
# Resumo: Exercícios sobre Dicionários
#############################################################################

##############
# Exercício 1
# Resumo: 
def procuraReversa (dicionario, valor):
    chaves = []
    for chave, value in dicionario.items():
        if valor == value:
            chaves.append (chave)
    return chaves
dicionario = {1 : "sim",
2 : "nao",
3 : "sim",
4 : "nao"
}
procurar = "talvez"
print( procuraReversa(dicionario, procurar) )

##############
# Exercício 2
# Resumo: 
import random
def GerarDados ():
    valor = random.randint(1, 6) + random.randint(1, 6)
    return valor
def milDados ():
    dados = {}
    for n in range (1, 1001):
        dados[n] = GerarDados()
    tabela = {}
    for n in range (2, 13):
        contador = 0
        for valor in dados.values():
            if valor == n:
                contador += 1
        tabela[n] = str(round(contador/11)) + "%"
    return tabela
print( milDados() )

##############
# Exercício 3
# Resumo: 
def Unicos (string):
    letras = {}
    for n in string:
        letras[n] = n
    return len( letras )
string = "Hello, World!"
print ("A string apresenta %s caracteres únicos!" % Unicos(string))

##############
# Exercício 4
# Resumo: 
def keys (palavra):
    dicionario = {}
    for letra in palavra:
        if letra in dicionario.keys():
            dicionario[letra] = dicionario[letra]+1
        else:
            dicionario[letra] = 1
    return dicionario
def verificar (palavra1, palavra2):
    palavra = keys(palavra1)
    anagrama = keys(palavra2)
    if palavra == anagrama:
        print("A palavra é um anagrama!")
    else:
        print("A palavra não é um anagrama!")
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
verificar(palavra1, palavra2)

##############
# Exercício 5
# Resumo: 
import random
def Gerar (menor, maior):
    lista = []
    while len(lista) <= 5:
        novo = random.randint(menor, maior)
        if novo not in lista:
            lista.append( novo )
    return lista
def criarCartao ():
    cartao = {}
    cartao["B"] = Gerar(1, 15)
    cartao["I"] = Gerar(16, 30)
    cartao["N"] = Gerar(31, 45)
    cartao["G"] = Gerar(46, 60)
    cartao["O"] = Gerar(61, 75)
    return cartao
def exibirCartao ():
    cartao = criarCartao()
    for chave in cartao:
        print ("  %s  " %chave, end="")
    print("")
    for n in range (5):
        for valor in cartao.values():
            print(" %2s  " %valor[n], end="")
        print("")
exibirCartao()