#############################################################################
# Nome: Aula 21 (Teoria) - Módulos e Pacotes
# Autor: Rafael Machado                                               
# Data: 20/10/2021                                                    
# Resumo: Exercícios sobre Módulos e Pacotes
#############################################################################
import math
##############
# Exercício 1
# Resumo: 
def aptidao (sexo, peso):
    if sexo == "F" and peso >= 50:
        return True
    elif sexo == "M" and peso >= 60:
        return True
    else:
        return False
##############
# Exercício 2
# Resumo: 
def hipotenusa (cateto1, cateto2):
    return math.sqrt( (cateto1**2) + (cateto2**2) )
# Exercício 3
# Resumo: 
def corrigir (texto):
    #.
    texto = texto.replace(". ", ".").split(".")
    for frase in range (len(texto)):
        if frase == 0:
            texto[frase] = texto[frase].capitalize()
        else:
            texto[frase] = ". " + texto[frase].capitalize()
    texto = "".join(texto)
    #!
    texto = texto.replace("! ", "!").split("!")
    for frase in range (len(texto)):
        if frase == 0:
            texto[frase] = texto[frase]
        else:
            texto[frase] = "! " + texto[frase].capitalize()
    texto = "".join(texto)
    #?
    texto = texto.replace("? ", "?").split("?")
    for frase in range (len(texto)):
        if frase == 0:
            texto[frase] = texto[frase]
        else:
            texto[frase] = "? " + texto[frase].capitalize()
    texto = "".join(texto)
    return(texto)
# Exercício 4
# Resumo: 
def tamanho (senha):
    if len(senha) >= 8:
        return True
    else:
        return False
def maiuscula (senha):
    if senha.lower() == senha:
        return False
    else:
        return True
def minuscula (senha):
    if senha.upper() == senha:
        return False
    else:
        return True
def numero (senha):
        return any(char.isdigit() for char in senha)
# Exercício 5
# Resumo: 
def isInteger (string):
    if string.isdigit():
        return True
    elif (string[0] == "+" or string[0] == "-") and string[1:].isdigit():
        return True
    else:
        return False