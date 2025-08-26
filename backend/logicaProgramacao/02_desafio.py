#criar menu de opçoes e pedir a opção desejada 
#criar função de deposito
#criar função de saque
#criar função de ver saldo
#ao digitiar "sair" encerrar o programa

saldo = 0  # saldo inicial

def deposito():
    global saldo
    valor = float(input("Digite o valor para depósito: R$"))
    if valor > 0:
        saldo += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido.")

def saque():
    global saldo
    valor = float(input("Digite o valor para saque: "))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print("Saque realizado com sucesso.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        print("Valor inválido.")

def ver_saldo():
    print("Seu saldo é: {saldo:.2f}")

while True:
    print("Menu do brenin:")
    print("1 - Depósito foda")
    print("2 - Saque fodinha")
    print("3 - Ver Saldo fodinha")
    print("Digite 'sair' para encerrar.")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        deposito()
    elif opcao == "2":
        saque()
    elif opcao == "3":
        ver_saldo()
    elif opcao.lower() == "sair":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")
	
    