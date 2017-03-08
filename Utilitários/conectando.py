import fdb

conTarget = fdb.connect(dsn='C:\BOUTIQUE\syspdv_srv.fdb',user='SYSDBA',
                          password='masterkey')

#conSource = fdb.connect(dsn='C:\BOUTIQUE\SYSPDV_MOV0103161.fdb',user='SYSDBA',
#                          password='masterkey')

conSource = fdb.connect(dsn='C:\BOUTIQUE\SYSPDV_MOV0105161.fdb',user='SYSDBA',
                          password='masterkey')

cursorSel = conSource.cursor()

retlog = open('logImportacao.txt','w')

sqlInsercao = 'insert into ocorrencia_pdv(ID,FUCCOD,FUNCOD,FUNCODAUT,TRNSEQ,CXANUM,TRNDAT,OCODATHOR,OCOVLR,OCODES,OCOTRF)'
sqlInsercao += ' values(?,?,?,?,?,?,?,?,?,?,?)'
sqlSel = 'select ID,FUCCOD,FUNCOD,FUNCODAUT,TRNSEQ,CXANUM,TRNDAT,OCODATHOR,OCOVLR,OCODES,OCOTRF from ocorrencia_pdv'

cursorSel.execute(sqlSel)
rsSel = cursorSel.fetchall()

for linhaBD in rsSel:
    cursorIns = conTarget.cursor()
    print('ID adicionado: '+str(linhaBD[0]))
    cursorIns.execute(sqlInsercao,linhaBD)
    conTarget.commit()
    cursorIns.close()
#print(sql)
