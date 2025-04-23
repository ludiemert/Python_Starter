# projeto pedra, papel e tesoura

import random
import os

# crirar uma lista com as 3 jogadas
move_list = ["Paper", "Stones", "Scissors"]

# uma variavel para segurar o placar do jogador e do computador
player_count = 0
computer_count = 0

print("======================")
print("Welcome to the Game 🥰")

# funcao para sempre ficar o print na tela
# funcao que print valores
def main_print():
    print("====================")
    print("\nPLACAR")
    print("You: {}".format(player_count))
    print("Computer: {}".format(computer_count))
    print("\n")
    print("Choose Your Bid: ")
    print("0 - Paper | 1 - Stones | 2 - Scissors")

    # funcao que escolhe um lance do computador
    def select_move(): # nome da funcao
        return random.choice(move_list) # escolhe um elemento da lista de forma aleatoria, pega o move_list e retorna um elemento dessa lista aleatoriamente

    # prox funcao que recebe a jogada do jogador (nos)
    def get_player_move():
        while True: # so eh possivel sair desse while tru se digitar oque eh esperado ()
            try: # proteje o codigo com try
                player_move = int(input()) # converte para inteiro
                if player_move not in[0, 1, 2]: # pergunta se esta dentro da lista que a gente quer, 0,1,2
                    raise # sem ele nao estiver retorna um erro, proteje o programa
                return move_list[player_move] # se ela digitar certo 0,1 ou 2 vem p ca
            except Exception as e:
                print(e)

    # funcao que vai definir quem venceu



