# projeto pedra, papel e tesoura

import random
import os

# crirar uma lista com as 3 jogadas
mover = ["Paper", "Stones", "Scissors"]

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

