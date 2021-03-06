import fdb
from listaSQLITEVDA import sqlInsertItevda,sqlSelectAllItevda

def pumpOcorrencia_pdv(bdSource,bdTarget):
    conTarget = fdb.connect(dsn=bdTarget,user='SYSDBA',
                          password='masterkey')
    conSource = fdb.connect(dsn=bdSource,user='SYSDBA',
                          password='masterkey')

    cursorSel = conSource.cursor()

    sqlInsercao = 'insert into ocorrencia_pdv(ID,FUCCOD,FUNCOD,FUNCODAUT,TRNSEQ,CXANUM,TRNDAT,OCODATHOR,OCOVLR,OCODES,OCOTRF)'
    sqlInsercao += ' values(?,?,?,?,?,?,?,?,?,?,?)'
    sqlSel = 'select ID,FUCCOD,FUNCOD,FUNCODAUT,TRNSEQ,CXANUM,TRNDAT,OCODATHOR,OCOVLR,OCODES,OCOTRF from ocorrencia_pdv'

    cursorSel.execute(sqlSel)
    rsSel = cursorSel.fetchall()

    for linhaBD in rsSel:
        cursorIns = conTarget.cursor()
        print('ID adicionado: '+str(linhaBD[0])+' OCOTRF: '+str(linhaBD[10]))
        cursorIns.execute(sqlInsercao,linhaBD)
        conTarget.commit()
        cursorIns.close()
        
def pumpItevdaAllRegisters(bdSource,bdTarget):
    conTarget = fdb.connect(dsn=bdTarget,user='SYSDBA',
                          password='masterkey')
    conSource = fdb.connect(dsn=bdSource,user='SYSDBA',
                          password='masterkey')

    cursorSel = conSource.cursor()
    cursorSel.execute(sqlSelectAllItevda)
    rsSel = cursorSel.fetchall()

    for linhaBD in rsSel:
        cursorIns = conTarget.cursor()
        cursorIns.execute(sqlInsercao,linhaBD)
        conTarget.commit()
        cursorIns.close()        

#The function is not ready yet...Has to implement filter conditions for the cursorSel and further..
def pumpItevdaMissingRegisters(bdSource,bdTarget):
    conTarget = fdb.connect(dsn=bdTarget,user='SYSDBA',
                          password='masterkey')
    conSource = fdb.connect(dsn=bdSource,user='SYSDBA',
                          password='masterkey')

    cursorSel = conSource.cursor()
    cursorSel.execute(sqlSelectAllItevda)
    rsSel = cursorSel.fetchall()

    for linhaBD in rsSel:
        cursorIns = conTarget.cursor()
        cursorIns.execute(sqlInsercao,linhaBD)
        conTarget.commit()
        cursorIns.close()   
print(sqlInsertItevda)
    
