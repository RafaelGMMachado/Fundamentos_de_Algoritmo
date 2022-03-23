#############################################################################
# Nome: Aula 12 (Laboratório) - Listas e Tuplas 
# Autor: Rafael Machado                                               
# Data: 17/09/2021                                                    
# Resumo: Tarefa sobre Listas e Tuplas
#############################################################################

##############
# Exercício 1
# Resumo: 
#"""
print("Exercício 1")

carros = []
consumo = []
kms = []
for n in range (5):
    carros.append (str(input("")))
n = 0
for n in range (5):
    valor = int(input(""))
    consumo.append (valor)
    kms.append (1000/valor)
economico = consumo.index(max(consumo))
print(carros[economico])
for n in range (5):
    print(round(kms[n]))
#"""
##############
# Exercício 2
# Resumo: 
#"""
print("\nExercício 2")

lista_n = []
lista_p = []
numero = 1
while numero != 0:
    numero = int(input(""))
    if numero < 0:
        lista_n.append (numero)
    elif numero > 0:
        lista_p.append (numero)

lista = [*lista_n, *lista_p]
print(lista)
#"""
##############
# Exercício 3
# Resumo: 
#"""
print("\nExercício 3")

from math import sqrt
lista = []
desvio = 0

tamanho = int(input("Qual o tamanho da lista: "))
print("Digite os valores:")

total = 0
for n in range (tamanho):
    numero = int(input(""))
    lista.append (numero)
    total += numero
media = total/tamanho

for n in range (tamanho):
    numero = (lista[n] - media)**2
    desvio += numero
desvio = sqrt(desvio/tamanho)
print ("Média = %.2f" %media + " e Desvio = %.4f" %desvio)

##############
# Exercício 4
# Resumo: 
#"""
print("\nExercício 4")

lista = []
lista_p = []
lista_i = []
for n in range (20):
    numero = int(input(""))
    lista.append (numero)
    if numero%2 == 0:
        lista_p.append (numero)
    else:
        lista_i.append (numero)
print(*lista)
print(*lista_i)
print(*lista_p)

##############
# Exercício 5
# Resumo: 
#""""
print("\nExercício 5")

v1 = []
v2 = []
dimensao = int(input("Digite a dimensão dos vetores: "))
print("Digite o vetor 1:")
for n in range (dimensao):
    v1.append (int(input("")))
print("Digite o vetor 2:")
for n in range (dimensao):
    v2.append (int(input("")))
soma = 0
for n in range (dimensao):
    soma += (v1[n]*v2[n])
print(soma)

##############
# Exercício 6
# Resumo: 
#""""
print("\nExercício 6")

def quadrado(lista = []):
    n_lista = []
    for indice in range(len(lista)):
        n_lista.append (lista[indice]**2)
    return n_lista
