
import random  # Para embaralhar halteres aleatoriamente

# Classe que representa uma academia com halteres organizados por peso
class Academia:
    def __init__(self):
        # Lista dos halteres disponíveis (pares de 10 a 34)
        self.halteres = [i for i in range(10, 36, 2)]

        # Dicionário onde a chave é a posição (10, 12, 14...) e o valor é o peso do haltere
        self.porta_halteres = {}

        # Inicializa a academia com os halteres organizados
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        """
        Organiza os halteres nas posições corretas.
        """
        self.porta_halteres = {peso: peso for peso in self.halteres}

    def listar_halteres(self):
        """
        Retorna uma lista com os halteres disponíveis (≠ 0).
        """
        return [peso for peso in self.porta_halteres.values() if peso != 0]

    def pegar_haltere(self, peso):
        """
        Retira o haltere com o peso especificado da posição original.
        """
        if peso not in self.porta_halteres.values():
            raise ValueError(f"Haltere {peso} não está disponível.")

        # Localiza o índice e a chave correspondente
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]

        # Marca a posição como vazia
        self.porta_halteres[key_halt] = 0
        return peso

    def devolver_halter(self, pos, peso):
        """
        Devolve o haltere em uma posição específica (pode estar errada).
        """
        if pos not in self.porta_halteres:
            raise ValueError(f"Posição {pos} inválida.")
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        """
        Calcula o percentual de halteres fora do lugar.
        """
        total = len(self.porta_halteres)
        fora_do_lugar = sum(1 for pos, peso in self.porta_halteres.items() if peso != 0 and pos != peso)
        return round((fora_do_lugar / total) * 100, 2)  # Ex: 23.08%

    def embaralhar_halteres(self):
        """
        Embaralha aleatoriamente os halteres (simula o fim do dia).
        """
        pesos = self.halteres[:]
        random.shuffle(pesos)
        self.porta_halteres = {pos: peso for pos, peso in zip(self.halteres, pesos)}


# Exemplo de uso (teste da classe)
if __name__ == "__main__":
    academia = Academia()

    # Bagunçar os halteres para testar o caos
    academia.embaralhar_halteres()

    # Mostrar estado atual
    print("Estado atual dos halteres:")
    for pos, peso in academia.porta_halteres.items():
        print(f"Posição {pos} → Haltere {peso}")

    # Calcular o caos
    print(f"\nNível de caos: {academia.calcular_caos()}%")

# %%
