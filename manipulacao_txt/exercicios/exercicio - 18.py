def gerenciar_notas():
    alunos = []

    with open("nota.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota1, nota2, nota3 = linha.strip().split(";")

            aluno = {
                "nome": nome,
                "nota1": float(nota1),
                "nota2": float(nota2),
                "nota3": float(nota3)
            }

            alunos.append(aluno)

    for aluno in alunos:
        media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3

        if media >= 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"{aluno['nome']} - Média: {media:.2f} - {situacao}")


gerenciar_notas()