import csv
from idlelib.pyshell import usage_msg


def criar_csv():
    with open("alunos.csv", "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerow(["Renan", "40", "Python"])
        escritor.writerow(["Moises", "43", "IOT"])
        escritor.writerow(["Rafael", "42", "Eletromecanica"])


# criar_csv()


def salvar_alunos():
    alunos = [
        ["Renan", "40", "Python"],
        ["Moises", "43", "Iot"],
        ["Rafael", "42", "Eletromecanica"],
        ["Rogerio", "23", "JavaScript"],
        ["Maristela", "19", "React"],
        ["Katia", "35", "Java"]
    ]

    with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerows(alunos)


#salvar_alunos()

def ler_csv():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            print(linha[0])

#ler_csv()

def exibir_alunos():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        alunos = csv.DictReader(arquivo)

        for aluno in alunos:
            print(aluno["Curso"])

#exibir_alunos()

def cadastrar_alunos():
    with open("novos_alunos.csv", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.seek(0,2)
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")

        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, curso])

        arquivo.seek(0)
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            print(linha)

#cadastrar_alunos()

def deletar_aluno():
    with open("novos_alunos.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        alunos = list(leitor)

    nome_apagar = input("Digite o nome do aluno que deseja apagar: ")

    with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        cabecalho = ["Nome", "Idade", "Curso"]
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)

        escritor.writeheader()

        for aluno in alunos:
            if aluno["Nome"] != nome_apagar:
                escritor.writerow(aluno)


deletar_aluno()