def contar_caracteres():
    with open("texto.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    quantidade = len(conteudo)

    print(f"Quantidade de caracteres: {quantidade}")


contar_caracteres()
