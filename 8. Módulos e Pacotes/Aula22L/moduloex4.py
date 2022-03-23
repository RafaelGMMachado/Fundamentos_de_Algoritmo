def ordenar (palavras):
    palavras = sorted(palavras.split("-"))
    n_palavras = ""
    for n in range ( len(palavras) ):
        if n == len(palavras) - 1:
            n_palavras = n_palavras + str(palavras[n])
        else:
            n_palavras = n_palavras + str(palavras[n]) + "-"
    return n_palavras
def calcular (palavras):
    palavras = palavras.replace("-", "")
    minusculas = 0
    maiusculas = 0
    for n in range ( len(palavras) ):
        if palavras[n].isupper():
            maiusculas += 1
        else:
            minusculas += 1
    print("Maiúsculas =",maiusculas)
    print("Minúsculas =",minusculas)