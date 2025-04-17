# as funcoes agora ficam dentro de os.path
# testes de funcoes do os.path

import os

# %%
# caminho onde estou
os.getcwd()
#'c:\\Users\\user\\Downloads\\Computer_Vision_Py\\Aulas\\3 - Modulo OS - Automacao basica com OS\\Atividades_OS'

# %%
#metotho join mescla informacoes
os.path.join(os.getcwd(), 'pasta')
# os.getcwd() + '/pasta' eh igual o comando

#%%
# retorna apensa a utima pasta do caminho
os.path.basename(os.getcwd()) # seria a pasta OS  - 'Atividades_OS'
# %%
# quebrar a string grande em lista []
os.getcwd().split('/')[-1] # pega a ultima da lista [1]

# %%
# vai quebrar em tupla
os.path.split(os.getcwd())[0]

# %%
# vai retornar tudo que vem antes da pasta
os.path.dirname(os.getcwd())

# %%
curr_dir = os.getcwd() # variavel
os.path.getatime(curr_dir) #tempo da ultima modificacao

# %%
# transformando isso na hora de hoje,
curr_dir = os.getcwd() # variavel
lt = os.path.getatime(curr_dir) #tempo da ultima modificacao, segundo

from datetime import datetime # data
datetime.utcfromtimestamp(lt)
# resposta datetime.datetime(2025, 4, 16, 20, 59, 21, 598870)


# %%
# perguntar se eh arquivo ou pasta
os.path.isfile(curr_dir) # eh arquivo?
# False


# %%
# perguntar se eh diretorio
os.path.isdir(curr_dir)
#True

# %%
