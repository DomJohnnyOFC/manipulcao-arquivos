def gerar_relatorio():
    vendas = []

    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(";")

            venda = {
                "vendedor": vendedor,
                "produto": produto,
                "valor": float(valor)
            }

            vendas.append(venda)

    # Exibir todas as vendas
    print("VENDAS:")

    for venda in vendas:
        print(
            f"{venda['vendedor']} - "
            f"{venda['produto']} - "
            f"R$ {venda['valor']:.2f}"
        )

    # Calcular o valor total
    total_vendas = 0

    for venda in vendas:
        total_vendas += venda["valor"]

    print()
    print(f"TOTAL DE VENDAS: R$ {total_vendas:.2f}")

    # Contar quantidade de vendas por vendedor
    quantidade_vendas = {}

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] += 1
        else:
            quantidade_vendas[vendedor] = 1

    print()
    print("Quantidade de vendas:")

    for vendedor, quantidade in quantidade_vendas.items():
        print(f"{vendedor}: {quantidade}")

    # Descobrir o vendedor com maior valor total
    total_por_vendedor = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        if vendedor in total_por_vendedor:
            total_por_vendedor[vendedor] += valor
        else:
            total_por_vendedor[vendedor] = valor

    maior_vendedor = ""
    maior_valor = 0

    for vendedor, valor in total_por_vendedor.items():
        if valor > maior_valor:
            maior_valor = valor
            maior_vendedor = vendedor

    print()
    print(
        f"Maior valor total em vendas: "
        f"{maior_vendedor} - R$ {maior_valor:.2f}"
    )


gerar_relatorio()