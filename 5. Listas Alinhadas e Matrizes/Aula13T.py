#############################################################################
# Nome: Aula 13 (Teoria) - Listas Alinhadas e Matrizes
# Autor: Rafael Machado                                               
# Data: 22/09/2021                                                    
# Resumo: Exercícios Sobre Listas Alinhadas e Matrizes
#############################################################################

##############
# Exercício 1
# Resumo: 
from random import randint, uniform 
#randint - Gera números inteiros aleatórios 
##uniform - Gera números Reais aleatórios
inteiros = []
reais = []
strings = ["a", "b", "c", "d", "e", "f", "g"]
complexos = [2+3j, -3-6j, 7j, 1-9j, 8+5j]
for n in range (15):
    reais.append (round (uniform (0,50) ,2) )
    if n < 10:
        inteiros.append (randint(0,50))
completa = [inteiros, reais, strings, complexos]

inteiros = []
reais = []
strings = []
complexos = []

for n in range (50):
    completa[0].append (randint(0, 50))

##############
# Exercício 2
# Resumo: 
from random import randint
Matriz = []

for n_linhas in range(10):
    linha = []
    for n_colunas in range(15):
        linha.append(randint(0,10))
    Matriz.append(linha)
for linha in range(len(Matriz)): 
    #Poderia substituir o "len(Matriz)" pela variável "linha"
    for coluna in range (len(Matriz[linha])): 
        #Poderia substituir o "len(Matriz[linha])" pela variável "colunas"
        print("%4d" % Matriz[linha][coluna] , end= "")
    print()
print("Primeira coluna: ")
for linha in range(10):
    print ("%4d" % Matriz[linha][0])

##############
# Exercício 3
# Resumo: 
from random import randint
Matriz = []
vetor = []
for n_linhas in range(4):
    linha = []
    for n_colunas in range(4):
        linha.append(randint(0,10))
    Matriz.append(linha)
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        print("%4d" % Matriz[linha][coluna] , end= "")
    print()
for linha in range(len(Matriz)): 
    soma = 0
    for coluna in range (len(Matriz[linha])): 
        if (Matriz[linha][coluna])%2 != 0:
            soma += Matriz[linha][coluna]
    vetor.append (soma)
print(vetor)

##############
# Exercício 4
# Resumo: 
from random import randint
Matriz = []
for n_linhas in range(3):
    linha = []
    for n_colunas in range(3):
        linha.append(randint(0,10))
    Matriz.append(linha)
soma = 0
for n in range(len(Matriz)): 
    soma += Matriz[n][n]
print("A soma dos elementos da diagonal principal é:", soma)
print("A matriz é:")
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        print("%4d" % Matriz[linha][coluna] , end= "")
    print()

##############
# Exercício 5
# Resumo: 
from random import randint
Matriz = []
for n_linhas in range(10):
    linha = []
    for n_colunas in range(5):
        linha.append(randint(0, 10))
    Matriz.append(linha)
print("Matriz:")
for linha in range(len(Matriz)):
    for coluna in range (len(Matriz[linha])):
        print("%4d" % Matriz[linha][coluna], end= "")
    print()
print("Matriz transposta:")
for coluna in range(5):
    for linha in range(10):
        print("%4d" % Matriz[linha][coluna], end= "")
    print()

##############
# Exercício 6
# Resumo: 
from random import randint
Matriz = []
for n_linhas in range(12):
    linha = []
    for n_colunas in range(12):
        linha.append(randint(0,10))
    Matriz.append(linha)
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        print("%4d" % Matriz[linha][coluna] , end= "")
    print()
soma = 0
numeros = 0
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        if [linha] > [coluna]:
            soma += Matriz[linha][coluna]
            numeros += 1
calculo = str(input("Deseja realizar uma soma('S') ou média('M') dos elementos? "))
if calculo == "S":
    print("A soma dos números foi:",soma)
elif calculo == "M":
    print("A média dos números foi: %.2f" % (soma/numeros))
else:
    print("Valor inválido")

##############
# Exercício 7
# Resumo: 
from random import randint
Matriz = []
for n_linhas in range(10):
    linha = []
    for n_colunas in range(3):
        linha.append(randint(0,10))
    Matriz.append(linha)
#
print("\nMatriz das notas de cada aluno:")
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        print("%4d" % Matriz[linha][coluna] , end= "")
    print()
#
print("\nMenor nota e valor da menor nota de cada aluno:")
for linha in range (len(Matriz)):
    print("A menor nota do aluno {0} foi da prova {1}, ele tirou {2} pontos".format (linha+1, Matriz[linha].index(min(Matriz[linha])),min(Matriz[linha])  ))
#
print("\nMenor nota obtida em cada prova e quantidade de alunos que obtiveram essa nota:")
prova1 = []
prova2 = []
prova3 = []
for linha in range(len(Matriz)): 
    prova1.append(Matriz[linha][0])
    prova2.append(Matriz[linha][1])
    prova3.append(Matriz[linha][2])
print("A menor nota obtida na prova 1 foi {0}, ela foi tirada {1} vezes".format ( min(prova1) , prova1.count(min(prova1)) ) )
print("A menor nota obtida na prova 2 foi {0}, ela foi tirada {1} vezes".format ( min(prova2) , prova2.count(min(prova2)) ) )
print("A menor nota obtida na prova 3 foi {0}, ela foi tirada {1} vezes".format ( min(prova3) , prova3.count(min(prova3)) ) )

##############
# Exercício 8
# Resumo: 
from random import uniform
Matriz = []
for n_linhas in range(4):
    linha = []
    for n_colunas in range(7):
        linha.append (round (uniform(0,10),2 ) )
    Matriz.append(linha)
#
menor = 10
lin_menor = 0
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        if Matriz[linha][coluna] < menor:
            menor = Matriz[linha][coluna]
            lin_menor = Matriz.index(Matriz[linha])
#
print("O MINIMAX é:",max(Matriz[lin_menor]))
print("Ele está\nNa linha: {0}\nNa coluna: {1}".format (lin_menor, Matriz[lin_menor].index(max(Matriz[lin_menor])) ) )