from random import randrange, choice
def letras():
  alphab = ["A", "B", "C", "D", "E","F", "G", "H","I","J","K","L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  #lista para guardar as letras que irao na placa
  letras = []
  #for onde as letras serão, uma a uma, escolhidas aleatoriamente usando  a função choice
  for i in range(4):
    letras.append(choice(alphab))
  return letras
def numeros():
  #lista que armazena os numeros gerados aleatoriamente
  numeros = []
  #for onde os numeros sao gerados aleatoriamente, um a um
  for i in range(3):
    numeros.append(randrange(9))
  return numeros
def placas(num, let):
  placa = []
  #for em que a placa é montada
  for i in range(7):
    if i <=2:
      placa.append(let[i])
    elif i == 3:
      placa.append(num[0])
    elif i == 4:
      placa.append(let[3])
    else:
      placa.append(num[i-4])
  return placa