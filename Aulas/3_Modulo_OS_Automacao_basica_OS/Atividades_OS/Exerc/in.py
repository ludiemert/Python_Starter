# Criar um script para colocar todos os arquivos em pastas organizadas por extensão
# Arquivos .py e .ipynb devem ficar fora das pastas

# %%
import os       # Módulo para interagir com o sistema de arquivos
import shutil   # Módulo para mover arquivos de forma segura

# 1. Obtém o caminho do diretório atual (onde o script está sendo executado)
cwd = os.getcwd()
print("📁 Diretório atual:", cwd)

# 2. Lista tudo (arquivos e pastas) dentro do diretório atual
full_list = os.listdir(cwd)
print("📄 Lista completa de arquivos e pastas:", full_list)

# 3. Filtra somente os arquivos (ignora pastas), e exclui os arquivos .py e .ipynb
files_list = [
    file for file in full_list
    if os.path.isfile(file) and not file.endswith(('.py', '.ipynb'))
]
print("📃 Arquivos que serão movidos:", files_list)

# 4. Coleta todos os tipos de extensões diferentes encontradas nos arquivos
types = list(set([
    file.rsplit('.', 1)[-1]  # Pega a última parte após o ponto (ex: 'txt')
    for file in files_list if '.' in file
]))
print("📂 Tipos de extensões encontradas:", types)

# 5. Cria uma pasta para cada tipo de extensão encontrada (se ainda não existir)
for file_type in types:
    folder_path = os.path.join(cwd, file_type)  # Caminho: .../txt, .../png, etc.
    os.makedirs(folder_path, exist_ok=True)     # Cria pasta se não existir
    print(f"📁 Pasta criada (ou já existia): {folder_path}")

# 6. Move os arquivos para suas respectivas pastas com base na extensão
for file in files_list:
    from_path = os.path.join(cwd, file)  # Caminho original do arquivo

    # Garante que o arquivo tem extensão
    if '.' in file:
        ext = file.rsplit('.', 1)[-1]  # Pega a extensão do arquivo
    else:
        ext = 'sem_extensao'           # Se não tiver extensão, usa essa pasta

    to_path = os.path.join(cwd, ext, file)  # Caminho de destino

    try:
        shutil.move(from_path, to_path)     # Move o arquivo para a pasta
        print(f"✅ Arquivo movido: {file} → {ext}/")
    except FileNotFoundError:
        # Caso o arquivo já tenha sido movido ou apagado
        print(f"❌ Arquivo não encontrado (talvez já foi movido): {file}")
    except Exception as e:
        # Outro erro qualquer
        print(f"❌ Erro ao mover '{file}': {e}")

# %%
