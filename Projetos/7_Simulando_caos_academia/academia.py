# academia organizada e desorganizada (halteres de academia)
# usou o py 3.9.4 eu estou com 3.13
# %%
import random # posicoes aleatorias

# %%
#criar a classe e a funcao
class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0] # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
        self.porta_halteres = {} # criar o porta halteres, dicionario vazio
        self.reiniciar_o_dia()  # criar funcao

    #definir a funcao e dizer oque ela faz, organiza os halteres
    def reiniciar_o_dia(self):
      self.porta_halteres = {i: i for i in self.halteres}  # usar o dicionario de compreencao

    # metodo para listar alteres
    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i !=0] # retorna todos os halteres disponiveis, uma lista, com os hateres que podem ser pegos
       # se alguem tirar o halter colocar o num 0 na `vaga do halter` executar self.porta_halteres.values() => dict_values([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])
       # so vai pegar os valores qdo o i for diferente de 0

    # funcao de pegar haltere(pegar peso)
    def pegar_haltere(self, peso): # pegar peso
        halt_pos = list(self.porta_halteres.values()) # converter para lista executar o comando: halt_pos = list(self.porta_halteres.values())


# dica para depurar classe
self = Academia()
# %%
