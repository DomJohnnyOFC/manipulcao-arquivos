def contar_palavras():
    with open("textos.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    palavras = texto.split()

    quantidade = len(palavras)

    print(f"Quantidade de palavras: {quantidade}")


contar_palavras()