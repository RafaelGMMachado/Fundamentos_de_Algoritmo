#############################################################################
# Nome: Aula 22 (Laboratório) - Módulos
# Autor: Rafael Machado                                               
# Data: 22/10/2021                                                    
# Resumo: Tarefa sobre Módulos
#############################################################################
import modulo
##############
# Exercício 1
# Resumo: 
def main1 ():
    placa = modulo.arrumarPlaca(modulo.criarLetras(), modulo.criarNumeros())
    print("Placa =", placa)
if __name__ == "__main__":
    main1()

##############
# Exercício 2
# Resumo: 

def main2 ():
    limite = int(input("Digite um limite para os números primos: "))
    lista = modulo.crivo(limite)
    primos = ""
    for n in range ( len(lista) ):
        primos = primos + str(lista[n]) + " "
    print (primos)
if __name__ == "__main__":
    main2()

##############
# Exercício 3
# Resumo: 
def main3 ():
    arquivo = input("Digite o nome do arquivo com o extensão: ")
    modulo.remover(arquivo)
if __name__ == "__main__":
    main3()

##############
# Exercício 4
# Resumo: 
def main4 ():
    palavras = input("Digite as palavras desejadas separando-as por hífen(-): ")
    print(modulo.ordenar(palavras))
    modulo.calcular(palavras)
if __name__ == "__main__":
    main4()