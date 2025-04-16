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
