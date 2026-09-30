# Modo "r" - Abre o arquivo para leitura
# Modo "w" - Abrepara escrita e apaga o conteúdo existente
# Modo "a" - Adiciona novo conteúdo no final do arquivo
# Modo "x" - Cria um arquivo novo e gera erro se ele já existir

def criar_arquivo():
    # O "with" fecha o arquivo automaticamente
    # O "open()" função para leitura ou escrita de arquivos
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("João\n")
        arquivo.write("Rafael\n")
        arquivo.write("Paulo\n")



#criar_arquivo()

def adicionar_aluno(nome):
    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")

#adicionar_aluno("Neymar")
#adicionar_aluno("Pelé")
#adicionar_aluno("Maradona")


def listar_alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(f"O conteudo do arquivo aluno é: {conteudo}")

#listar_alunos()

def listar_alunos_individual():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            listar_alunos().append(linha.strip())

            nomes_alunos = [nome.strip() for nome in arquivo]

            print(f"Lista de alunos: {listar_alunos()}")

# listar_alunos_individual()


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    with open("cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{idade}\n")

        print("Aluno cadastrado com sucesso!")

#cadastrar_aluno()


def listar_cadastro():
    itens_cadastro = []
    with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(";")

            obj = {
                "nome": nome,
                "idade": idade
            }

            itens_cadastro.append(obj)
            print(f"itens cadastrados: {itens_cadastro}")


listar_cadastro()
