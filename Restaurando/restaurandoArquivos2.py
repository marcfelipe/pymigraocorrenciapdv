import os,subprocess
FB_GBAK = 'gbak.exe'    #FBCLIENT e GBAK devem estar na mesma pasta
backup = []
#A pasta output deve ser criada no folder digitado motherfucker!!!!
sourceFolder = input('Digite a Pasta: \n')
os.makedirs(sourceFolder+'\\'+'output')
for folderName, subfolders, filenames in os.walk(sourceFolder):    
    for filename in filenames:
        if (filename.endswith('.gbk')):        
            print('executará processo para: '+filename)
            print('Irá gerar o arquivo no caminho: '+os.path.dirname(folderName)+'\\outuput\\'+filename.replace('.gbk','.fdb'))
            print(subprocess.Popen(['gbak.exe','-c',folderName+'\\'+filename, \
                                    os.path.dirname(folderName)+'\\output\\'+filename.replace('.gbk','.fdb'),'-user', \
                                    'SYSDBA','-PASSWORD','masterkey'],shell=False))
print("encerrado")
