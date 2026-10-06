import csv

# LEITURA DOS ARQUIVOS CSV
treinadores = []
pokemons = []

# Ler treinadores.csv
with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for treinador in leitor:
        treinadores.append(treinador)


# Ler pokemons.csv
with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for pokemon in leitor:
        pokemons.append(pokemon)

# MENU
while True:

    print("\n===== RELATÓRIOS =====")
    print("1 - Relatório de um treinador")
    print("2 - Média de nível dos Pokémon de um treinador")
    print("3 - Média de nível dos Pokémon por tipo")
    print("4 - Quantidade de Pokémon por treinador")
    print("5 - Quantidade de Pokémon por tipo")
    print("6 - Treinadores com nível acima de um valor")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1
    # RELATÓRIO DE UM TREINADOR
    if opcao == "1":

        nome = input("Digite o nome do treinador: ")

        treinador_encontrado = None

        # Procurar o treinador
        for treinador in treinadores:

            if treinador["nome"].lower() == nome.lower():
                treinador_encontrado = treinador
                break

        if treinador_encontrado is None:

            print("Treinador não encontrado.")

        else:

            print("\n===== RELATÓRIO DO TREINADOR =====")

            print(f"Treinador: {treinador_encontrado['nome']}")
            print(f"Região: {treinador_encontrado['regiao']}")
            print(f"Nível do treinador: {treinador_encontrado['nivel']}")

            print("\nPokémon:")

            encontrou_pokemon = False

            for pokemon in pokemons:

                if pokemon["treinador"].lower() == nome.lower():

                    print(
                        f"- {pokemon['nome']} - "
                        f"{pokemon['tipo']} - "
                        f"Nível {pokemon['nivel']}"
                    )

                    encontrou_pokemon = True

            if not encontrou_pokemon:
                print("Nenhum Pokémon cadastrado.")

    # OPÇÃO 2
    # MÉDIA DE NÍVEL DOS POKÉMON
    elif opcao == "2":

        nome = input("Digite o nome do treinador: ")

        treinador_existe = False

        # Verificar se o treinador existe
        for treinador in treinadores:

            if treinador["nome"].lower() == nome.lower():
                treinador_existe = True
                break

        if not treinador_existe:

            print("Treinador não encontrado.")

        else:

            soma = 0
            quantidade = 0

            for pokemon in pokemons:

                if pokemon["treinador"].lower() == nome.lower():

                    nivel = int(pokemon["nivel"])

                    soma += nivel
                    quantidade += 1

            if quantidade == 0:

                print("Esse treinador não possui Pokémon.")

            else:

                media = soma / quantidade

                print("\n===== MÉDIA DOS POKÉMON =====")
                print(f"Treinador: {nome}")
                print(f"Média de nível: {media:.2f}")

    # OPÇÃO 3
    # MÉDIA DE NÍVEL POR TIPO
    elif opcao == "3":

        tipo = input("Digite o tipo do Pokémon: ")

        soma = 0
        quantidade = 0

        for pokemon in pokemons:

            if pokemon["tipo"].lower() == tipo.lower():

                nivel = int(pokemon["nivel"])

                soma += nivel
                quantidade += 1

        if quantidade == 0:

            print("Nenhum Pokémon desse tipo foi encontrado.")

        else:

            media = soma / quantidade

            print("\n===== MÉDIA POR TIPO =====")
            print(f"Tipo: {tipo}")
            print(f"Quantidade: {quantidade}")
            print(f"Média de nível: {media:.2f}")

    # OPÇÃO 4
    # QUANTIDADE DE POKÉMON POR TREINADOR
    elif opcao == "4":

        quantidade_por_treinador = {}

        for pokemon in pokemons:

            treinador = pokemon["treinador"]

            if treinador in quantidade_por_treinador:

                quantidade_por_treinador[treinador] += 1

            else:

                quantidade_por_treinador[treinador] = 1

        # Ordenar do maior para o menor
        resultado = sorted(
            quantidade_por_treinador.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\n===== QUANTIDADE DE POKÉMON POR TREINADOR =====")

        for treinador, quantidade in resultado:

            print(f"{treinador}: {quantidade}")

    # OPÇÃO 5
    # QUANTIDADE DE POKÉMON POR TIPO
    elif opcao == "5":

        quantidade_por_tipo = {}

        for pokemon in pokemons:

            tipo = pokemon["tipo"]

            if tipo in quantidade_por_tipo:

                quantidade_por_tipo[tipo] += 1

            else:

                quantidade_por_tipo[tipo] = 1

        # Ordenar do maior para o menor
        resultado = sorted(
            quantidade_por_tipo.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\n===== QUANTIDADE DE POKÉMON POR TIPO =====")

        for tipo, quantidade in resultado:

            print(f"{tipo}: {quantidade}")

    # OPÇÃO 6
    # TREINADORES ACIMA DE UM NÍVEL
    elif opcao == "6":

        nivel = int(input("Digite o nível mínimo: "))

        encontrados = False

        print(f"\n===== TREINADORES ACIMA DE {nivel} =====")

        for treinador in treinadores:

            nivel_treinador = int(treinador["nivel"])

            if nivel_treinador > nivel:

                print(
                    f"{treinador['nome']} - "
                    f"{treinador['regiao']} - "
                    f"Nível {treinador['nivel']}"
                )

                encontrados = True

        if not encontrados:

            print("Nenhum treinador encontrado.")

    # OPÇÃO 7
    elif opcao == "7":

        print("Programa encerrado.")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("Opção inválida. Escolha uma opção de 1 a 7.")