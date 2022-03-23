#############################################################################
# Nome: Aula 20 (Laboratório) - Manipulação de Strings
# Autor: Rafael Machado                                               
# Data: 20/10/2021                                                    
# Resumo: Tarefa sobre Manipulação de Strings
#############################################################################

##############
# Exercício 1
# Resumo: 
def contaPalavras(frase):
    palavras = frase.split(" ")
    return len(palavras)

##############
# Exercício 2
# Resumo: 
def criptCesar(palavra, deslocamento):
    decodificada = []
    for n in range( len(palavra) ):
        decodificada.append ( ord(palavra[n]) )
    codificada = []
    for letra in decodificada:
        if deslocamento <0:
            for n in range( -deslocamento ):
                if 122 >= letra >= 97:
                    letra -= 32
                if letra == 65:
                    letra = 90
                elif 90 >= letra >= 65:
                    letra -= 1
                
            codificada.append(chr(letra))
        if deslocamento >0:
            for n in range( deslocamento ):
                if 122 >= letra >= 97:
                    letra -= 32
                if letra == 90:
                    letra = 65
                elif 90 >= letra >= 65:
                    letra += 1
                    
            codificada.append(chr(letra))
    print ("".join(codificada))

##############
# Exercício 3
# Resumo: 
def nomeCitacao (nome_completo):
    nomes = nome_completo.split(" ")
    print("{0}, {1}".format ( nomes[-1], nomes[0] ) )

##############
# Exercício 4
# Resumo: 
def spellChecker(texto):
    #Ler o arquivo
    arquivo = open("words.txt","r")
    checker = []
    for i in arquivo.readlines():
        checker.append(i.lower().strip())
    arquivo.close()
    #Arrumar a lista com as palavras do texto inserido
    texto = texto.lower().replace(",", "").split(" ")
    #Ver se as palavras do texto existem no arquivo words
    erradas = []
    for palavra in texto:
        if palavra not in checker:
            erradas.append(palavra)
    return erradas

##############
# Exercício 5
# Resumo: Jogo da forca
p = input("Digite a palavra secreta:").lower()
palavra = list(p)
secreta = list("-"*len(p))
print("\n"*9)
print("".join(secreta))
forca = ["X==:==","X  :","X","X","X","X","==========="]
erros = 0
while True:
    chute = input("\nDigite uma letra:")
    if chute in palavra:
        for n in range (len(palavra)):
            if palavra[n] == chute:
                secreta[n] = chute
    else:
        print("Você errou!")
        erros += 1
        if erros == 1:
            forca[2] = "X  O"
        elif erros == 2:
            forca[3] = "X  |"
        elif erros == 3:
            forca[3] = "X \|"
        elif erros == 4:
            forca[3] = "X \|/"
        elif erros == 5:
            forca[4] = "X /"
        elif erros == 6:
            o = r"'X / \'"
            forca[4] = o.replace("'","")
    for linha in forca:
        print(linha)
    if erros == 6:
        print("Enforcado!")
        break
    print("".join(secreta))
    if secreta == palavra:
        print("Você acertou!")
        break