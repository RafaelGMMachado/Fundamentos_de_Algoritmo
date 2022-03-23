#############################################################################
# Nome: Aula 13 (Teoria) - Arquivos
# Autor: Rafael Machado                                               
# Data: 29/09/2021                                                    
# Resumo: Exercícios Sobre Arquivos
#############################################################################

import os
##############
# Exercício 1
# Resumo: 
def Exercicio1 ():
    arq_pares = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\Pares.txt", "w")
    for n in range (1000):
        if n%2 == 0:
            arq_pares.write("%d\n" % n)
    arq_pares.close()

    arq_pares = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\Pares.txt", "r")
    lista = arq_pares.readlines()
    arq_pares.close()
    arq_pares_invertido = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\Pares Invertido.txt", "w")
    for n in range ( len(lista) ):
        arq_pares_invertido.write("%s" % ( lista[len(lista)-1-n] ) )
    arq_pares_invertido.close()

##############
# Exercício 2
# Resumo: 
def Exercicio2 ():
    arq_numeros2 = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\numeros2.txt", "r")
    lista = arq_numeros2.readlines()
    arq_numeros2.close()
    lista = lista[0].split()
    def somatoria(lista):
        soma = 0
        for elemento in range( len(lista) ):
            soma += int(lista[elemento])
        return soma
    print(somatoria(lista))

##############
# Exercício 3
# Resumo: 
def Exercicio3 ():
    def ler ():
        arq_numeros3 = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\numeros3.txt", "r")
        lista = arq_numeros3.readlines()
        arq_numeros3.close()
        num = []
        for n in range ( len(lista) ):
            num.append ( int (lista[n].strip()) )
        return num

    def num_unicos (num):
        num_unicos = []
        for elemento in range ( len(num) ):
            for verificar in range ( elemento+1 ):
                if elemento == verificar:
                    num_unicos.append ( num[elemento] )
                elif num[elemento] == num[verificar]:
                    break
        return num_unicos

    def gravar (num_unicos):
        arq_numeros3unicos = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\numeros3unicos.txt", "w")
        for n in range ( len(num_unicos) ):
            arq_numeros3unicos.write("%d\n" % num_unicos[n] )
        arq_numeros3unicos.close()

    num = ler()
    num_unicos = num_unicos( num )
    gravar (num_unicos)

##############
# Exercício 4
# Resumo: 
def Exercicio4 ():
    def criar():
        print("Insira as informações para a criação do contato")
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        numero = input("Digite o número do celular: ")
        email = input("Digite o endereço de e-mail: ")
        arquivo = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\_" + nome + "_" + sobrenome + ".txt", "w")
        arquivo.write ("Número: {0}\nE-mail: {1}".format (numero, email) )
        arquivo.close()

    def procurar():
        print("Para ler o arquivo, precisamos do nome e sobrenome do contato.")
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        arquivo = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\_" + nome + "_" + sobrenome + ".txt", "r")
        lista = arquivo.readlines()
        arquivo.close()
        for n in range ( len(lista) ):
            print(lista[n].strip() )
    
    def atualizar ():
        print("Para atualizar o arquivo, precisamos do nome e sobrenome do contato.")
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        arquivo = open(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\_" + nome + "_" + sobrenome + ".txt", "w")
        numero = input("Digite o novo número do celular: ")
        email = input("Digite o novo endereço de e-mail: ")
        arquivo.write("Número: {0}\nE-mail: {1}".format ( numero, email ) )
        arquivo.close()
    
    def apagar ():
        print("Para excluir o arquivo, precisamos do nome e sobrenome do contato.")
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        os.remove(r"C:\Users\RafaelGMM\OneDrive\Documents\Estudos FEI\1. Fundamentos de Algoritimos\Teoria\Aula15 - Arquivos\_" + nome + "_" + sobrenome + ".txt")
    
    while True:
        os.system("cls") or None
        print("1 - Novo Contato\n2 - Procura\n3 - Atualiza Contato\n4 - Apaga Contato\n0 - Sair")
        entrada = int(input("Digite a Opção: "))
        if entrada == 1:
            os.system("cls") or None
            criar()
            input("Contato criado!\nAperte 'ENTER' para continuar")
        elif entrada == 2:
            os.system("cls") or None
            procurar()
            input("Aperte 'ENTER' para continuar")
        elif entrada == 3:
            os.system("cls") or None
            atualizar()
            input("Contato atualizado!\nAperte 'ENTER' para continuar")
        elif entrada == 4:
            os.system("cls") or None
            apagar()
            input("Contato excluido!\nAperte 'ENTER' para continuar")
        elif entrada == 0:
            break
        else:
            print("Opção Inválida")
            break
###################################################
print("1 - Exercício 1\n2 - Exercício 2\n3 - Exercício 3\n4 - Exercício 4")
entrada = int(input("Digite qual exercício deseja rodar: "))
if entrada == 1:
    os.system("cls") or None
    Exercicio1()
elif entrada == 2:
    os.system("cls") or None
    Exercicio2()
elif entrada == 3:
    os.system("cls") or None
    Exercicio3()
elif entrada == 4:
    os.system("cls") or None
    Exercicio4()
else:
    print("Opção Inválida")
