# criar um script para colocar todos os arquivos em pasta ordenadas em pastas

import os

# %%
cwd = os.getcwd()  # obtém o diretório atual
print("Diretório atual:", cwd)  # exibe o diretório atual

# %%
# full lista (full_list variavel) de todos arquivos dentro dessa pasta
full_list = os.listdir(cwd)
print("Full List file:", full_list)
# %%
# tb separar os arq py, usando copreesao em lista
# que seja somente arquivos e que os arquivos .py nao esteja presente nessa string de codigo
# se tem substring dentro dela '.py' not in i => 'text' in 'teste' # False porque nao esta dentro de text, USANDO TUPLE  and not i.endswith(('.py', '.ipynb'))]
# se fosse so file py o comando seria: files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]
files_list = [i for i in full_list if os.path.isfile(i) and not i.endswith(('.py', '.ipynb'))]
#print("files_list: ", files_list)

# %%
# preciso saber os tipos na lista final, pegando somente a extensao
types = [i.split('.')[1] for i in files_list]
# essa logica types = [i for i in files_list]
#'teste09.docx'.split('.')[1]  #'docx' pega o segundo elemento
#'teste09.docx'.split('.')  # ['teste09', 'docx']
print("types: ", types)


# %%
