menu = """Digite a letra com a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1400
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    print('=' * 88)

    if opcao == "d":
        deposito = -1
        while deposito <= 0:
            deposito = float(input('Qual valor você deseja depositar (ele precisa ser maior que R$ 0,00)? '))
        
        saldo += deposito
        extrato += f'(+) Depósito: R$ {deposito:.2f}\n'
        print(f'Depósito de R$ {deposito:.2f} realizado com sucesso!')
        print('=' * 88)

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input('Qual valor você deseja sacar (ele precisa ser maior que R$ 0,00 e menor ou igual a R$ 500,00)? '))

            if saque > saldo:
                print(f'Você não tem saldo suficiente. Seu saldo é de: R$ {saldo:.2f}')
                numero_saques -= 1
            else:
                while saque <= 0 or saque > 500:
                    saque = -1
                    saque = float(input('Qual valor você deseja sacar (ele precisa ser maior que R$ 0,00 e menor ou igual a R$ 500,00)? '))
                
                saldo -= saque
                extrato += f'(-) Saque: R$ {saque:.2f}\n'
                print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
                print('=' * 88)

        else:
            print(f'Você atingiu o limite de {LIMITE_SAQUES} saques diários. Para mais saques, volte amanhã!')
            print('=' * 88)
            
        numero_saques += 1

    elif opcao == "e":
        print(f'Extrato detalhado:\n\n{extrato}\nSaldo atual: R$ {saldo:.2f}.')
        print('=' * 88)
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        print('=' * 88)