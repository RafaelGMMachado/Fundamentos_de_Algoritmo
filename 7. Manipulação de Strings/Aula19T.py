#############################################################################
# Nome: Aula 19 (Teoria) - Manipulação de strings
# Autor: Rafael Machado                                               
# Data: 13/10/2021                                                    
# Resumo: Exercícios Sobre Manipulação de strings
#############################################################################

##############
# Exercício 1
# Resumo: Verifica se a palavra é um palíndromo
palavra = input("Digite a palavra: ").replace(" ", "").lower()
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo!")

##############
# Exercício 2
# Resumo: 
arquivo = open("Python.txt", "r", encoding="utf-8")
texto = arquivo.read()
arquivo.close()
palavras = texto.replace(",", "").replace(".", "").split()
tamanho = 0
for n in range ( len(palavras) ):
    if len(palavras[n]) > tamanho:
        contador = 1
        tamanho = len(palavras[n])
        palavra = palavras[n]
    elif len(palavras[n]) == tamanho and palavra != palavras[n]:
        contador += 1
print ("A palavra mais longa contém {0} caracteres\nApareceram {1} palavras desse comprimento!".format (tamanho, contador) )

##############
# Exercício 3
# Resumo: 

arquivo = open("Python.txt", "r", encoding="utf-8")
texto = arquivo.read()
arquivo.close()
palavras = texto.replace(",", "").replace(".", "").replace("!", "").lower().split()
maior = 0
for palavra in range ( len(palavras) ):
    contagem = palavras.count( palavras[palavra] )
    if contagem > maior:
        maior = contagem
        frequentes = [ palavras[palavra] ]
    elif contagem == maior and palavras[palavra] not in frequentes:
        frequentes.append( palavras[palavra] )
print("As palavras mais frequentes aparecem {0} vezes, elas são: {1}".format ( maior, ", ".join(frequentes) ) )

"""
#A parte do count pode ser substituída por 
    contagem = 0
    for ver_palavra in range ( len(palavras) ):
        if palavras[palavra] == palavras[ver_palavra]:
            contagem += 1
"""
##############
# Exercício 4
# Resumo: 
texto = input("Digite a linha que deseja traduzir para Pig Latin: ")
palavras = texto.replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower().split()
vogais = ["a", "e", "i", "o", "u", "é"]
n_palavras = []
for palavra in palavras:
    if palavra[0] in vogais:
        n_palavras.append (palavra+"way")
    elif palavra.isdecimal():
        n_palavras.append (palavra)
    else:
        for n in range( len(palavra) ):
            if palavra[n] in vogais:
                n_palavras.append ( palavra[n:] + palavra[:n] + "ay" )
                break
n_texto = texto.split()
pontuacao = [".", ",", "!", "?"]
for palavra in range( len(n_texto) ):
    if n_texto[palavra][-1] in pontuacao:
        n_texto[palavra] = n_palavras[palavra]+n_texto[palavra][-1]
    else:
        n_texto[palavra] = n_palavras[palavra]
print(*n_texto)