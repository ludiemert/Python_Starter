import random  # Importa a biblioteca para embaralhar os halteres

# =========================
# Classe Academia
# =========================
class Academia:
    def __init__(self):
        # Lista de halteres pares de 10 até 34 (inclusive)
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        # Cria um dicionário vazio onde a chave é a posição e o valor é o haltere
        self.porta_halteres = {}
        # Inicializa o dia com os halteres organizados
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        # Coloca os halteres na posição correta (chave = valor)
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        # Retorna uma lista com todos os halteres disponíveis (que não foram pegos, ou seja, valor diferente de 0)
        return [i for i in self.porta_halteres.values() if i != 0]

    def pegar_haltere(self, peso):
        # Tenta pegar um haltere com o peso solicitado
        if peso not in self.porta_halteres.values():
            return False  # Retorna False se o peso não estiver disponível
        # Encontra a posição do haltere com o peso solicitado
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        # Marca a posição como vazia (0)
        self.porta_halteres[key_halt] = 0
        return True  # Retorna True indicando que conseguiu pegar o haltere

    def devolver_halter(self, pos, peso):
        # Tenta devolver um haltere em uma posição específica
        if pos in self.porta_halteres:
            self.porta_halteres[pos] = peso
            return True
        return False  # Retorna False se a posição não existir

    def calcular_caos(self):
        # Calcula o nível de bagunça (halteres fora da posição original e que não foram pegos)
        num_caos = [i for i, j in self.porta_halteres.items() if i != j and j != 0]
        # Retorna o nível de caos como porcentagem do total de halteres
        return len(num_caos) / len(self.porta_halteres)

    def embaralhar_halteres(self):
        # Pega os valores (pesos dos halteres), embaralha e recria o dicionário com os mesmos índices
        valores = list(self.porta_halteres.values())
        random.shuffle(valores)
        self.porta_halteres = dict(zip(self.porta_halteres.keys(), valores))


# ==============================
# Menu de interação com o usuário
# ==============================
def menu():
    academia = Academia()  # Cria uma nova academia

    while True:
        # Exibe as opções para o usuário
        print("\n=== Menu Academia ===")
        print("1. Listar halteres disponíveis")
        print("2. Pegar haltere")
        print("3. Devolver haltere")
        print("4. Calcular nível de caos")
        print("5. Reiniciar o dia (organizar halteres)")
        print("6. Embaralhar halteres (simular bagunça)")
        print("0. Sair")

        # Lê a escolha do usuário
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Lista os halteres disponíveis
            halteres = academia.listar_halteres()
            print("Halteres disponíveis:", halteres)

        elif escolha == "2":
            # Tenta pegar um haltere de determinado peso
            try:
                peso = int(input("Qual peso deseja pegar? "))
                sucesso = academia.pegar_haltere(peso)
                if sucesso:
                    print(f"Você pegou o haltere de {peso}kg.")
                else:
                    print("Peso não disponível ou já foi pego.")
            except ValueError:
                print("Digite um número válido.")

        elif escolha == "3":
            # Tenta devolver um haltere em uma posição específica
            try:
                pos = int(input("Digite a posição para devolver: "))
                peso = int(input("Digite o peso do haltere: "))
                sucesso = academia.devolver_halter(pos, peso)
                if sucesso:
                    print(f"Haltere de {peso}kg devolvido na posição {pos}.")
                else:
                    print("Posição inválida.")
            except ValueError:
                print("Digite números válidos.")

        elif escolha == "4":
            # Calcula e mostra o nível de desorganização da academia
            caos = academia.calcular_caos()
            print(f"Nível de caos: {caos:.2%}")  # Exibe como porcentagem

        elif escolha == "5":
            # Organiza todos os halteres de volta às suas posições
            academia.reiniciar_o_dia()
            print("Academia organizada! Halteres em seus lugares.")

        elif escolha == "6":
            # Embaralha os halteres (simula bagunça)
            academia.embaralhar_halteres()
            print("Halteres embaralhados!")

        elif escolha == "0":
            # Encerra o programa
            print("Saindo... Até a próxima!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Executa o menu apenas se o arquivo for executado diretamente (não se for importado como módulo)
if __name__ == "__main__":
    menu()
