import os
for folderName, subfolders, filenames in os.walk('c:\\BOUTIQUE'):
    print('Diretório atual: '+folderName)

    for subfolder in subfolders:
        print('Sub diretório: '+folderName + ':'+subfolder)

    for filename in filenames:        
        print('Arquivo: '+folderName+':'+filename)

    print('')
