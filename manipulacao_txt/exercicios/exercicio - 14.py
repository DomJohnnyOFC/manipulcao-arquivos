def gerenciar_tarefas():
    tarefas = []

    # Carregar tarefas existentes
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                tarefa = linha.strip()

                if tarefa:
                    tarefas.append(tarefa)

    except FileNotFoundError:
        # Se o arquivo não existir, ele será criado quando
        # uma tarefa for adicionada.
        pass

    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")

            tarefas.append(tarefa)

            with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                for tarefa in tarefas:
                    arquivo.write(tarefa + "\n")

            print("Tarefa adicionada!")

        elif opcao == "2":
            if len(tarefas) == 0:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\nTarefas:")

                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i} - {tarefa}")

        elif opcao == "3":
            if len(tarefas) == 0:
                print("Nenhuma tarefa para remover.")
            else:
                print("\nTarefas:")

                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i} - {tarefa}")

                numero = int(input("Digite o número da tarefa que deseja remover: "))

                if numero >= 1 and numero <= len(tarefas):
                    tarefas.pop(numero - 1)

                    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                        for tarefa in tarefas:
                            arquivo.write(tarefa + "\n")

                    print("Tarefa removida!")
                else:
                    print("Número de tarefa inválido.")

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


gerenciar_tarefas()

#Usei ajuda para fazer este exercicio pois estava meio dificil para mim