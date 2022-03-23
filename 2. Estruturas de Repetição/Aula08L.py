#############################################################################
# Nome: Aula 08 (Laboratório) - Estruturas de Repetição   
# Autor: Rafael Machado                                               
# Data: 03/09/2021                                                    
# Resumo: Tarefa sobre Estruturas de Repetição
#############################################################################

##############
# Exercício 1
# Resumo: Informa o maior número entre os digitados
#""""
print("Exercício 1")

ns = int(input("Entre com a quantidade de números que serão digitados: "))
for n in range(ns):
    num = int(input("{0}º número : ".format (n+1)))
    if n == 0:
        maior = num
    elif num > maior:
        maior = num
print("Maior número digitado:", maior)

##############
# Exercício 2
# Resumo: Converte graus Celsius para graus Fahrenheit
#""""
print("\nExercício 2")

min = int(input("Digite o valor mínimo em graus C: "))
max = int(input("Digite o valor máximo em graus C: "))

print("%18s %18s" % ("Temperatura em C","Temperatura em F"))
for i in range(min, max + 1,5):
    print("%18d %18d" % (i, i*9/5+32))

##############
# Exercício 3
# Resumo: Recebe um ano maior que 2007 e determina o salário atual do funcionário
#""""
print("\nExercício 3")

ano = int(input("Digite o ano desejado: "))
salario = 5000*1.015*1.03
aumento = 0.03
if ano > 2007:
    n_ano = ano - 2007
    for n in range(n_ano):
        aumento*= 2
        salario = salario*(1+aumento)
else:
    exit()

print("Salário de {0}: R$ {1:.2f}".format (ano,salario))

##############
# Exercício 4
# Resumo: Lê um valor inteiro e mostra um valor E seguindo uma fórmula.
#""""
print("\nExercício 4")

nu = int(input("Digite o número desejado: "))
E = 1
for n in range (nu):
    E += 1/(n+1)
print("%.3f" %E)

##############
# Exercício 5
# Resumo: Verifica se o número é primo ou não
#""""
print("\nExercício 5")

num = int(input("Digite o número desejado: "))
vezes = 0
if num > 1:
    for n in range(num):
        t = num%(n+1)
        if t == 0:
            vezes += 1
else:
    exit()
if vezes == 2:
    print("Número primo")
else:
    print("Número não primo")

##############
# Exercício 6
# Resumo: Determina o maior divisor comum entre dois números m, n.
#""""
print("\nExercício 6")

n = int(input("Digite n: "))
m = int(input("Digite m: "))
if n > m:
    d = m
else:
    d = n
md = m%d
nd = n%d
while nd != 0 or md != 0:
    d -= 1
    md = m%d
    nd = n%d
print(d)

##############
# Exercício 7
# Resumo: Método para aproximar valores das raízes de uma equação numérica. Método de Newton.
#""""
print("\nExercício 7")

from math import *
x = int(input("Digite o número desejado: "))
palpite = x/2
erro = abs(palpite**2-x)
while erro > 10**(-12):
    palpite = (palpite+(x/palpite))/2
    erro = (palpite**2)-x
print("%.3f"%palpite)