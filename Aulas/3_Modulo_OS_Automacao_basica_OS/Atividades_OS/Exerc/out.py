# tirar todos os arquivos das pastas

# %%
import os

cwd = os.getcwd() # variavel para listar as pastas
print ("Pasta que esta o projeto", cwd)

# acessar e tirar todos os arquivos de dentro das pastas
# listar todas as pastas => folder_list = [i for i in os.listdir(cwd)]
# para garantir que vai ler todos os arquivos, logica se for um diretorio ele passa na logica e faz oque determinar if os.path.isdir(i)]
folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]
print("list das pastas e arquivos do projeto", folder_list)
# mostra a lista de pastas list das pastas e arquivos do projeto ['docx', 'png', 'py', 'txt', 'xlsx', 'yml', 'zip']


# logica para ver as pastas tirar os arquivos das pastas e colocar fora das pastas e deletar a pasta
for folder in folder_list:
  path = os.path.join(cwd, folder)
  print("lista : ", path)

  files = os.listdir(path)
  for file in files:
    from_path = os.path.join(path, file)
    to_path = os.path.join(cwd, file)
    os.replace(from_path, to_path)
  os.rmdir(path)


# %%
