print('='*60)
print('Olá, você está na Axiom locadora de carros'.center(60))
print('='*60)
nome = input('Por favor, digite seu nome: ')
portifolio = {'Chevrolet Tracker': 120, 'Chevrolet Onix': 90, 'Chevrolet Spin': 150,
              'Hyundai HB20': 85, 'Hyndai Tucson': 120, 'Fiat Uno': 60, 'Fiat Mobi': 70, 'Fiat Pulse': 130}
carros_alugados = {}


while True:

    print('='*60)
    print(f'Digite o que deseja fazer, {nome}:')
    print('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro')
    operacao = int(input())

    while operacao not in [0, 1, 2]:
        print('Por favor digite alguma das opções do Menu!')
        operacao = int(input())

    if operacao == 0:
        print('[PORTIFÓLIO] Esse é o  nosso portifólio.')
        print('')
        i = 0
        for carro, valor in portifolio.items():
            print(f'[{i}] - {carro} R${valor}/dia')
            i += 1

    elif operacao == 1:
        print('='*60)
        print('[ALUGUEL] Escolha o código de algum de nossos carros disponíveis:')

        for carro, valor in portifolio.items():
            print(f'[{i}] - {carro} R${valor}/dia')
            i += 1

        codigo_carro = int(input())
        while codigo_carro not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            print('Por favor digite alguma das opções do Menu!')
            codigo_carro = int(input())

        print('Escolha por quantos dias deseja alugar:')
        dias = int(input())

        print('='*60)
        print(
            f'Você escolheu {list(portifolio.keys())[codigo_carro]} por {dias} dias')
        valor_aluguel = (list(portifolio.values())[codigo_carro]) * dias
        print(f'O aluguel totalizaria R${valor_aluguel}. Deseja alugar?')
        print('='*60)
        print('0 - SIM | 1 - NÃO')
        comando = int(input())
        while comando not in [0, 1]:
            print('Por favor digite alguma das opções do Menu!')
            comando = int(input())

        if comando == 0:
            print('='*60)
            print(
                f'Parabéns! Você alugou o {list(portifolio.keys())[codigo_carro]}'
            )
            carros_alugados[list(portifolio.keys())[codigo_carro]] = list(
                portifolio.values())[codigo_carro]
            portifolio.pop(list(portifolio.keys())[codigo_carro])

    elif operacao == 2:
        print('='*60)
        print('[DEVOLUÇÃO] Segue a lista de carros alugados, qual você deseja devolver?')
        i = 0
        for carro, valor in carros_alugados.items():
            print(f'[{i}] - {carro} R${valor}/dia')
            i += 1
        print('='*60)
        print('Escolha o código do carro que deseja devolver:')
        devolvercarro = int(input())
        print(
            f'Obrigado por devolver o carro {list(carros_alugados.keys())[devolvercarro]}')
        portifolio[list(carros_alugados.keys())[devolvercarro]] = list(
            carros_alugados.values())[devolvercarro]
        carros_alugados.pop(list(carros_alugados.keys())[devolvercarro])

    print('='*60)
    print('0 - CONTINUAR | 1 - SAIR')

    comando = int(input())
    while comando not in [0, 1]:
        print('Por favor digite alguma das opções do Menu!')
        comando = int(input())

    if comando == 0:
        continue
    else:
        break
