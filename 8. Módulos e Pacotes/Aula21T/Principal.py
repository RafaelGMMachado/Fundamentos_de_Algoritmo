#############################################################################
# Nome: Aula 21 (Teoria) - Módulos e Pacotes
# Autor: Rafael Machado                                               
# Data: 20/10/2021                                                    
# Resumo: Exercícios sobre Módulos e Pacotes
#############################################################################

##############
# Exercício 1
# Resumo: 
def main1 ():
    sexo = input("Digite o seu sexo (F ou M): ")
    peso = float(input("Digite o seu peso em Kg: "))
    if Modulo.aptidao(sexo, peso) == True:
        print("Você está apto para doar sangue!")
    else:
        print("Você não está apto para doar sangue!")
if __name__ == "__main__":
    main1()

# Exercício 2
# Resumo: 
def main2 ():
    cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
    cateto2 = float(input("Digite o comprimento do segundo cateto: "))
    print("O valor da hipotenusa é:", Modulo.hipotenusa(cateto1, cateto2) )
if __name__ == "__main__":
    main2()

# Exercício 3
# Resumo: 
def main3 ():
    texto = input("Digite o texto que deseja corrigir: ")
    print(Modulo.corrigir(texto))
if __name__ == "__main__":
    main3()

# Exercício 4
# Resumo: 
def main4 ():
    senha = input("Digite a sua senha: ")
    if Modulo.tamanho(senha) == False:
        print("A senha é muito curta!")
    elif Modulo.maiuscula(senha) == False:
        print("A senha não possui maiúsculas!")
    elif Modulo.minuscula(senha) == False:
        print("A senha não possui minúsculas!")
    elif Modulo.numero(senha) == False:
        print("A senha não possui números!")
    else:
        print("A senha é boa!")
if __name__ == "__main__":
    main4()

# Exercício 5
# Resumo: 
def main5 ():
    string = input("Digite um numero inteiro: ")
    if Modulo.isInteger(string) == True:
        print("O número é inteiro!")
    else:
        print("O número não é inteiro!")
if __name__ == "__main__":
    main5()