def menu_arquivo():
    while True:
        print("\n1 - Ler arquivo")
        print("2 - Adicionar texto")
        print("3 - Sobrescrever arquivo")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            with open("notas.txt", "r", encoding="utf-8") as arquivo:
                print(arquivo.read())

        elif opcao == "2":
            texto = input("Digite o texto que deseja adicionar: ")

            with open("notas.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(texto + "\n")

        elif opcao == "3":
            texto = input("Digite o novo conteúdo: ")

            with open("notas.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(texto + "\n")

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


menu_arquivo()
