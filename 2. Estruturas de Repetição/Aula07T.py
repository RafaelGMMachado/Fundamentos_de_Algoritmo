#############################################################################
# Nome: Aula 07 (Teoria) - Estruturas de Repetição   
# Autor: Rafael Machado                                               
# Data: 01/09/2021                                                    
# Resumo: Exercícios sobre Estruturas de Repetição
#############################################################################

from time import*
from random import randrange
##############
# Exercício 1
# Resumo: 
#
x = 10
while x >= 0:
    print(x)
    x -= 1
    sleep(1)

##############
# Exercício 2
# Resumo: 
#
n = int(input("Digite um número: "))
x = 1
print("A tabuada do {0} é:".format(n))
sleep(1)
while x <= 10:
    print("{0} x {1} = {2}".format (n,x,(n*x)))
    x += 1
    sleep(1)

##############
# Exercício 3
# Resumo: 
#
n = int(input("Digite um número de 0 a 10: "))
while 0 > n or n > 10:
    print("Número inválido!")
    n = int(input("Digite um número de 0 a 10: "))
print("Valor Aceito!")

#Teste
print("Tabuada do 1 ao 10!")
for t in range(1,11):
    sleep(3)
    print("Tabuada do",t)
    for m in range(1,11):
        print("{0} x {1} = {2}".format (m,t,(m*t)))

##############
# Exercício 4
# Resumo: 
#
maior = 0
vezes = 0
for x in range(0,70):
    num = randrange(1,101)
    if num > maior:
        maior = num
        print(maior)
        vezes += 1
print("O maior número gerado foi:",maior)
print("Ele foi atualizado {0} vezes".format(vezes))         

##############
# Exercício 5
# Resumo: 
#
total = 0
for x in range(5):
    n = float(input("Digite o {0}º número: ".format(x+1)))
    media = n/5
    total += media 
print("A sua média é: %.2f" %total)
#ou (é mais eficiente, pois faz o cálculo só uma vez)
soma = 0
for x in range(1,6):
    n = float(input("Digite o {0}º número: ".format(x)))
    soma += n 
print("A sua média é: %.2f" %(soma/x))

##############
# Exercício 6
# Resumo: 
#
total = 0
numeros = 0
n = int(input("Digite um número: "))

while n != 0:
    total += n
    numeros += 1
    n = int(input("Digite um número: "))
numeros += 1
print("Você digitou {0} números!".format(numeros))
print("A somatória desses números foi:",total)
print("A média aritimética desses números foi: %.2f" %(total/numeros))
#ou (melhor, menor quantidade de linhas)
total = 0
numeros = 0

while True:
    n = int(input("Digite um número: "))
    total += n
    numeros += 1
    if n == 0:
        break

print("Você digitou {0} números!".format(numeros))
print("A somatória desses números foi:",total)
print("A média aritimética desses números foi: %.2f" %(total/numeros))

##############
# Exercício 7
# Resumo: 
#
total = 0
while True:
    idade = int(input("Qual a idade da pessoa? "))
    if idade <= 2:
        continue
    elif 3 <= idade <= 12:
        total += 14
    elif total >= 65:
        total += 18
    elif total == "":
        break
    else:
        total += 23
print ("O custo total para o grupo será de: R$%.2f" %total)