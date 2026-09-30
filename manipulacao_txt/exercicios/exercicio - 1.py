def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)


ler_arquivo("mensagem.txt")