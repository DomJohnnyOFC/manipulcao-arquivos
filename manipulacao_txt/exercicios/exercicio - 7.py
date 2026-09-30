def buscar_nome():
    nomes = []

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            nomes.append(nome)

    busca = input("Digite o nome que deseja pesquisar: ")

    if busca in nomes:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")


buscar_nome()