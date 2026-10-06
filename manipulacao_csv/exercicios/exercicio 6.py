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

# FUNÇÃO PARA CALCULAR AS PONTUAÇÕES
def calcular_resultados():

    resultados = []

    for treinador in treinadores:

        nome_treinador = treinador["nome"]

        nivel_treinador = int(treinador["nivel"])

        soma_niveis = 0

        quantidade_pokemons = 0

        # Procurar os Pokémon desse treinador
        for pokemon in pokemons:

            if pokemon["treinador"].lower() == nome_treinador.lower():

                nivel_pokemon = int(pokemon["nivel"])

                soma_niveis += nivel_pokemon

                quantidade_pokemons += 1

        # Calcular pontuação
        pontuacao = nivel_treinador + soma_niveis

        # Criar dicionário
        resultado = {
            "treinador": nome_treinador,
            "regiao": treinador["regiao"],
            "nivel_treinador": nivel_treinador,
            "quantidade_pokemons": quantidade_pokemons,
            "soma_niveis": soma_niveis,
            "pontuacao": pontuacao
        }

        # Adicionar à lista
        resultados.append(resultado)

    return resultados

# MENU
while True:

    print("\n===== CAMPEONATO POKÉMON =====")
    print("1 - Listar treinadores")
    print("2 - Consultar equipe")
    print("3 - Calcular pontuação")
    print("4 - Mostrar classificação")
    print("5 - Gerar arquivo CSV do campeonato")
    print("6 - Sair")

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
    # CONSULTAR EQUIPE
    elif opcao == "2":

        nome = input("Digite o nome do treinador: ")

        treinador_encontrado = None

        # Procurar treinador
        for treinador in treinadores:

            if treinador["nome"].lower() == nome.lower():

                treinador_encontrado = treinador
                break


        if treinador_encontrado is None:

            print("Treinador não encontrado.")

        else:

            print("\n===== EQUIPE =====")

            print(f"Treinador: {treinador_encontrado['nome']}")
            print(f"Região: {treinador_encontrado['regiao']}")
            print(f"Nível: {treinador_encontrado['nivel']}")

            print("\nPokémon da equipe:")

            contador = 1

            encontrou = False

            for pokemon in pokemons:

                if (
                    pokemon["treinador"].lower()
                    == treinador_encontrado["nome"].lower()
                ):

                    print(
                        f"{contador} - "
                        f"{pokemon['nome']} - "
                        f"{pokemon['tipo']} - "
                        f"{pokemon['nivel']}"
                    )

                    contador += 1

                    encontrou = True

            if not encontrou:

                print("Nenhum Pokémon cadastrado.")

    # OPÇÃO 3
    # CALCULAR PONTUAÇÃO
    elif opcao == "3":

        resultados = calcular_resultados()

        print("\n===== PONTUAÇÃO DOS TREINADORES =====")

        for resultado in resultados:

            print(f"\nTreinador: {resultado['treinador']}")
            print(f"Região: {resultado['regiao']}")
            print(
                f"Nível do treinador: "
                f"{resultado['nivel_treinador']}"
            )
            print(
                f"Quantidade de Pokémon: "
                f"{resultado['quantidade_pokemons']}"
            )
            print(
                f"Soma dos níveis dos Pokémon: "
                f"{resultado['soma_niveis']}"
            )
            print(
                f"Pontuação: "
                f"{resultado['pontuacao']}"
            )

    # OPÇÃO 4
    # CLASSIFICAÇÃO
    elif opcao == "4":

        resultados = calcular_resultados()

        # Ordenar pela pontuação, do maior para o menor
        resultados.sort(
            key=lambda resultado: resultado["pontuacao"],
            reverse=True
        )

        print("\n===== CLASSIFICAÇÃO =====")

        posicao = 1

        for resultado in resultados:

            print(
                f"{posicao}º lugar - "
                f"{resultado['treinador']} - "
                f"{resultado['pontuacao']} pontos"
            )

            posicao += 1
    # OPÇÃO 5
    # GERAR CSV
    elif opcao == "5":

        resultados = calcular_resultados()

        # Ordenar pela pontuação
        resultados.sort(
            key=lambda resultado: resultado["pontuacao"],
            reverse=True
        )


        # Criar arquivo CSV
        with open(
            "resultado_campeonato.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            campos = [
                "treinador",
                "regiao",
                "nivel_treinador",
                "quantidade_pokemons",
                "soma_niveis",
                "pontuacao"
            ]

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            # Cabeçalho
            escritor.writeheader()

            # Dados
            escritor.writerows(resultados)


        print("\nArquivo gerado com sucesso!")
        print("Arquivo: resultado_campeonato.csv")
        print(
            f"Quantidade de treinadores: "
            f"{len(resultados)}"
        )

    # OPÇÃO 6
    # SAIR

    elif opcao == "6":

        print("Programa encerrado.")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("Opção inválida. Escolha uma opção de 1 a 6.")