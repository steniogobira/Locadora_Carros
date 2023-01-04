print('='*60)
print('Olá, você está na Axiom locadora de carros'.center(60))
print('='*60)
nome = input('Por favor, digite seu nome: ')

portifolio = {'Chevrolet Tracker': 120, 'Chevrolet Onix': 90, 'Chevrolet Spin': 150,
              'Hyundai HB20': 85, 'Hyndai Tucson': 120, 'Fiat Uno': 60, 'Fiat Mobi': 70, 'Fiat Pulse': 130}
carros_alugados = {}

carros_lista = list(portifolio.keys())
valores_lista = list(portifolio.values())


def mostrar_carros(dicionario):
    i = 0
    for carro, valor in dicionario.items():
        print(f'[{i}] - {carro} R${valor}/dia')
        i += 1


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
        mostrar_carros(portifolio)

    elif operacao == 1:
        print('='*60)
        print('[ALUGUEL] Escolha o código de algum de nossos carros disponíveis:')
        mostrar_carros(portifolio)

        codigo_carro = int(input())
        while codigo_carro not in range(0, ((len(carros_lista)) + 1)):
            print('Por favor digite alguma das opções do Menu!')
            codigo_carro = int(input())

        print('Escolha por quantos dias deseja alugar:')
        dias = int(input())

        print('='*60)
        print(
            f'Você escolheu {carros_lista[codigo_carro]} por {dias} dias'
        )
        valor_aluguel = (valores_lista[codigo_carro]) * dias
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
                f'Parabéns! Você alugou o {carros_lista[codigo_carro]}'
            )
            carros_alugados[carros_lista[codigo_carro]
                            ] = valores_lista[codigo_carro]

            carros_alugados_lista = list(carros_alugados.keys())
            valores_carros_alugados_lista = list(carros_alugados.values())

            portifolio.pop(carros_lista[codigo_carro])

    elif operacao == 2:
        if (len(carros_alugados)) == 0:
            print("Não existem carros alugados")
        else:
            print('='*60)
            print('[DEVOLUÇÃO] Segue a lista de carros alugados, qual você deseja devolver?'
                  )
            mostrar_carros(carros_alugados)

            print('='*60)
            print('Escolha o código do carro que deseja devolver:')
            devolvercarro = int(input())
            while devolvercarro not in range(0, ((len(carros_alugados_lista)) + 1)):
                print('Por favor digite alguma das opções do Menu!')
                devolvercarro = int(input())

            print(
                f'Obrigado por devolver o carro {carros_alugados_lista[devolvercarro]}'
            )
            portifolio[carros_alugados_lista[devolvercarro]
                       ] = valores_carros_alugados_lista[devolvercarro]
            carros_alugados.pop(carros_alugados_lista[devolvercarro])

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
