import csv

# LEITURA DOS ARQUIVOS
treinadores = []
pokemons = []

# Lendo treinadores.csv
with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for treinador in leitor:
        treinadores.append(treinador)

# Lendo pokemons.csv
with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for pokemon in leitor:
        pokemons.append(pokemon)

# MENU
while True:
    print("\n===== POKÉMON DOS TREINADORES =====")
    print("1 - Listar Pokémon de um treinador")
    print("2 - Contar Pokémon de um treinador")
    print("3 - Mostrar Pokémon de maior nível")
    print("4 - Mostrar Pokémon de menor nível")
    print("5 - Listar Pokémon de determinado tipo")
    print("6 - Voltar ao menu")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1
    if opcao == "1":
        nome_treinador = input("Digite o nome do treinador: ")

        # Verifica se o treinador existe
        treinador_existe = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome_treinador.lower():
                treinador_existe = True
                break

        if not treinador_existe:
            print("Treinador não encontrado.")
        else:
            # Lista que armazenará os Pokémon encontrados
            pokemons_treinador = []

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome_treinador.lower():
                    pokemons_treinador.append(pokemon)

            if len(pokemons_treinador) == 0:
                print("Esse treinador não possui Pokémon cadastrados.")
            else:
                print(f"\n===== POKÉMON DE {nome_treinador.upper()} =====")

                for pokemon in pokemons_treinador:
                    print(f"Nome: {pokemon['nome']}")
                    print(f"Tipo: {pokemon['tipo']}")
                    print(f"Nível: {pokemon['nivel']}")
                    print("------------------------")

    # OPÇÃO 2
    elif opcao == "2":
        nome_treinador = input("Digite o nome do treinador: ")

        treinador_existe = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome_treinador.lower():
                treinador_existe = True
                break

        if not treinador_existe:
            print("Treinador não encontrado.")
        else:
            quantidade = 0

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome_treinador.lower():
                    quantidade += 1

            print(
                f"{nome_treinador} possui "
                f"{quantidade} Pokémon."
            )

    # OPÇÃO 3
    elif opcao == "3":
        nome_treinador = input("Digite o nome do treinador: ")

        treinador_existe = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome_treinador.lower():
                treinador_existe = True
                break

        if not treinador_existe:
            print("Treinador não encontrado.")
        else:
            pokemons_treinador = []

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome_treinador.lower():
                    pokemons_treinador.append(pokemon)

            if len(pokemons_treinador) == 0:
                print("Esse treinador não possui Pokémon cadastrados.")
            else:
                maior_nivel = pokemons_treinador[0]

                for pokemon in pokemons_treinador:
                    if int(pokemon["nivel"]) > int(maior_nivel["nivel"]):
                        maior_nivel = pokemon

                print("\n===== POKÉMON DE MAIOR NÍVEL =====")
                print(f"Nome: {maior_nivel['nome']}")
                print(f"Tipo: {maior_nivel['tipo']}")
                print(f"Nível: {maior_nivel['nivel']}")

    # OPÇÃO 4
    elif opcao == "4":
        nome_treinador = input("Digite o nome do treinador: ")

        treinador_existe = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome_treinador.lower():
                treinador_existe = True
                break

        if not treinador_existe:
            print("Treinador não encontrado.")
        else:
            pokemons_treinador = []

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome_treinador.lower():
                    pokemons_treinador.append(pokemon)

            if len(pokemons_treinador) == 0:
                print("Esse treinador não possui Pokémon cadastrados.")
            else:
                menor_nivel = pokemons_treinador[0]

                for pokemon in pokemons_treinador:
                    if int(pokemon["nivel"]) < int(menor_nivel["nivel"]):
                        menor_nivel = pokemon

                print("\n===== POKÉMON DE MENOR NÍVEL =====")
                print(f"Nome: {menor_nivel['nome']}")
                print(f"Tipo: {menor_nivel['tipo']}")
                print(f"Nível: {menor_nivel['nivel']}")

    # OPÇÃO 5
    elif opcao == "5":
        tipo = input("Digite o tipo do Pokémon: ")

        encontrados = []

        for pokemon in pokemons:
            if pokemon["tipo"].lower() == tipo.lower():
                encontrados.append(pokemon)

        if len(encontrados) == 0:
            print("Nenhum Pokémon desse tipo foi encontrado.")
        else:
            print(f"\n===== POKÉMON DO TIPO {tipo.upper()} =====")

            for pokemon in encontrados:
                print(f"Nome: {pokemon['nome']}")
                print(f"Tipo: {pokemon['tipo']}")
                print(f"Nível: {pokemon['nivel']}")
                print(f"Treinador: {pokemon['treinador']}")
                print("------------------------")

    # OPÇÃO 6

    elif opcao == "6":
        print("Voltando ao menu...")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Escolha uma opção de 1 a 6.")