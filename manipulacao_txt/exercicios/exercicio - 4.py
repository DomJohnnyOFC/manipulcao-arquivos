def contar_linhas():
    contador = 0

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            contador += 1

    print(f"O arquivo possui {contador} linhas.")


contar_linhas()