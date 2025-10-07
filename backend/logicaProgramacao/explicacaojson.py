#{} -> Chaves: Definir um objeto -> Ficha de cadastro -> pessoa: nome,cpf,telefone

#[] -> Colchete: Definir uma lista

# Chave/Valor: Chave Descreve o valor  Chave = telefone  Valor = 4499999999

import json

inventario = []

# Tenta carregar o arquivo existente
try:
    with open("loja.json", "r") as arquivo:
        inventario += json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado. Um novo será criado.")

# Coleta dados do usuário
id = int(input("Digite o id do produto:"))
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))

# Cria o novo produto
novo_produto = {
    "id" : id,
    "nome": nome,
    "quantidade": quantidade,
    "preco": preco,
    "em_estoque": quantidade > 0
}

# Adiciona ao inventário
inventario.append(novo_produto)

# Salva no arquivo
with open("loja.json", "w") as arquivo:
    json.dump(inventario, arquivo, indent=4)

print("Produto cadastrado com sucesso!")


id_produto_modificar = int (input("Digite o id para modificar"))
nova_quantidade = int(input("digite a nova quantidade: "))

try:
    with open ("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)

except FileNotFoundError:
    print("Arquivo não Encontrado")

produto_encontrado = False

for produto in inventario:
    if produto["id"] == id_produto_modificar:
        #colocamos a nova quantidade
        produto["quantidade"] = nova_quantidade
        produto["em_estoque"] = nova_quantidade > 0 
        produto_encontrado = True
        break;  

if not produto_encontrado:
    print("o produto com id informado não foi encontrado")

else:
    with open("loja.json","w") as arquivo:
        json.dump(inventario, arquivo , indent = 4)
print("O arquivo foi alterado com sucesso!")



#excluir produtos no json

try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)

exept FileNotFoundError:
    print("Arquivo não encontrado")


novo_inventario = []
produto_excluido = False

id_peoduto_excluir = int(input("digite o  id do produto para excluir "))

for produto in inventario:
    if produto["id"]   != id_produto_excluir
    #se o id for diferente adicionamos  a nova lista novo_inventario.append (produto)

    else:
        print("produto removido com sucesso!!")
        produto_excluido = True


if not produto_excluido:
    print("o id do produto não foi encontrado")

else:
    with open ("loja.json", "w") as arquivo:
        json.dump(novo_inventario, arquivo, indent = 4)
    print("O arquivo foi atualizado, produto removido")

    #listar produtos do arquivo json

try:
    with open ("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)

    if not inventario:
        print("o arquivo está vazio!")

    else:
        print("-----lista de produtos no inventario-----")
        for produto in inventario:
            print(f"\n--produto{produto.get("id")}-")
            print(f"nome:{produto.get("nome_produto", "n/a")}")
            print(f"preço:{produto.get("preco_unitario", 0):.2f}")
            print(f"quantidade:{produto.get("quantidade", 0)}unidades")
            print(f"em estoque:{produto.get("em_estoque")}")

exept FileNotFoundError:
    print("arquivo não encontrado")
