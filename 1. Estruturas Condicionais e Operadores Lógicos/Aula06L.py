#############################################################################
# Nome: Aula 06 (Laboratório) - Operadores Lógicos e Estruturas Condicionais    
# Autor: Rafael Machado                                               
# Data: 27/08/2021                                                    
# Resumo: Tarefa sobre Operadores Lógicos e Condicionais 
#############################################################################

##############
# Exercício 1
# Resumo: O programa lê uma letra e diz se ela é vogal ou consoante. No caso da letra "y", ele diz que em algumas linguas pode ser vogal e em outras consoante.
#""""
print("Exercício 1")

letra = str(input("Digite a letra desejada: "))

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Essa letra é uma vogal")
elif letra == "y":
    print("Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.")
else:
    print("Essa letra é uma consoante.")

##############
# Exercício 2
# Resumo: O programa recebe um mês e um dia e diz qual estação do ano está associada aquela data.
#""""
print("\nExercício 2")

dia = int(input("Digite o dia desejado: "))
mes = str(input("Digite o mês desejado: "))

if (mes == "março" and dia >= 20) or mes == "abril" or mes == "maio" or (mes == "junho" and dia < 21):
    print("Outono")
elif (mes == "junho" and dia >= 21) or mes == "julho" or mes == "agosto" or (mes == "setembro" and dia < 22):
    print("Inverno")
elif (mes == "setembro" and dia >= 22) or mes == "outubro" or mes == "novembro" or (mes == "dezembro" and dia < 21):
    print("Primavera")
elif (mes == "dezembro" and dia >= 21) or mes == "janeiro" or mes == "fevereiro" or (mes == "março" and dia < 20):
    print("Verão")
else:
    print("Data Inválida!")

##############
# Exercício 3
# Resumo: O programa recebe uma nota em letra e a converte para número. 
#""""
print("\nExercício 3")

nota = str(input("Digite a nota em letra, e o sinal +/-: "))

if nota == "A+" or nota == "A":
    print("{0} é equivalente a 5.0".format (nota))
elif nota == "A-":
    print("{0} é equivalente a 4.5".format (nota))
elif nota == "B+":
    print("{0} é equivalente a 4.0".format (nota))
elif nota == "B":
    print("{0} é equivalente a 3.5".format (nota))
elif nota == "B-":
    print("{0} é equivalente a 3.0".format (nota))
elif nota == "C+":
    print("{0} é equivalente a 2.5".format (nota))
elif nota == "C":
    print("{0} é equivalente a 2.0".format (nota))
elif nota == "C-":
    print("{0} é equivalente a 1.5".format (nota))
elif nota == "D+":
    print("{0} é equivalente a 1.0".format (nota))
elif nota == "D":
    print("{0} é equivalente a 0.5".format (nota))
elif nota == "F":
    print("{0} é equivalente a 0.0".format (nota))
else:
    print("Nota inválida")

##############
# Exercício 4
# Resumo: O programa recebe uma linha e uma coluna do xadrez e identifica se o quadrado naquela coordenada é preto ou branco.
#""""
print("\nExercício 4")

linha = int(input("Digite a linha desejada: "))
coluna = str(input("Digite a coluna desejada: "))

if (coluna == "a" or coluna == "c" or coluna == "e" or coluna == "g") and (linha%2) == 1:
    print("Preto")
elif (coluna == "b" or coluna == "d" or coluna == "f" or coluna == "h") and (linha%2) != 1:
    print("Preto")
else:
    print("Branco")

##############
# Exercício 5
# Resumo: O programa recebe um ano maior que 0 e diz qual animal do zodíaco chinês é associado aquele ano.
#""""
print("\nExercício 5")

ano = int(input("Digite um ano: "))

if ano > 0:
    if (ano%12) == 1:
        animal = "Galo"
    elif (ano%12) == 2:
        animal = "Cachorro"
    elif (ano%12) == 3:
        animal = "Porco"
    elif (ano%12) == 4:
        animal = "Rato"
    elif (ano%12) == 5:
        animal = "Boi"
    elif (ano%12) == 6:
        animal = "Tigre"
    elif (ano%12) == 7:
        animal = "Lebre"
    elif (ano%12) == 8:
        animal = "Dragão"
    elif (ano%12) == 9:
        animal = "Cobra"
    elif (ano%12) == 10:
        animal = "Cavalo"
    elif (ano%12) == 11:
        animal = "Carneiro"
    else:
        animal = "Macaco"
else:
    print("Ano inválido!")
    exit()
print("{0} é o ano do(a) {1}".format (ano, animal))