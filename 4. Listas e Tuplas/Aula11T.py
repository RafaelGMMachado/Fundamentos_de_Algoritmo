#############################################################################
# Nome: Aula 11 (Teoria) - Listas e Tuplas   
# Autor: Rafael Machado                                               
# Data: 15/09/2021                                                    
# Resumo: Exercícios Sobre Listas e Tuplas
#############################################################################

##############
# Exercício 1
# Resumo: Mostra o Menor Valor Dentro da Lista.
T = [1,7,4,2]
print(min(T))

##############
# Exercício 2
# Resumo: Pede 10 Números e diz qual é o maior e qual o seu índice.
lista = []
for n in range(10):
    numero = float(input("Digite o {0}º número: ".format (n+1)))
    lista.append (numero)
print("O índicie do seu maior número é:", lista.index(max(lista)))
print("O maior número é:",max(lista))

##############
# Exercício 3
# Resumo: 
numero = []
soma_par = 0
soma_ipar = 0
for n in range(10):
    numero.append (int(input("Digite o {0}º número: ".format (n+1))))
    if (n%2) == 0:
        soma_ipar += num


for elemento in numero:
    if (elemento%2) == 0:
        soma_par += elemento

print("Soma dos elementos pares:", soma_par)
print("Soma dos índices pares:", soma_ipar)

##############
# Exercício 4
# Resumo: 
lista = []
for n in range(5):
    lista.append (int(input("Digite o {0}º número: ".format (n+1))))
#ou print(lista[::-1])
for n in range(len(lista)):
    print(lista[-1], end=" ")
    lista.pop(-1)
"""
#ou
i = 5
for n in range(n-1, -1, -1):
    print(lista[n], end = " ")
"""
##############
# Exercício 5
# Resumo: 
numeros = []
for n in range(10):
    numeros.append (int(input("Digite o {0}º número: ".format (n+1))))

for indice in range(2, len(numeros)):
    if numeros[indice] > (numeros[indice-1]+numeros[indice-2]):
        print(numeros[indice])

##############
# Exercício 6
# Resumo: 
from random import randint
lista = []
for n in range (20):
    lista.append (randint(0,201))
for n in range (20):
    print(max(lista), end = " ")
    lista.remove(max(lista))
"""
ou
import random
lista = []
for i in range(20):
    lista.append(random.randrange(0, 201))

for valor in range(len(lista)):
    for outro_valor in range(len(lista)):
        if lista[valor] < lista[outro_valor]:
            salva = lista[valor] 
            lista[valor] = lista[outro_valor]
            lista[outro_valor] = salva
            #O que isso faz é basicamente trocar os itens de lugar na lista, se um valor for menor
            #que outro valor, eles trocam de posição.

print(lista)
"""