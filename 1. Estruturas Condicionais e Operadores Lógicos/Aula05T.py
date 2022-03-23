######################################################################
# Nome: Aula 05 (Teórica) - Estrutura Condicional e Operadores Lógicos   
# Autor: Rafael Machado                                               
# Data: 25/08/2021                                                    
# Resumo: Exercícios Sobre Estrutura Condicional e Operadores Lógicos 
######################################################################

#ou

"""
3 '"' para comentários em bloco
Da pra usar os comentários para tirar alguma coisa temporariamente do código para fazer testes ou algo do gênero.
"""

##############
# Exercício 1
# Resumo: O programa recebe 2 notas parciais de um aluno e exibe a média alcançada por ele.

print("Exercício 1")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media <= 10 and media >= 0:
    if media == 10:
        print("Aprovado Com Distinção!")
    elif media>=5:
        print("Aprovado!")
    else:
        print("Reprovado!")
else:
    print("Nota Inválida!")

##############
# Exercício 2
# Resumo: O programa recebe dois números e pergunta qual operação você quer realizar. Depois disso, ele te retorna o valor correspondente aquela operação.

print("\nExercício 2")

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
operacao = str(input("Qual operação deseja realizar? "))

if operacao == "soma" or operacao == "+" or operacao == "Soma":
    soma = n1+n2
    print(soma)
elif operacao == "divisão" or operacao == "/" or operacao == "Divisão":
    divisão = n1/n2
    print(divisão)
elif operacao == "subtração" or operacao == "-" or operacao == "Subtração":
    subtracao = n1-n2
    print(subtracao)
elif operacao == "multiplicação" or operacao == "*" or operacao == "Multiplicação":
    multiplicacao = n1*n2
    print(multiplicacao)
else:
    print("A operação escolhida não é válida!")

##############
# Exercício 3
# Resumo: O programa recebe um ano e diz se esse ano é ou não bissexto.

print("\nExercício 3")

ano = int(input("Digite o ano: "))

d400 = ano%400
d4 = ano%4
d100 = ano%100

if (ano%400 == 0) or (ano%4 == 0) and not (ano%100 == 0):
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")

##############
# Exercício 4
# Resumo: O programa recebe o valor de "x" e "y" e diz o quadrante que o ponto pertence.

print("\nExercício 4")

x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

if x>1 and y>1:
    print("O ponto pertence ao quadrante Q1!")
elif x<1 and y>1:
    print("O ponto pertence ao quadrante Q2!")
elif x<1 and y<1:
    print("O ponto pertence ao quadrante Q3!")
elif x>1 and y<1:
    print("O ponto pertence ao quadrante Q4!")
elif x == 0 and y != 0:
    print("O ponto está sobre o eixo y")
elif x != 0 and y == 0:
    print("O ponto está sobre o eixo x")
else:
    print("O ponto está na origem!")

##############
#Exercício 5
#Resumo: O programa recebe o salário de um funcionário e mostra qual será o reajuste do seu salário.

print("\nExercício 5")

salario = float(input("Digite o seu salário: "))

if salario >= 0 and salario <= 400:
    reajuste = 0.15 * salario
elif salario > 400 and salario <= 800:
    reajuste = 0.12 * salario
elif salario > 800 and salario <= 1200:
    reajuste = 0.1 * salario
elif salario > 1200 and salario <= 2000:
    reajuste = 0.07 * salario
elif salario > 2000:
    reajuste = 0.04 * salario
else:
    print("Valor inválido!")
    exit()

print("Salário novo: R$",salario + reajuste)
print("Reajuste: R$", round(reajuste,2))
print("Percentual do reajuste: %.2f %%" %(((salario+reajuste)/salario-1)*100))

"""
Outra forma de fazer esse final sem usar o comando 'exit()' seria:
...
else:
    reajuste == 0
    
if reajuste == 0:
    print("Valor inválido!")
else:
...
"""

##############
# Exercício 6
# Resumo: O programa faz 5 perguntas de "sim" ou "não" e com base nelas, emite uma classificação sobre a participação da pessoa no crime.

print("\nExercício 6")

print("!Aviso!")
print("Responder apenas com 'sim' ou 'não'!")
telefone = str(input("Telefonou para a vítima? "))
local = str(input("Esteve no local do crime? "))
casa = str(input("Mora perto da vítima? "))
dever = str(input("Devia para a vítima? "))
trabalho = str(input("Já trabalhou com a vítima? "))

if telefone == "sim":
    telefone = int(1)
else:
    telefone = int(0)
if local == "sim":
    local = int(1)
else:
    local = int(0)
if casa == "sim":
    casa = int(1)
else:
    casa = int(0)
if dever == "sim":
    dever = int(1)
else:
    dever = int(0)
if trabalho == "sim":
    trabalho = int(1)
else:
    trabalho = int(0)

suspeito = telefone + local + casa + dever + trabalho

if suspeito == 2:
    print("Suspeito!")
elif suspeito == 3 or suspeito == 4:
    print("Cúmplice!")
elif suspeito == 5:
    print("Assassino!")
else:
    print("Inocente!")

##############
# Exercício 7
# Resumo: O programa pergunta a quantidade de litros e o tipo de gasolina que deseja abastecer e retorna o valor que será pago.

print("\nExercício 7")

print("Combustíveis disponíveis: álcool e gasolina")
combustivel = str(input("Com qual combustível deseja abastecer? "))
litros = int(input("Com quantos litros deseja abastecer? "))

gasolina = float(litros*5.6)
alcool = float(litros*4.19)

if combustivel == "álcool":
    if 0 < litros <= 20: 
        print("O valor a ser pago é de: R$%.2f" % float(alcool*0.97))
    elif litros > 20:
        print("O valor a ser pago é de: R$%.2f" % float(alcool*0.95)) 
    else:
        print("Valor inválido!")            
elif combustivel == "gasolina":
    if 0 < litros <= 20: 
        print("O valor a ser pago é de: R$%.2f" % float(alcool*0.96))
    elif litros > 20:
        print("O valor a ser pago é de: R$%.2f" % float(alcool*0.94)) 
    else:
        print("Valor inválido!")            
else:
    print("Combustível inválido!")

##############
# Exercício 8
# Resumo: O programa recebe um valor entre 10 e 1000 que a pessoa deseja sacar e retorna a quantidade cada nota que será entregue, sempre dando a menor quantidade possível.

print("\nExercício 8")
valor = int(input("Qual valor deseja sacar? "))

n100 = valor//100
n50 = (valor%100)//50
n10 = ((valor%100)%50)//10
n5 = (((valor%100)%50)%10)//5
n1 = (((valor%100)%50)%10)%5
if 10 < valor < 1000:
    print("Serão entregues:")
    if n100 >= 1:
        print("{0} notas de R$100,00".format (n100))
    if n50 >=1:
        print("{0} notas de R$50,00".format (n50))
    if n10 >=1:
        print("{0} notas de R$10,00".format (n10))
    if n5 >=1:
        print("{0} notas de R$5,00".format (n5))
    if n1 >=1:
        print("{0} notas de R$1,00".format (n1))
else:
    print("Valor inválido")


#Tomar cuidado com comparações com o 'float', pois se somar valores #
#decimais ele passa errado por causa da conversão de decimal para binário.#
#Por isso, quando for fazer essas comparações, arredondar as casas decimais antes#