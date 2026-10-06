import csv

# Lista para armazenar os treinadores
treinadores = []

# Leitura do arquivo CSV
with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for treinador in leitor:
        treinadores.append(treinador)


# Menu principal
while True:
    print("\n===== TREINADORES POKÉMON =====")
    print("1 - Listar todos os treinadores")
    print("2 - Buscar treinador pelo nome")
    print("3 - Listar treinadores de uma região")
    print("4 - Mostrar treinador com maior nível")
    print("5 - Mostrar treinador com menor nível")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    # Opção 1
    if opcao == "1":
        print("\n===== TODOS OS TREINADORES =====")

        for treinador in treinadores:
            print(f"Nome: {treinador['nome']}")
            print(f"Região: {treinador['regiao']}")
            print(f"Nível: {treinador['nivel']}")
            print("------------------------")

    # Opção 2
    elif opcao == "2":
        nome = input("Digite o nome do treinador: ")

        encontrado = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                print("\nTreinador encontrado!")
                print(f"Nome: {treinador['nome']}")
                print(f"Região: {treinador['regiao']}")
                print(f"Nível: {treinador['nivel']}")
                encontrado = True

        if not encontrado:
            print("Treinador não encontrado.")

    # Opção 3
    elif opcao == "3":
        regiao = input("Digite a região: ")

        encontrados = False

        print(f"\n===== TREINADORES DA REGIÃO {regiao} =====")

        for treinador in treinadores:
            if treinador["regiao"].lower() == regiao.lower():
                print(f"Nome: {treinador['nome']}")
                print(f"Região: {treinador['regiao']}")
                print(f"Nível: {treinador['nivel']}")
                print("------------------------")
                encontrados = True

        if not encontrados:
            print("Nenhum treinador encontrado nessa região.")

    # Opção 4
    elif opcao == "4":
        if len(treinadores) > 0:
            maior_nivel = treinadores[0]

            for treinador in treinadores:
                if int(treinador["nivel"]) > int(maior_nivel["nivel"]):
                    maior_nivel = treinador

            print("\n===== TREINADOR COM MAIOR NÍVEL =====")
            print(f"Nome: {maior_nivel['nome']}")
            print(f"Região: {maior_nivel['regiao']}")
            print(f"Nível: {maior_nivel['nivel']}")
        else:
            print("Não há treinadores cadastrados.")

    # Opção 5
    elif opcao == "5":
        if len(treinadores) > 0:
            menor_nivel = treinadores[0]

            for treinador in treinadores:
                if int(treinador["nivel"]) < int(menor_nivel["nivel"]):
                    menor_nivel = treinador

            print("\n===== TREINADOR COM MENOR NÍVEL =====")
            print(f"Nome: {menor_nivel['nome']}")
            print(f"Região: {menor_nivel['regiao']}")
            print(f"Nível: {menor_nivel['nivel']}")
        else:
            print("Não há treinadores cadastrados.")

    # Opção 6
    elif opcao == "6":
        print("Programa encerrado.")
        break

    # Opção inválida
    else:
        print("Opção inválida. Escolha uma opção de 1 a 6.")