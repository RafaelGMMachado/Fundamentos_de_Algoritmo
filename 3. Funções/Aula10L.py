#############################################################################
# Nome: Aula 10 (Laboratório) - Funções   
# Autor: Rafael Machado                                               
# Data: 10/09/2021                                                    
# Resumo: Tarefa Sobre Funções
#############################################################################

##############
# Exercício 1
# Resumo: Calcula a hipotenusa de um triângulo
from math import *
l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
def hipotenusa(l1, l2):
    hipotenusa = sqrt(l1**2+l2**2)
    return hipotenusa
print("Hipotenusa: %.2f" % (hipotenusa(l1,l2)))

##############
# Exercício 2
# Resumo: Calcula a média entre 3 números
def media(a,b,c):
    return (a + b + c)/3

##############
# Exercício 3
# Resumo: 
def produtorio (a, b, c, d=1, e=1, f=1):
    return a*b*c*d*e*f

##############
# Exercício 4
# Resumo: Define todas as "datas mágicas" do século XX.
Km = float(input("Digite a quantidade de quilômetros: "))
def tarifa(Km):
    return 10.00 + (0.5 * (Km/0.125))
print("Tarifa %.2f" % tarifa(Km))

##############
# Exercício 5
# Resumo: Define o peso de uma pessoa em outros planetas do Sistema Solar
def Peso (planeta, peso):
    if planeta == "Mercúrio":
        return peso*0.37
    elif planeta == "Vênus":
        return peso*0.88
    elif planeta == "Marte":
        return peso*0.38
    elif planeta == "Júpiter":
        return peso*2.64
    elif planeta == "Saturno":
        return peso*1.15
    elif planeta == "Urano":
        return peso*1.17
    elif planeta == "Netuno":
        return peso*1.18
planeta = str(input("Digite o o nome do planeta desejado: "))
peso = float(input("Digite o peso da pessoa na Terra em kg: "))
print("Peso em {0}: {1:.2f}".format (planeta,Peso(planeta,peso)))

##############
# Exercício 6
# Resumo: Verifica se o número é primo ou não
def test_prime(a):
    vezes = 0
    for n in range (a):
        teste = a % (n+1)
        if teste == 0:
            vezes += 1
    if vezes == 2:
        return True
    else:
        return False

##############
# Exercício 7
# Resumo: 
from math import *

def dist(laA, laB, loA, loB):
    return (6371.01*acos(sin(laA)*sin(laB)+cos(laA)*cos(laB)*cos(loA-loB)))
    
laA = radians(float(input('Digite a latitude A: ')))
loA = radians(float(input('Digite a longitude A: ')))
laB = radians(float(input('Digite a latitude B: ')))
loB = radians(float(input('Digite a longitude B: ')))
    
print('A distância é %.2fkm.' % dist(laA, laB, loA, loB))