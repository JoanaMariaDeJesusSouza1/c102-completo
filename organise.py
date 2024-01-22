#importando os pacotes
from importlib.resources import path
import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx
#criando variaveis para armazenar os caminhos dos diretorios
from_dir = "C:/Users/jo__a/Downloads"
to_dir = "C:/Users/jo__a/Documents/byjus codes pro/c101 a c 120/c102/PRO_1-1_C102_AtividadeDaProfessora3-main"

# exibindo os arquivos existentes no diretório de origem
list_of_files = os.listdir(from_dir)
print(list_of_files)

# Mova todos os arquivos de imagem da pasta Downloads para outra pasta
# iniciando o processo de copiar/mover os arquivos
for file_name in list_of_files:
  # separando nome e extensão dos arquivos
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

 # verificando a extensão dos arquivos para saber se sao imagens
    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                         # Exemplo path1 : Downloads/nomeImagem1.jpg        
        path2 = to_dir + '/' + "Arquivos_Imagem"                   # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem      
        path3 = to_dir + '/' + "Arquivos_Imagem" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg
        print("path1 " , path1)
        print("path3 ", path3)

        # Verifique se o caminho da pasta/diretório existe antes de mover
        # Caso contrário, crie uma NOVA pasta/diretório, e então mova
            # movendo os arquivos para a nova pasta
        if os.path.exists(path2):
          print(f'Movendo {file_name}...')
         # print("Movendo " + file_name + ".....")

          # Mover de path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print(f'Movendo {file_name}...')
          #print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)

