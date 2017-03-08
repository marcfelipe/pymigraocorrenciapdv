import os
lista=[]
listaArquivo=[]
for folderName, subfolders, filenames in os.walk('c:\\BOUTIQUE'):    
    for filename in filenames:
      lista.append(folderName+'\\'+filename)
      listaArquivo.append(filename)

for arquivo in listaArquivo:
    print(arquivo)
    comando = 'gbak -c -v '+arquivo
    print(comando)
