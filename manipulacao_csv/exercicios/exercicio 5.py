import csv

# LEITURA DOS ARQUIVOS
pokemons = []
treinadores = []


# Ler pokemons.csv
with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for pokemon in leitor:
        pokemons.append(pokemon)


# Ler treinadores.csv
with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for treinador in leitor:
        treinadores.append(treinador)

# FUNÇÃO PARA VERIFICAR TREINADOR
def treinador_existe(nome):

    for treinador in treinadores:

        if treinador["nome"].lower() == nome.lower():
            return True

    return False

# MENU PRINCIPAL
while True:

    print("\n===== GERENCIADOR DE POKÉMON =====")
    print("1 - Listar Pokémon")
    print("2 - Pesquisar Pokémon")
    print("3 - Adicionar Pokémon")
    print("4 - Alterar nível de um Pokémon")
    print("5 - Remover Pokémon")
    print("6 - Salvar alterações")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1 - LISTAR
    if opcao == "1":

        print("\n===== LISTA DE POKÉMON =====")

        if len(pokemons) == 0:

            print("Nenhum Pokémon cadastrado.")

        else:

            for pokemon in pokemons:

                print(f"Nome: {pokemon['nome']}")
                print(f"Tipo: {pokemon['tipo']}")
                print(f"Nível: {pokemon['nivel']}")
                print(f"Treinador: {pokemon['treinador']}")
                print("------------------------")

    # OPÇÃO 2 - PESQUISAR
    elif opcao == "2":

        nome = input("Digite o nome do Pokémon: ")

        encontrado = False

        for pokemon in pokemons:

            if pokemon["nome"].lower() == nome.lower():

                print("\n===== POKÉMON ENCONTRADO =====")
                print(f"Nome: {pokemon['nome']}")
                print(f"Tipo: {pokemon['tipo']}")
                print(f"Nível: {pokemon['nivel']}")
                print(f"Treinador: {pokemon['treinador']}")

                encontrado = True
                break

        if not encontrado:

            print("Pokémon não encontrado.")

    # OPÇÃO 3 - ADICIONAR
    elif opcao == "3":

        print("\n===== ADICIONAR POKÉMON =====")

        # Nome
        nome = input("Nome: ")

        while nome.strip() == "":
            print("O nome não pode ficar vazio.")
            nome = input("Nome: ")


        # Verificar se o Pokémon já existe
        existe = False

        for pokemon in pokemons:

            if pokemon["nome"].lower() == nome.lower():

                existe = True
                break


        if existe:

            print("Esse Pokémon já está cadastrado.")

        else:

            # Tipo
            tipo = input("Tipo: ")

            while tipo.strip() == "":
                print("O tipo não pode ficar vazio.")
                tipo = input("Tipo: ")


            # Nível
            nivel_valido = False

            while not nivel_valido:

                nivel = input("Nível: ")

                if nivel.isdigit():

                    nivel = int(nivel)

                    if nivel >= 1 and nivel <= 100:

                        nivel_valido = True

                    else:

                        print("O nível deve estar entre 1 e 100.")

                else:

                    print("Digite um número válido.")


            # Treinador
            treinador = input("Treinador: ")

            while not treinador_existe(treinador):

                print("Treinador não encontrado em treinadores.csv.")
                treinador = input("Treinador: ")


            # Criar o novo registro
            novo_pokemon = {
                "nome": nome,
                "tipo": tipo,
                "nivel": str(nivel),
                "treinador": treinador
            }


            # Adicionar à lista
            pokemons.append(novo_pokemon)

            print("Pokémon adicionado com sucesso!")

    # OPÇÃO 4 - ALTERAR NÍVEL
    elif opcao == "4":

        nome = input("Digite o nome do Pokémon: ")

        encontrado = False

        for pokemon in pokemons:

            if pokemon["nome"].lower() == nome.lower():

                encontrado = True

                # Solicitar novo nível
                nivel_valido = False

                while not nivel_valido:

                    novo_nivel = input("Digite o novo nível: ")

                    if novo_nivel.isdigit():

                        novo_nivel = int(novo_nivel)

                        if novo_nivel >= 1 and novo_nivel <= 100:

                            nivel_valido = True

                        else:

                            print("O nível deve estar entre 1 e 100.")

                    else:

                        print("Digite um número válido.")


                # Alterar o nível
                pokemon["nivel"] = str(novo_nivel)

                print("Nível alterado com sucesso!")

                break


        if not encontrado:

            print("Pokémon não encontrado.")

    # OPÇÃO 5 - REMOVER
    elif opcao == "5":

        nome = input("Digite o nome do Pokémon: ")

        encontrado = False

        for pokemon in pokemons:

            if pokemon["nome"].lower() == nome.lower():

                pokemons.remove(pokemon)

                encontrado = True

                print("Pokémon removido com sucesso!")

                break


        if not encontrado:

            print("Pokémon não encontrado.")

    # OPÇÃO 6 - SALVAR
    elif opcao == "6":

        with open(
            "pokemons_atualizados.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            campos = ["nome", "tipo", "nivel", "treinador"]

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            # Cabeçalho
            escritor.writeheader()

            # Registros
            escritor.writerows(pokemons)


        print("\nAlterações salvas com sucesso!")
        print("Arquivo: pokemons_atualizados.csv")
        print(f"Quantidade de Pokémon salvos: {len(pokemons)}")

    # OPÇÃO 7 - SAIR
    elif opcao == "7":

        print("Programa encerrado.")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("Opção inválida. Escolha uma opção de 1 a 7.")