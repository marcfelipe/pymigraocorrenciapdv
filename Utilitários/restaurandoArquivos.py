import os,subprocess
FB_GBAK = 'gbak'
FB_PARAMS = [FB_GBAK,'-user','SYSDBA','-pas','masterkey','-c','-v']
backup = []
for folderName, subfolders, filenames in os.walk('c:\\BOUTIQUE2'):    
    for filename in filenames:
        #backup.extend(FB_PARAMS)
        #backup.append(filename)
        #backup.append(filename.replace('.gbk','.fdb'))                      
        #print(filename+' Saída: '+filename.replace('.gbk','.fdb'))
        #subprocess.Popen(backup, shell=True)
        subprocess.Popen(['start','gbak -user SYSDBA -pas masterkey -c -v c:\\BOUTIQUE2\\01\\syspdv_mov01.gbk c:\\BOUTIQUE2\\syspdv_mov.fdb'],shell=False)
        print("encerrado")
