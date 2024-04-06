from modules import expense, togain
count = 1
data = []
solicitacao = str(input('do you want to add money or spend?'))
while solicitacao not in 'spendadd':
         escolha = str(input('do you want to add money or spend?'))
if solicitacao == 'spend':
    carteira = float(input('Balance: R$'))
    while True:
            produtos = str(input(f'{count}:')).strip()
            data.append(produtos)
            preco = float(input(f'{count} Price: R$')) 
            count += 1 
            solicitacao = str(input('do you want more?[y/n]')).strip().lower()[0]
            if solicitacao == 'n':
                break
    main = expense(carteira, produtos, preco)
    main.spend()
    print(data)
if 'add' in solicitacao:
    count2 = 1
    while True:
        print('type "stop" to stop')
        carteira2 = float(input('Balance: R$'))
        task_name = input(f'{count2} Task: ')
        receive = float(input(f'{count2} To receive: R$'))
        count2 += 1
        request = str(input('Do want to continue [N/Y]')).strip().lower()[0]
        if request == 'n':
            break

