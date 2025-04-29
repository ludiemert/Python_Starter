import random
import os

# criar uma lista com as 3 jogadas
move_list = ["paper", "stones", "scissors"]  # Lista com as opções possíveis de jogadas

# variáveis para segurar o placar do jogador e do computador
player_count = 0
computer_count = 0

print("======================")
print("Welcome to the Game 🥰")  # Mensagem de boas-vindas

# função que imprime as opções e o placar na tela
def main_print():
    print("====================")
    print("\nPLACAR")  # Mostra o placar
    print("You: {}".format(player_count))  # Placar do jogador
    print("Computer: {}".format(computer_count))  # Placar do computador
    print("\n")
    print("Choose Your Bid: ")  # Pede para o jogador escolher uma jogada
    print("0 - Paper | 1 - Stones | 2 - Scissors")  # Mapeamento das opções

# função que escolhe aleatoriamente a jogada do computador
def select_move():  # nome da função
    return random.choice(move_list)  # escolhe um elemento da lista de forma aleatória

# função que recebe a jogada do jogador
def get_player_move():
    while True:  # loop infinito até receber uma entrada válida
        try:
            player_move = int(input())  # solicita e converte a entrada para inteiro
            if player_move not in [0, 1, 2]:  # verifica se está dentro das opções permitidas
                raise ValueError("Escolha inválida! Digite 0, 1 ou 2.")  # força um erro se for inválido
            return move_list[player_move]  # retorna a jogada correspondente na lista
        except Exception as e:
            print(e)  # mostra o erro e repete o input

# função que define quem venceu a rodada
def select_winner(p_move, c_move):  # recebe a jogada do player e do computador
    global player_count, computer_count  # permite alterar as variáveis globais do placar

    # empate
    if p_move == c_move:
        return "d"  # d de draw (empate)

    # regras para o jogador vencer
    if (p_move == "paper" and c_move == "stones") or \
       (p_move == "stones" and c_move == "scissors") or \
       (p_move == "scissors" and c_move == "paper"):
        player_count += 1
        return "p"  # p de player venceu
    else:
        computer_count += 1
        return "c"  # c de computador venceu

# loop principal do jogo que repete até o jogador decidir parar
again = 1  # variável de controle do jogo
while again == 1:  # enquanto o jogador quiser continuar, again == 1
    main_print()  # exibe menu e placar
    player_move = get_player_move()  # captura jogada do jogador
    computer_move = select_move()  # captura jogada do computador
    winner = select_winner(player_move, computer_move)  # determina vencedor

    # exibe visualmente os resultados da rodada
    print("")
    print("=================")
    print("Sua jogada: {}".format(player_move.upper()))  # mostra a jogada do player em maiúscula
    print("Jogada do computador: {}".format(computer_move.upper()))  # jogada do PC

    # mostra quem venceu
    if winner == "p":
        print("Você venceu 🥳 !!!!")
    elif winner == "c":
        print("Você perdeu 😣 !!!!")
    else:
        print("Empate 🤓⏳🤓 !!!!!")
    print("=================")

    # pergunta se o jogador quer jogar novamente
    while True:
        print("Jogar novamente? 0 - SIM | 1 - NÃO")  # opções de continuação
        try:
            next_game = int(input())  # entrada do jogador
            if next_game == 0:
                break  # sai do loop interno e joga de novo
            elif next_game == 1:
                again = 0  # altera variável para encerrar o jogo
                break
            else:
                print("Escolha inválida! Digite 0 ou 1.")  # entrada não reconhecida
        except:
            print("Entrada inválida! Digite um número.")  # erro de entrada

    # limpa a tela (funciona apenas no Windows)
    os.system("cls")
