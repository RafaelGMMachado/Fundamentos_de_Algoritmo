def remover (arquivo):
    arquivo = open(arquivo, "r")
    lista = arquivo.readlines()
    del lista[0]
    for n in range ( len(lista) ):
        lista[n] = lista[n].split(",")
    n = 0
    while n < len(lista):
        if lista[n][3] != "ball":
            del lista[n]
            n -= 1
        n += 1
    for n in range ( len(lista) ):
        del lista[n][2]
        del lista[n][1]
    for n in range ( len(lista) ):
        lista[n] = lista[n][0] + "," + lista[n][1] + "," + lista[n][2] + "," + lista[n][3] + "," + lista[n][4] + "," + lista[n][5]
        print(lista[n])