#############################################################################
# Nome: Aula 16 (Laboratório) - Arquivos
# Autor: Rafael Machado                                               
# Data: 01/10/2021                                                    
# Resumo: Tarefa sobre Arquivos
#############################################################################

##############
# Exercício 1
# Resumo: 
def read_file ():
    arquivo = open("poema.txt","r")
    lista = arquivo.readlines()
    for n in range ( len(lista) ):
        print( lista[n].strip() )
    arquivo.close()

##############
# Exercício 2
# Resumo: 
def conta_palavras ():
    #ler o arquivo
    arquivo = open("palavras.txt","r")
    lista = arquivo.readlines()
    arquivo.close()
    #contar quantas palavras tem no arquivo
    palavras = []
    contador = 0
    for linha in range ( len(lista) ):
        palavras.append (lista[linha].split())
    for linha in range ( len(palavras) ):
        for palavra in range ( len(palavras[linha]) ):
            contador += 1
    print ("Quantidade de palavras:  %d" % contador )

##############
# Exercício 3
# Resumo: 
def lista_arquivo (palavras):
    #escrever no arquivo
    arquivo = open("arquivo.txt","w")
    for n in range ( len(palavras) ):
        arquivo.write ("%s\n" % palavras[n] )
    arquivo.close()
    #ler o que foi escrito no arquivo
    arquivo = open("arquivo.txt","r")
    lista = arquivo.readlines()
    for n in range ( len(lista) ):
        print (lista[n], end="")
    arquivo.close()

##############
# Exercício 4
# Resumo: 
def acha_palavra (busca):
    #ler o arquivo
    arquivo = open("busca.txt", "r")
    lista = arquivo.readlines()
    arquivo.close()
    #contar quantas vezes a palavra aparece no arquivo
    palavras = []
    contador = 0
    for linha in range ( len(lista) ):
        palavras.append (lista[linha].split())
    for linha in range ( len(palavras) ):
        for palavra in range ( len(palavras[linha]) ):
            if palavras[linha][palavra] == busca:
                contador += 1
    print(contador)

##############
# Exercício 5
# Resumo: 
def ao_quadrado() :
    #ler o arquivo
    arquivo = open("quadrado.txt","r")
    lista = arquivo.readlines()
    arquivo.close()
    #calcular o quadrado de cada número
    quadrado = []
    for n in range ( len(lista) ):
        quadrado.append ( int(lista[n])**2 )
    print(quadrado)

##############
# Exercício 6
# Resumo: 
def line_count():
    #ler o arquivo
    arquivo = open("story.txt", "r")
    lista = arquivo.readlines()
    arquivo.close()
    #contar quantas linhas não começam com "E"
    contador = 0
    for linha in range ( len(lista) ):
        if lista[linha][0] != "E":
            contador += 1
    print( "Numero de linhas que nao comecam com 'E'= %d" % contador )