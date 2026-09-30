def listar_aprovados():
    print("Alunos aprovados:")

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")

            nota = float(nota)

            if nota >= 6.0:
                print(f"{nome} - {nota}")


listar_aprovados()