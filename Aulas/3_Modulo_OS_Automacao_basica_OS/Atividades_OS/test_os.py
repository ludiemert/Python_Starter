# PY version 3.9.0

import os
print(os.getcwd())

#string do caminho
# 'c:\\Users\\user\\Downloads\\Computer_Vision_Py\\Aulas\\3 - Modulo OS - Automacao basica com OS\\Atividades_OS'


# %%
print("Essa é uma nova célula!")
# mostra todos os arquivos e dir de onde estou
os.listdir()
# %%
# lista um nivel acima c:\\Users\\user\\Downloads\\Computer_Vision_Py\\Aulas\
#arquivos com . sao arq ocultos
os.listdir('c:\\Users\\user\\Downloads\\Computer_Vision_Py\\Aulas')


# %%
actual_dir = os.getcwd() # uma string que salvei do dir que estava entao volta ela abaixo
# ir para um dir acima
os.chdir('c:\\Users\\user\\Downloads\\Computer_Vision_Py\\Aulas\\')
print(os.getcwd())
# %%
os.chdir(actual_dir) # volta o diretorio que eu estava acima# %%
print(os.getcwd())

# %%
# criar pasta 02
os.mkdir('Past2')
# %%
#renomear um arquivo ou uma pasta
os.rename('teste.txt', 'teste2.txt')

# movimentacao de arquivos usando o rename
# %%
os.rename('Past3', 'Past3/Past2')

# %%
import os
print(os.getcwd())

#%%
os.mkdir('Past3')

# %%
os.makedirs('Past3/Past2', exist_ok=True)


# %%
os.remove('teste2.txt')
# %%
os.rmdir('Past3/Past2')

# %%
# comando system criar comando de desejo, como se fosse um as(apelido)
cmd = 'date'
os.system(cmd)


# %%
os.system(cmd)
# %%



# %%
