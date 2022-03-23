#############################################################################
# Nome: Aula 24 (Laboratório) - Dicionários
# Autor: Rafael Machado                                               
# Data: 03/11/2021                                                    
# Resumo: Exercícios sobre Dicionários
#############################################################################

##############
# Exercício 1
# Resumo: 
codigo_morse = {
'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---',
'3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'}
def converte(codigo_morse, palavra):
    palavra = palavra.upper().replace("!", "").replace(",", "").replace(".", "").replace(" ", "")
    texto_morse = []
    for letra in palavra:
        texto_morse.append(codigo_morse[letra])
    return " ".join(texto_morse)
palavra = "Hello World!!!"
print(converte(codigo_morse, palavra))

##############
# Exercício 2
# Resumo: 
def contaPalavras (frase):
    frase = frase.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").split()
    incidencias = {}
    for palavra in frase:
        if palavra in incidencias:
            incidencias[palavra] += 1
        else:
            incidencias[palavra] = 1
    return incidencias
frase = "Um teste, dois testes, mais testes, acabou?, SIM !!!"
print(contaPalavras(frase))

##############
# Exercício 3
# Resumo: 
centena = {
    "1" : "cento",
    "2" : "duzentos",
    "3" : "trezentos",
    "4" : "quatrocentos",
    "5" : "quinhentos",
    "6" : "seiscentos",
    "7" : "setecentos",
    "8" : "oitocentos",
    "9" : "novecentos"
}
dezena = {
    "1" : "dez",
    "2" : "vinte",
    "3" : "trinta",
    "4" : "quarenta",
    "5" : "cinquenta",
    "6" : "sessenta",
    "7" : "setenta",
    "8" : "oitenta",
    "9" : "noventa"
}
unidade = {
    "1" : "um",
    "2" : "dois",
    "3" : "três",
    "4" : "quatro",
    "5" : "cinco",
    "6" : "seis",
    "7" : "sete",
    "8" : "oito",
    "9" : "nove",
    "10" : "dez"
}
dez = {
    "1" : "onze",
    "2" : "doze",
    "3" : "treze",
    "4" : "quatorze",
    "5" : "quinze",
    "6" : "dezeseis",
    "7" : "dezesete",
    "8" : "dezoito",
    "9" : "dezenove"
}
def numero_texto (numero):
    if numero == 100:
        return "cem"
    elif 0 < numero <= 10:
        return unidade[str(numero)]
    else:
        texto = ""
        numero = [int(a) for a in str(numero)]
        if len(numero) == 3:
            texto = centena[str(numero[0])]
            numero.pop(0)
            if numero[0] != 0 or numero[1] != 0:
                texto += " e "
        if numero[0] == 1 and numero[1] != 0:
            texto += dez[str(numero[1])]
        else:
            if numero[0] != 0:
                texto += dezena[str(numero[0])]
                if numero[1] != 0:
                    texto += " e "
            if numero[1] != 0:
                texto += unidade[str(numero[1])]
        return texto
n = int(input("Digite um número entre 0 e 999: "))
print(numero_texto(n))