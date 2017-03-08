import os
from bdfunction import pumpOcorrencia_pdv

localBDs = input('Digite o caminho do diretorio output:\n')
#localBDTarget = input('Digite o caminho do syspdv_srv.fdb')
retLog = open('resultadoProcessamento.txt','w')
retLog.write('Diretório digitado para varredura output: '+localBDs)
for foldername,subfolders,filenames in os.walk(localBDs):    
    for filename in filenames:
        retLog.write('Arquivo Processado: '+filename)
        bdSource = foldername+'\\'+filename
        print('Processando o banco: '+bdSource)
        pumpOcorrencia_pdv(bdSource,'c:\\syspdv\\syspdv_srv.fdb')

retLog.close()
print('Processo Encerrado')
