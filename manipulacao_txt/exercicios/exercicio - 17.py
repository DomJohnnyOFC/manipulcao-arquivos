def calcular_estoque():
    produtos = []

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")

            produto = {
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            }

            produtos.append(produto)

    valor_total = 0

    for produto in produtos:
        valor_total += produto["preco"] * produto["quantidade"]

    print(f"Valor total do estoque: R$ {valor_total:.2f}")


calcular_estoque()