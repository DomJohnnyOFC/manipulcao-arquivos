def mostrar_numeros():
    numeros = []

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())
            numeros.append(numero)

    for numero in numeros:
        if numero % 2 == 0:
            print(numero)


mostrar_numeros()