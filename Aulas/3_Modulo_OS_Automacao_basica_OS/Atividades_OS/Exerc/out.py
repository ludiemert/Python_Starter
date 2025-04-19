# tirar todos os arquivos das pastas

# %%
import os

cwd = os.getcwd() # variavel para listar as pastas
print ("Pasta que esta o projeto", cwd)
# %%
# acessar e tirar todos os arquivos de dentro das pastas
# listar todas as pastas => folder_list = [i for i in os.listdir(cwd)]
folder_list = [i for i in os.listdir(cwd)]
print("list das pastas e arquivos do projeto", folder_list)

# %%
