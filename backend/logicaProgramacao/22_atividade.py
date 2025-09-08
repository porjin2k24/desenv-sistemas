# pesquisar como alterar e excluir registros do arquivo.txt, e criar um comentario no arquivo do python com a explicação.

# logo abaixo no mesmo arquivo, criar um exemplo de sistema de uma loja de carros, onde tenha um menu no terminal, e tenha as opçoes de cadastrar, listar, alterar e excluir. use as boas práticas de programação.



# ========================================
# COMO ALTERAR E EXCLUIR REGISTROS EM ARQUIVO .TXT
# ========================================
# Para alterar ou excluir registros em um arquivo .txt, é necessário:
# 1. Ler todas as linhas do arquivo;
# 2. Modificar ou excluir a linha desejada;
# 3. Reescrever o conteúdo no arquivo (sobrescrevendo o original).
# Isso acontece porque arquivos .txt não suportam edição direta em posições específicas.

# Abaixo, segue um exemplo de um sistema simples de uma loja de carros.
# O sistema permite cadastrar, listar, alterar e excluir carros registrados em um arquivo texto.
# Utilizamos boas práticas como: funções bem definidas, clareza no código, e separação de responsabilidades.

import os

ARQUIVO = 'carros.txt'

def menu():
    print("\n===== MENU - LOJA DE CARROS =====")
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Alterar carro")
    print("4. Excluir carro")
    print("5. Sair")

def cadastrar_carro():
    modelo = input("Digite o modelo do carro: ")
    marca = input("Digite a marca do carro: ")
    ano = input("Digite o ano do carro: ")

    with open(ARQUIVO, 'a', encoding='utf-8') as f:
        f.write(f"{modelo};{marca};{ano}\n")

    print("Carro cadastrado com sucesso!")

def listar_carros():
    print("\n===== LISTA DE CARROS =====")
    if not os.path.exists(ARQUIVO):
        print("Nenhum carro cadastrado.")
        return

    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        if not linhas:
            print("Nenhum carro cadastrado.")
            return

        for i, linha in enumerate(linhas):
            modelo, marca, ano = linha.strip().split(";")
            print(f"{i+1}. Modelo: {modelo}, Marca: {marca}, Ano: {ano}")

def alterar_carro():
    listar_carros()
    try:
        indice = int(input("Digite o número do carro que deseja alterar: ")) - 1
    except ValueError:
        print("Entrada inválida.")
        return

    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    if 0 <= indice < len(linhas):
        modelo = input("Novo modelo: ")
        marca = input("Nova marca: ")
        ano = input("Novo ano: ")
        linhas[indice] = f"{modelo};{marca};{ano}\n"

        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            f.writelines(linhas)

        print("Carro alterado com sucesso!")
    else:
        print("Carro não encontrado.")

def excluir_carro():
    listar_carros()
    try:
        indice = int(input("Digite o número do carro que deseja excluir: ")) - 1
    except ValueError:
        print("Entrada inválida.")
        return

    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    if 0 <= indice < len(linhas):
        confirmacao = input("Tem certeza que deseja excluir este carro? (s/n): ").lower()
        if confirmacao == 's':
            del linhas[indice]

            with open(ARQUIVO, 'w', encoding='utf-8') as f:
                f.writelines(linhas)

            print("Carro excluído com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Carro não encontrado.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_carro()
        elif opcao == '2':
            listar_carros()
        elif opcao == '3':
            alterar_carro()
        elif opcao == '4':
            excluir_carro()
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


# O que esse sistema faz:

# Cadastra carros num arquivo .txt com formato: modelo;marca;ano

# Lista todos os carros com numeração

# Altera um carro selecionado pelo número

# Exclui um carro também selecionado pelo número

# Usa boas práticas: funções separadas, clareza, tratamento de erros simples, encoding UTF-8, comentários explicativos