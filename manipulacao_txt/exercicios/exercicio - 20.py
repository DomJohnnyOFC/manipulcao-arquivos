def carregar_alunos():
    alunos = []

    with open("aluno.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            id_aluno, nome, idade, curso = linha.strip().split(";")

            aluno = {
                "id": int(id_aluno),
                "nome": nome,
                "idade": int(idade),
                "curso": curso
            }

            alunos.append(aluno)

    return alunos


def salvar_alunos(alunos):
    with open("aluno.txt", "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(
                f"{aluno['id']};"
                f"{aluno['nome']};"
                f"{aluno['idade']};"
                f"{aluno['curso']}\n"
            )


def listar_alunos(alunos):
    print("\n===== LISTA DE ALUNOS =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(
                f"{aluno['id']} - "
                f"{aluno['nome']} - "
                f"{aluno['idade']} anos"
            )


def buscar_aluno(alunos):
    id_busca = int(input("Digite o ID: "))

    encontrado = False

    for aluno in alunos:
        if aluno["id"] == id_busca:
            print("\nAluno encontrado:")
            print(aluno["nome"])
            print(f"{aluno['idade']} anos")
            print(aluno["curso"])

            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado!")


def cadastrar_aluno(alunos):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    if len(alunos) == 0:
        novo_id = 1
    else:
        maior_id = 0

        for aluno in alunos:
            if aluno["id"] > maior_id:
                maior_id = aluno["id"]

        novo_id = maior_id + 1

    novo_aluno = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(novo_aluno)

    salvar_alunos(alunos)

    print("Aluno cadastrado com sucesso!")


def remover_aluno(alunos):
    id_remover = int(input("Digite o ID do aluno que deseja remover: "))

    encontrado = False

    for aluno in alunos:
        if aluno["id"] == id_remover:
            alunos.remove(aluno)
            encontrado = True
            break

    if encontrado:
        salvar_alunos(alunos)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado!")


def alterar_aluno(alunos):
    id_alterar = int(input("Digite o ID do aluno que deseja alterar: "))

    encontrado = False

    for aluno in alunos:
        if aluno["id"] == id_alterar:
            print("\nAluno encontrado!")

            novo_nome = input("Novo nome: ")
            nova_idade = int(input("Nova idade: "))
            novo_curso = input("Novo curso: ")

            aluno["nome"] = novo_nome
            aluno["idade"] = nova_idade
            aluno["curso"] = novo_curso

            encontrado = True
            break

    if encontrado:
        salvar_alunos(alunos)
        print("Aluno alterado com sucesso!")
    else:
        print("Aluno não encontrado!")


def sistema_alunos():
    alunos = carregar_alunos()

    while True:
        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_alunos(alunos)

        elif opcao == "2":
            buscar_aluno(alunos)

        elif opcao == "3":
            cadastrar_aluno(alunos)

        elif opcao == "4":
            remover_aluno(alunos)

        elif opcao == "5":
            alterar_aluno(alunos)

        elif opcao == "6":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida!")


sistema_alunos()
