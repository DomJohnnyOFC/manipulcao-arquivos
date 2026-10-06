import csv

# LEITURA DOS ARQUIVOS
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

    print("\n===== GERADOR DE ARQUIVOS =====")
    print("1 - Listar treinadores")
    print("2 - Gerar CSV de um treinador")
    print("3 - Gerar CSV de todos os treinadores")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1
    # LISTAR TREINADORES
    if opcao == "1":

        print("\n===== TREINADORES =====")

        for treinador in treinadores:

            print(
                f"Nome: {treinador['nome']} | "
                f"Região: {treinador['regiao']} | "
                f"Nível: {treinador['nivel']}"
            )

    # OPÇÃO 2
    # GERAR CSV DE UM TREINADOR
    elif opcao == "2":

        nome_treinador = input("Digite o treinador: ")

        # Procurar o treinador
        treinador_encontrado = False

        for treinador in treinadores:

            if treinador["nome"].lower() == nome_treinador.lower():

                treinador_encontrado = True

                # Guardar o nome correto do arquivo
                nome_correto = treinador["nome"]

                break


        if not treinador_encontrado:

            print("Treinador não encontrado.")

        else:

            # Lista para guardar os Pokémon do treinador
            pokemons_treinador = []

            for pokemon in pokemons:

                if pokemon["treinador"].lower() == nome_treinador.lower():

                    pokemons_treinador.append(pokemon)


            if len(pokemons_treinador) == 0:

                print("Esse treinador não possui Pokémon.")

            else:

                # Criar nome do arquivo
                nome_arquivo = (
                    "pokemons_"
                    + nome_correto.lower().replace(" ", "_")
                    + ".csv"
                )


                # Criar o novo arquivo CSV
                with open(
                    nome_arquivo,
                    "w",
                    newline="",
                    encoding="utf-8"
                ) as arquivo:

                    campos = ["nome", "tipo", "nivel", "treinador"]

                    escritor = csv.DictWriter(
                        arquivo,
                        fieldnames=campos
                    )

                    # Escrever cabeçalho
                    escritor.writeheader()

                    # Escrever os Pokémon
                    escritor.writerows(pokemons_treinador)


                print("\nArquivo gerado com sucesso!")
                print(f"Arquivo: {nome_arquivo}")
                print(
                    f"Quantidade de registros gravados: "
                    f"{len(pokemons_treinador)}"
                )

    # OPÇÃO 3
    # GERAR CSV COM TODOS OS POKÉMON
    # ORDENADOS POR NÍVEL
    elif opcao == "3":

        # Criar uma cópia da lista
        pokemons_ordenados = pokemons.copy()


        # Ordenar pelo nível
        pokemons_ordenados.sort(
            key=lambda pokemon: int(pokemon["nivel"])
        )


        # Criar o arquivo
        with open(
            "todos_pokemons_ordenados.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            campos = ["nome", "tipo", "nivel", "treinador"]

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            # Escrever cabeçalho
            escritor.writeheader()

            # Escrever todos os Pokémon
            escritor.writerows(pokemons_ordenados)


        print("\nArquivo gerado com sucesso!")
        print("Arquivo: todos_pokemons_ordenados.csv")
        print(
            f"Quantidade de registros gravados: "
            f"{len(pokemons_ordenados)}"
        )

    # OPÇÃO 4
    # SAIR
    elif opcao == "4":

        print("Programa encerrado.")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("Opção inválida. Escolha uma opção de 1 a 4.")