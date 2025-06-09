
# %%
import random  # posições aleatórias

# %%
# Criar a classe e a função
class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]

    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso

    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)


# %%
class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo  # 1 - normal / 2 - bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if not espacos:
            return  # Evita erro se não houver espaço livre

        if self.tipo == 1:  # Organizado
            # Verifica se a posição original está vazia
            if self.academia.porta_halteres.get(self.peso) == 0:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                # Se estiver ocupada, usa o primeiro espaço livre
                pos = espacos[0]
                self.academia.devolver_halter(pos, self.peso)
        else:  # Bagunceiro
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)

        self.peso = 0


# %%
# 	Há aleatoriedade no comportamento dos usuários
# toda vez que executar aqui tem valores diferentes, simulacao estocastica
# Simulação de Monte Carlo => Executa milhares ou milhões de repetições. Calcula estatísticas como média, desvio padrão, probabilidade de eventos etc.
#Se você rodasse as 10 sessões de treino milhares de vezes (com diferentes bagunceiros, usuários, ordens), e calculasse a média da porcentagem de caos ou a probabilidade de caos > 50%, AÍ sim estaria usando a técnica Monte Carlo.
#Uma simulação em que há elementos de aleatoriedade.

academia = Academia()

usuarios = [Usuario(1, academia) for _ in range(10)]
usuarios += [Usuario(2, academia) for _ in range(1)]

random.shuffle(usuarios)

for _ in range(10):
    random.shuffle(usuarios)
    for user in usuarios:
        user.iniciar_treino()
    for user in usuarios:
        user.finalizar_treino()

print("Porta-halteres final:", academia.porta_halteres)
print("Porcentagem de caos: {:.2f}%".format(academia.calcular_caos() * 100))


#%%
# calculo media dos senarios finais
academia = Academia()

usuarios = [Usuario(1, academia) for _ in range(10)]
usuarios += [Usuario(2, academia) for _ in range(1)]
random.shuffle(usuarios)

list_chaos = []

for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_chaos += [academia.calcular_caos()]

list_chaos # aparece uma lista com todos valores
#print("Porta-halteres final:", academia.porta_halteres)
#print("Porcentagem de caos: {:.2f}%".format(academia.calcular_caos() * 100))

# %%
# usar uma lib de visualizacao de dados _ seaborn lib de visualiz de dados
academia = Academia()

usuarios = [Usuario(1, academia) for _ in range(10)]
usuarios += [Usuario(2, academia) for _ in range(1)]
random.shuffle(usuarios)

list_chaos = []

for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_chaos += [academia.calcular_caos()]

import seaborn as sns     # seaborn lib de visualiz de dados
# mostrar a distribuicao dessas variaveis
sns.displot(list_chaos)

# %%
#Exemplo para virar Monte Carlo:
#Só se você repetir muitas vezes para estimar média/probabilidade

resultados_caos = []

for _ in range(1000):  # Rodar a simulação 1000 vezes
    academia = Academia()
    usuarios = [Usuario(1, academia) for _ in range(10)]
    usuarios += [Usuario(2, academia) for _ in range(2)]
    random.shuffle(usuarios)

    for _ in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()

    caos = academia.calcular_caos()
    resultados_caos.append(caos)

print("Média de caos após 1000 simulações: {:.2f}%".format(100 * sum(resultados_caos) / len(resultados_caos)))


# %%
