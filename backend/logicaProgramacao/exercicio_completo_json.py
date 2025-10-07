import json

# -----------------------
# CRIAR (Cadastrar Pet)
# -----------------------
inventario = []

try:
    with open("petshop.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado. Um novo será criado.")

try:
    id = int(input("Digite o ID do pet: "))
except ValueError:
    print("ID inválido!")
    

nome = input("Digite o nome do pet: ")
raça = input("Digite a raça do pet: ")
sexo = input("Digite o sexo do pet: ")
idade = input("Digite a idade do pet: ")
nome_dono = input("Digite o nome do dono: ")
telefone_dono = input("Digite o telefone do dono: ")

novo_pet = {
    "id": id,
    "nome": nome,
    "raça": raça,
    "sexo": sexo,
    "idade": idade,
    "nome_dono": nome_dono,
    "telefone_dono": telefone_dono
}

inventario.append(novo_pet)

with open("petshop.json", "w") as arquivo:
    json.dump(inventario, arquivo, indent=4)

print("Pet cadastrado com sucesso!")


# Modificar Pet

try:
    with open("petshop.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
    

id_pet_modificar = int(input("Digite o ID do pet para modificar: "))

pet_encontrado = False

for pet in inventario:
    if pet["id"] == id_pet_modificar:
        print("Digite os novos dados (pressione Enter para manter o valor atual):")
        nome = input(f"Nome atual: {pet('nome')}  ") or pet "nome"
        raça = input(f"Raça atual: {pet('raça')}  ") or pet "raça"
        idade = input(f"Idade atual: {pet('idade')}  ") or pet "idade"
        sexo = input(f"Sexo atual: {pet('sexo')}  ") or pet "sexo"
        nome_dono = input(f"Nome do dono atual: {pet('nome_dono')}  ") or pet  "nome_dono"
        telefone_dono = input(f"Telefone do dono atual: {pet('telefone_dono')}  ") or pet "telefone_dono"

        pet("nome") = nome
        pet("raça") = raça
        pet("idade") = idade
        pet("sexo") = sexo
        pet("nome_dono") = nome_dono
        pet("telefone_dono") = telefone_dono

        pet_encontrado = True

        break

if pet_encontrado:
    with open("petshop.json", "w") as arquivo:
        json.dump(inventario, arquivo, indent=4)
    print("Pet atualizado com sucesso!")
else:
    print("Pet com o ID informado não foi encontrado.")


# Remover Pet

try:
    with open("petshop.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
    

id_pet_excluir = int(input("Digite o ID do pet que deseja excluir: "))
novo_inventario = []
pet_excluido = False

for pet in inventario:
    if pet["id"] != id_pet_excluir:
        novo_inventario.append(pet)
    else:
        pet_excluido = True

if pet_excluido:
    with open("petshop.json", "w") as arquivo:
        json.dump(novo_inventario, arquivo, indent=4)
    print("Pet removido com sucesso!")
else:
    print("Pet com o ID informado não foi encontrado.")


#Listar Pets

try:
    with open("petshop.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
    

if not inventario:
    print("Nenhum pet cadastrado.")
else:
    print("\n--- Lista de Pets Cadastrados ---")
    for pet in inventario:
        print(f"\nID: {pet.get('id')}")
        print(f"Nome: {pet.get('nome', 'n/a')}")
        print(f"Raça: {pet.get('raça', 'n/a')}")
        print(f"Idade: {pet.get('idade', 'n/a')}")
        print(f"Sexo: {pet.get('sexo', 'n/a')}")
        print(f"Nome do Dono: {pet.get('nome_dono', 'n/a')}")
        print(f"Telefone do Dono: {pet.get('telefone_dono', 'n/a')}")
