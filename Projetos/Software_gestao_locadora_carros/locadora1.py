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

mostar_lista_de_carros(carros)

#interface que vai se comunicar com o programa
while True:
    os.system('clear') #limpa a tela antes
    print('=========')
    print('Bem vindo a locadora de carros 🚗🚓🚐🚙')
    print('=========')
    print('O oque deseja fazer?')
    print('0 - Mostrar portifolio | 1 - Alugar um carro | 2 - Devolver um carro')
    op = int(input())  #pedir para o usuario dar algo
   
    os.system('clear') #limpa a tela antes
    #mostrar coisas p o usuario depois que ele selecionar algo
    if op == 0:
        pass #palavra reservada do py para nao estragar o prog
    
    elif op == 1:
        pass
    
    elif op == 2:
        pass
    
    print()
    #perg p usuario
    print("")
    print('==============')
    print('Digite: 0 para CONTINUAR | 1 para SAIR')
    if float(input()) == 1: # se for 1 ele da um break, ele nao volta para while
        break


