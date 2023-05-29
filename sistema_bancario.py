saldo = 1000
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
print('Olá, bem vindo ao nosso sistema bancário!')
while True:
    resposta = input(
        'O que deseja realizar? [1] Saque - [2]  Depósito - [3] Extrato - [4] Saldo - [5] Sair')
    if resposta == '1':
        valor_do_saque = int(input('Qual valor deseja sacar?'))
        if valor_do_saque <= 500:
            print('Saque realizado com sucesso!')
        else:
            print(
                'Não foi possível realizar o saque, pois o valor ultrapassa o limite dado pelo nosso banco.')

    if resposta == '2':
        valor_depositado = int(input('Qual o valor que deseja depositar?'))
        if valor_depositado <= 1000:
            input('Digite as informações da conta que deseja depositar:')
            confirmaçao = input('Confirma as informações fornecidas? [1] Sim - [2] Não')
            if confirmaçao == '1':
                print('Depósito realizado com sucesso!')
            if confirmaçao == '2':
                print('Retornando ao menu!')

    if resposta == '3':
        print('Seu saldo atual é de R$', (saldo), - 'Seu limite para saque é de R$', (limite), - 'O número de saques realizados hoje foram de', (numero_saques), - 'e o seu limite de saques diários é de', (LIMITE_SAQUES))

    if resposta == '4':
        print(f'Seu saldo atual é de R$ {saldo}')

    if resposta == '5':
        break
