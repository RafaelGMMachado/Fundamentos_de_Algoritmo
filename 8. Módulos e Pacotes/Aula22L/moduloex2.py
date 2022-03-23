def crivo (limite):
    primos = [0, 0]
    for n in range(2, limite+1):
        primos.append(n)
    for numero in range( len(primos) ):
        if primos[numero] != 0:
            for teste in range( len(primos) ):
                if primos[numero] != primos[teste] and primos[teste] != 0 and primos[teste] % primos[numero] == 0:
                    primos[teste] = 0
    return primos