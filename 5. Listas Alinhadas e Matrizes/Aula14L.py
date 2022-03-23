#############################################################################
# Nome: Aula 14 (Laboratório) - Listas Alinhadas e Matrizes
# Autor: Rafael Machado                                               
# Data: 24/09/2021                                                    
# Resumo: Tarefa sobre Listas Alinhadas e Matrizes
#############################################################################

##############
# Exercício 1
# Resumo: 
Matriz = []
Maiores = []
for n_linhas in range (2):
    linha = []
    for n_colunas in range (2):
        linha.append (int(input("Digite o elemento da linha {0} e coluna {1}: ".format (n_linhas,n_colunas) )))
    Matriz.append(linha)
    Maiores.append (max(linha))
maior = max(Maiores)

print("Matriz resultante:")
for linha in range (2):
    for coluna in range (2):
        print("%3d " % (Matriz[linha][coluna]*maior), end = "")
    print()

##############
# Exercício 2
# Resumo: 
lojas = []
produtos = []
precos = []
for n in range (3):
    lojas.append ( str(input("Digite o nome da loja: ")) )
for n in range (5):
    produtos.append (str(input("Digite o nome do produto: ")))
for linha in range (3):
    linha_x = []
    for coluna in range (5):
        linha_x.append (int(input("Digite o preco do produto {0} na loja {1}: ".format (coluna, linha) )))
    precos.append (linha_x)
    
print("\nLojas:")
for n in range (len(lojas)):
    print(lojas[n])
print("\nProdutos:")
for n in range (len(produtos)):
    print(produtos[n])
print("\nPreços:")
for linha in range(len(precos)): 
    for coluna in range ( len(precos[linha]) ): 
        print("%3d " % precos[linha][coluna] , end= "")
    print()
    
print("\nPreços menores que R$ 50.00:")
for linha in range ( len(precos) ):
    for coluna in range ( len(precos[linha]) ):
        if (precos[linha][coluna]) < 50:
            print("Loja: {0}, produto {1} e preço {2}".format (lojas[linha], produtos[coluna], precos[linha][coluna]) )
    print()

##############
# Exercício 3
# Resumo: 
from random import randint
Matriz = []
Vetor = []
Matriz_M = []
for n_linhas in range(20):
    linha = []
    for n_colunas in range(10):
        linha.append(randint(0,10))
    Matriz.append(linha)
print("Matriz original:")
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        print("%3d " % Matriz[linha][coluna] , end= "")
    print()
    
print("\nVetor com a somatória de cada linha:")
soma = 0
for linha in range (20):
    for coluna in range (10):
        soma += Matriz[linha][coluna]
    Vetor.append (soma)
print(Vetor)

print("\nmatriz depois da multiplicação:")
for n_linhas in range(20):
    linha = []
    for n_colunas in range(10):
        linha.append ( Matriz[n_linhas][n_colunas]*Vetor[n_linhas] )
    Matriz_M.append(linha)
for linha in range(len(Matriz_M)): 
    for coluna in range (len(Matriz_M[linha])): 
        print("%5d " % Matriz_M[linha][coluna] , end= "")
    print()

##############
# Exercício 4
# Resumo: 

Matriz = []

for n_linhas in range(4):
    linha = []
    for n_colunas in range(2):
        linha.append( int(input("Digite o elemento da linha {0} e coluna {1}: ".format (n_linhas, n_colunas) )) )
    Matriz.append(linha)

print("Matriz original:")
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        print("%3d " % Matriz[linha][coluna] , end= "")
    print()

print()
elementos = 0
for linha in range (4):
    for coluna in range (2):
        if Matriz[linha][coluna] > 10:
            print("%s é maior que 10!" % (Matriz[linha][coluna]) )
            elementos += 1
            Matriz[linha][coluna] = 0
print("No total, %s elementos são maiores que 10!" % (elementos) )

print("\nMatriz sem os números maiores que 10:")
for linha in range(len(Matriz)): 
    for coluna in range (len(Matriz[linha])): 
        print("%3d " % Matriz[linha][coluna] , end= "")
    print()