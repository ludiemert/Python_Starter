# Jogo da velha (Tic-Tac-Toe)
# O projeto tem 1 classe principal.
# O jogador será 'X' e o computador 'O'.

import random
import os  # Para limpar o terminal (cls no Windows, clear no Unix)

# Classe principal do jogo
class TicTacToe:
    def __init__(self):
        self.reset()  # Inicializa o tabuleiro ao criar o objeto

    def reset(self):
        # Cria um tabuleiro vazio 3x3
        self.board = [[" ", " ", " "] for _ in range(3)]
        self.done = ""  # Estado do jogo: "" (em andamento), "X", "O", ou "D" (empate)

    def print_board(self):
        # Mostra o tabuleiro formatado no terminal
        print("\nTabuleiro atual:")
        for i in range(3):
            print(" " + " | ".join(self.board[i]))
            if i < 2:
                print("---+---+---")

    def check_win_or_draw(self):
        # Verifica condições de vitória ou empate
        for player in ["X", "O"]:
            # Verifica linhas
            for row in self.board:
                if row.count(player) == 3:
                    self.done = player
                    print(f"{player} venceu! 🥳")
                    return

            # Verifica colunas
            for col in range(3):
                if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                    self.done = player
                    print(f"{player} venceu! 🥳")
                    return

            # Verifica diagonais
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
                self.done = player
                print(f"{player} venceu! 🥳")
                return
            if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
                self.done = player
                print(f"{player} venceu! 🥳")
                return

        # Verifica empate (todos os espaços preenchidos e ninguém ganhou)
        if all(cell != " " for row in self.board for cell in row):
            self.done = "D"
            print("Empate! 🤝")

    def get_player_move(self):
        # Captura jogada do usuário
        while True:
            try:
                x = int(input("Digite a linha (0 a 2): "))
                y = int(input("Digite a coluna (0 a 2): "))

                if not (0 <= x <= 2 and 0 <= y <= 2):
                    print("Coordenadas inválidas. Tente novamente.")
                    continue

                if self.board[x][y] != " ":
                    print("Essa posição já está ocupada. Tente outra.")
                    continue

                self.board[x][y] = "X"
                break

            except ValueError:
                print("Por favor, digite números inteiros válidos.")

    def make_computer_move(self):
        # Jogada aleatória do computador
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if available_moves:
            x, y = random.choice(available_moves)
            self.board[x][y] = "O"


# Instancia o jogo
game = TicTacToe()

# Loop principal do jogo
while True:
    # Resetar e mostrar o tabuleiro inicial
    game.print_board()

    # Jogar enquanto o jogo estiver em andamento
    while game.done == "":
        # Jogador
        game.get_player_move()
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa tela
        game.print_board()
        game.check_win_or_draw()
        if game.done != "":
            break

        # Computador
        game.make_computer_move()
        os.system('cls' if os.name == 'nt' else 'clear')
        game.print_board()
        game.check_win_or_draw()

    # Fim do jogo: perguntar ao jogador se deseja jogar novamente
    try:
        choice = input("Digite 1 para sair ou qualquer tecla para jogar novamente: ")
        if choice == "1":
            print("Jogo encerrado. Obrigado por jogar! 👋")
            break
        else:
            game.reset()
    except:
        game.reset()
