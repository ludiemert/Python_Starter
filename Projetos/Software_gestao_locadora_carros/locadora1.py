# start prog = \Software_gestao_locadora_carros> python .\locadora1.py     

import os

#listas, elementos da lista com tupla de informacoes(nome e valor = carro)
carros = [
          ("Chevrolet Tracker", 120),
          ("Chevrolet Onix", 90),
          ("Chevrolet Spin", 150),
          ("Hyundai HB20", 85),
          ("Hyundai Tucson", 120),
          ("Fiat Uno", 60),
          ("Fiat Mobi", 100),
          ("Fiat Pulse", 130)
          ]
alugados = []

#funcao para ver a lista organizada, porque vou repetir varias vezes
def mostar_lista_de_carros(Lista_de_carros):
    for i, car in enumerate(Lista_de_carros):
        #print(i, car) aparece a lista
        print('[{}] {} = R$ {} /dia.'.format(i, car[0], car[1]))

#interface que vai se comunicar com o programa
while True:
    os.system('clear') #limpa a tela antes
    print('=========')
    print('Bem vindo a locadora de carros 🚗🚓🚐🚙')
    print('=========')
    print('O que deseja fazer?')
    print('0 - Mostrar portifolio | 1 - Alugar um carro | 2 - Devolver um carro')
    op = int(input())  #pedir para o usuario dar algo
   
    os.system('clear') #limpa a tela antes
    #mostrar coisas p o usuario depois que ele selecionar algo
    if op == 0: #ver os carros      
        mostar_lista_de_carros(carros) #pass #palavra reservada do py para nao estragar o prog
    
    elif op == 1: # alugar um carro
        mostar_lista_de_carros(carros)
        print('=================')
        print('Escolha o codigo do carro: ')
        cod_car = int(input()) #pega o codigo do carro no input da pessoa
        print('Por quantos dias voce deseja alugar este carro??')
        dias = int(input()) #variavel dias
        os.system("clear")

        print('Voce escolheu {} por {} dias.'.format(carros[cod_car][0], dias)) # codig [0]acesa o carro

        #fazer a conta e ver se a pessoa quer confirmar a locacao
        print('O aluguel totalizaria R$ {}. Deseja alugar?'.format(dias * carros[cod_car][1])) # esse [1] acessa o valor

        print('0 = SIM | 1 = NAO')
        conf = int(input())
        if conf == 0: # se a pessoa quiz o carro, faz um apend e o pop para tirar da lista
            print('Parabens voce alugou o {} por {} dias.'.format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))  #append tira o carro alugado e o pop retorna os outros carros
   
    elif op == 2: #devolucao de carros
        if len(alugados) == 0: # se a lista esta vazia nao tem carros p ser devolvida
            print('Nao ha carros para devolver!!!😉')
        else: # do contrario, tem que devolver algum carro
            print('Segue a lista de carros alugados. Qual voce deseja devolver ?')
            mostar_lista_de_carros(alugados)
            print('')
            print('Escolha o codigo do carro que deseja devolver: ')
            cod = int(input())
            if conf == 0:
                print('Obrigado por devolver o carro {}'.format(alugados[cod][0]))
                carros.append(alugados.pop(cod))
                            
    print()
    #perg p usuario
    print("")
    print('==============')
    print('Digite: 0 para CONTINUAR | 1 para SAIR')
    if float(input()) == 1: # se for 1 ele da um break, ele nao volta para while
        break


