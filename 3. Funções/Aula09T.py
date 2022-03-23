#############################################################################
# Nome: Aula 09 (Teoria) - Funções   
# Autor: Rafael Machado                                               
# Data: 08/09/2021                                                    
# Resumo: Exercícios Sobre Funções
#############################################################################

##############
# Exercício 1
# Resumo: 
def maximo(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "Os valores são Iguais!"


x = int(input("Insira o valor de 'x': "))
y = int(input("Insira o valor de 'y': "))
print(maximo(x,y))

##############
# Exercício 2
# Resumo: 
def multiplo(x,y):
    if y%x == 0:
        return True
    else:
        return False

x = int(input("Insira o valor de 'x': "))
y = int(input("Insira o valor de 'y': "))
print(multiplo(x, y))

##############
# Exercício 3
# Resumo: 
def area(b, h):
    return (b*h)/2
b = int(input("Insira a base: "))
h = int(input("Insira a altura: "))
print("A área do triângulo é: %.2f" % area(b,h))

##############
# Exercício 4
# Resumo: Define todas as "datas mágicas" do século XX.
dia = 1
mes = 1
ano = 1901
cont = 0
def data_magica(dia, mes, ano):
    global cont
    if (dia*mes) == ano-1900:
        print("{0}/{1}/{2} é uma data mágica".format(dia,mes,ano))
        cont += 1


while ano <= 2000:
    mes = 1
    for m in range (12):
        dia = 1
        if m+1 == 1 or m+1 == 3 or m+1 == 5 or m+1 == 7 or m+1 == 8 or m+1 == 10 or m+1 == 12:
            for d in range (31):
                data_magica(dia, mes, ano)
                dia += 1
        elif ((ano%400 == 0) or (ano%4 == 0) and not (ano%100 == 0)) and m+1 == 2:
            for d in range (29):
                data_magica(dia, mes, ano)
                dia += 1
        elif m+1 == 2:
            for d in range (28):
                data_magica(dia, mes, ano)
                dia += 1
        else:
            for d in range (30):
                data_magica(dia, mes, ano)
                dia += 1
        mes += 1
    ano+=1
print(cont)

##############
# Exercício 5
# Resumo: 
def sangue(sexo, peso):
    if sexo == "homem":
        if peso >= 60:
            print("Você está apto para doar sangue!")
        else:
            print("Você não está apto para doar sangue!")
    elif sexo == "mulher":
        if peso >= 50:
            print("Você está apta para doar sangue!")
        else:
            print("Você não está apta para doar sangue!")
sexo = str(input("Você é homem ou mulher? "))
sexo = sexo.lower()
peso = float(input("Qual o seu peso em Kg? "))
sangue(sexo, peso)

##############
# Exercício 6
# Resumo: Refazer os ex 1, 2 e 3 usando o lambda.
a = lambda x,y: max(x, y)

x = int(input("Insira o valor de 'x': "))
y = int(input("Insira o valor de 'y': "))
print(a(x,y))
#__//__#
b = lambda x,y: y%x 

x = int(input("Insira o valor de 'x': "))
y = int(input("Insira o valor de 'y': "))
if b(x,y) == 0:
    print(True)
else:
    print(False)
#__//__#
a = lambda b,h: (b*h)/2
b = int(input("Insira a base: "))
h = int(input("Insira a altura: "))
print("A área do triângulo é: %.2f" % a(b,h))

##############
# Exercício 7
# Resumo: 
def calculo (dividendo, divisor):
    quociente = 0
    while dividendo >= 0:
        dividendo -= divisor
        quociente += 1
    if dividendo < 0:
        resto = dividendo + divisor
        quociente -= 1
        print("O quociente é:",quociente)
        print("O resto é:",resto)
dividendo = int(input("Digite o valor do dividendo: "))
divisor = int(input("Digite o valor do divisor: "))
calculo (dividendo, divisor)

# Exercício 8
# Resumo:
lista = []
def numeros(a,b,c):
    global lista
    um = max(a,b,c)
    tres = min(a,b,c)
    if um != a and tres != a:
        dois = a
    elif um != b and tres != b:
        dois = b
    else:
        dois = c
    lista.append(um)
    lista.append(dois)
    lista.append(tres)

I = int(input("Digite o valor de I: "))
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

numeros(A,B,C)
if I == 1:
    print("{0},{1},{2}".format(lista[2],lista[1],lista[0]))
elif I == 2:
    print("{0},{1},{2}".format(lista[0],lista[1],lista[2]))
elif I == 3:
    print("{0},{1},{2}".format(lista[1],lista[0],lista[2]))
else:
    print("Valor inválido!")