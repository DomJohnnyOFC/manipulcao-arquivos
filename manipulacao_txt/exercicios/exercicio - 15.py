def cadastrar_produtos():
    produtos = []

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            nome, preco, quantidade = linha.split(";")

            produto = {
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            }

            produtos.append(produto)

    return produtos


# Chamada da função
produtos = cadastrar_produtos()

print(produtos)
