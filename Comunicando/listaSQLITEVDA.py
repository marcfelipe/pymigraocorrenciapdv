#Archive with SQL for tables with many fields

#Performs an insert statement for ITEVDA table
sqlInsertItevda='insert into ITEVDA(ID, TRNSEQ, CXANUM, TRNDAT, LOJCOD, FUNCOD, PROCOD, ITVQTDVDA, ITVVLRUNI, ITVVLRACR \
, ITVVLRDCN, ITVVLRTOT, ITVFUNCAP, ITVFUNPRO, ITVCOMCAP, ITVCOMPRO, ITVCOMVEN, PRVNUM, ITVPRCVDA, ITVBONTIP \
, ITVBONFAT, ITVCOMRED, ITVCTREST, ITVPROCOMP, ITVPRCCST, ITVPRCCSTMED, ITVPRCCSTFIS, ITVTIP, ITVFUNAUT \
, ITVSERPRO, ITVTRBID, ITVTRBSIM, ITVTRBALQ, ITVTRBRED, ITVDCNMGC, ITVTXAENT, ITVTIPPRC, ITVVCCOD, ITVECFTRB \
, ITVSEQ, ITVCOMTIP, ITVTDCCOD, ITVORIPRV, ITVPRMDCNTIP, ITVIAT, ITVSTAPAF, ITVTABA, ITVTABB, ITVCSTPIS \
, ITVCSTCOFINS, ITVALQPIS, ITVALQCOFINS, ITVNCM, ITVNCMEXC, ITVNATUREZA, ITVCSOSN, ITVCFOP, ITVRECVASCOD, \
  ITVPROCODVASILHAME, ITVQTDETROCA, PRMCOD, ITVPRMQTD, ITVSCAN, ITVPROPRCOFE, ITVVLRSER) \
  values(?,?,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? \
  ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? \
  ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? )'

#print(sqlInsertItevda)

#Perform a query with select statement for table ITEVDA without any filter
sqlSelectAllItevda = 'select ID ,TRNSEQ ,CXANUM ,TRNDAT ,LOJCOD ,FUNCOD ,PROCOD ,ITVQTDVDA ,ITVVLRUNI , \
ITVVLRACR ,TVVLRDCN ,ITVVLRTOT ,ITVFUNCAP ,ITVFUNPRO ,ITVCOMCAP ,ITVCOMPRO ,ITVCOMVEN ,PRVNUM \
 ,ITVPRCVDA ,ITVBONTIP ,ITVBONFAT ,ITVCOMRED ,ITVCTREST ,ITVPROCOMP ,ITVPRCCST ,ITVPRCCSTMED \
 ,ITVPRCCSTFIS ,ITVTIP ,ITVFUNAUT ,ITVSERPRO ,ITVTRBID ,ITVTRBSIM ,ITVTRBALQ ,ITVTRBRED \
 ,ITVDCNMGC ,ITVTXAENT ,ITVTIPPRC ,ITVVCCOD ,ITVECFTRB ,ITVSEQ ,ITVCOMTIP ,ITVTDCCOD ,ITVORIPRV \
 ,ITVPRMDCNTIP ,ITVIAT ,ITVSTAPAF ,ITVTABA ,ITVTABB ,ITVCSTPIS ,ITVCSTCOFINS ,ITVALQPIS \
 ,ITVALQCOFINS ,ITVNCM ,ITVNCMEXC ,ITVNATUREZA ,ITVCSOSN ,ITVCFOP ,ITVRECVASCOD ,ITVPROCODVASILHAME \
 ,ITVQTDETROCA ,PRMCOD ,ITVPRMQTD ,ITVSCAN ,ITVPROPRCOFE ,ITVVLRSER from ITEVDA'

#Perform a query with select statement for table ITEVDA
#using foreign key as a filter
sqlSelectItevdaWithFilter = 'select ID ,TRNSEQ ,CXANUM ,TRNDAT ,LOJCOD ,FUNCOD ,PROCOD ,ITVQTDVDA ,ITVVLRUNI , \
ITVVLRACR ,TVVLRDCN ,ITVVLRTOT ,ITVFUNCAP ,ITVFUNPRO ,ITVCOMCAP ,ITVCOMPRO ,ITVCOMVEN ,PRVNUM \
 ,ITVPRCVDA ,ITVBONTIP ,ITVBONFAT ,ITVCOMRED ,ITVCTREST ,ITVPROCOMP ,ITVPRCCST ,ITVPRCCSTMED \
 ,ITVPRCCSTFIS ,ITVTIP ,ITVFUNAUT ,ITVSERPRO ,ITVTRBID ,ITVTRBSIM ,ITVTRBALQ ,ITVTRBRED \
 ,ITVDCNMGC ,ITVTXAENT ,ITVTIPPRC ,ITVVCCOD ,ITVECFTRB ,ITVSEQ ,ITVCOMTIP ,ITVTDCCOD ,ITVORIPRV \
 ,ITVPRMDCNTIP ,ITVIAT ,ITVSTAPAF ,ITVTABA ,ITVTABB ,ITVCSTPIS ,ITVCSTCOFINS ,ITVALQPIS \
 ,ITVALQCOFINS ,ITVNCM ,ITVNCMEXC ,ITVNATUREZA ,ITVCSOSN ,ITVCFOP ,ITVRECVASCOD ,ITVPROCODVASILHAME \
 ,ITVQTDETROCA ,PRMCOD ,ITVPRMQTD ,ITVSCAN ,ITVPROPRCOFE ,ITVVLRSER from ITEVDA \
 where TRNSEQ= ? AND TRNDAT=? AND CXANUM=?'

#Perform a query with select statement for table ITEVDA
#using date field trndat as a filter
sqlSelectItevdaWithDateInterval = 'select ID ,TRNSEQ ,CXANUM ,TRNDAT ,LOJCOD ,FUNCOD ,PROCOD ,ITVQTDVDA ,ITVVLRUNI , \
ITVVLRACR ,TVVLRDCN ,ITVVLRTOT ,ITVFUNCAP ,ITVFUNPRO ,ITVCOMCAP ,ITVCOMPRO ,ITVCOMVEN ,PRVNUM \
 ,ITVPRCVDA ,ITVBONTIP ,ITVBONFAT ,ITVCOMRED ,ITVCTREST ,ITVPROCOMP ,ITVPRCCST ,ITVPRCCSTMED \
 ,ITVPRCCSTFIS ,ITVTIP ,ITVFUNAUT ,ITVSERPRO ,ITVTRBID ,ITVTRBSIM ,ITVTRBALQ ,ITVTRBRED \
 ,ITVDCNMGC ,ITVTXAENT ,ITVTIPPRC ,ITVVCCOD ,ITVECFTRB ,ITVSEQ ,ITVCOMTIP ,ITVTDCCOD ,ITVORIPRV \
 ,ITVPRMDCNTIP ,ITVIAT ,ITVSTAPAF ,ITVTABA ,ITVTABB ,ITVCSTPIS ,ITVCSTCOFINS ,ITVALQPIS \
 ,ITVALQCOFINS ,ITVNCM ,ITVNCMEXC ,ITVNATUREZA ,ITVCSOSN ,ITVCFOP ,ITVRECVASCOD ,ITVPROCODVASILHAME \
 ,ITVQTDETROCA ,PRMCOD ,ITVPRMQTD ,ITVSCAN ,ITVPROPRCOFE ,ITVVLRSER from ITEVDA \
 where TRNDAT>= ? AND TRNDAT<=?'

#Perform a query with select statement for table ITEVDA
#using date field and checkout CXANUM as a filter
sqlSelectItevdaWithDateCxanum = 'select ID ,TRNSEQ ,CXANUM ,TRNDAT ,LOJCOD ,FUNCOD ,PROCOD ,ITVQTDVDA ,ITVVLRUNI , \
ITVVLRACR ,TVVLRDCN ,ITVVLRTOT ,ITVFUNCAP ,ITVFUNPRO ,ITVCOMCAP ,ITVCOMPRO ,ITVCOMVEN ,PRVNUM \
 ,ITVPRCVDA ,ITVBONTIP ,ITVBONFAT ,ITVCOMRED ,ITVCTREST ,ITVPROCOMP ,ITVPRCCST ,ITVPRCCSTMED \
 ,ITVPRCCSTFIS ,ITVTIP ,ITVFUNAUT ,ITVSERPRO ,ITVTRBID ,ITVTRBSIM ,ITVTRBALQ ,ITVTRBRED \
 ,ITVDCNMGC ,ITVTXAENT ,ITVTIPPRC ,ITVVCCOD ,ITVECFTRB ,ITVSEQ ,ITVCOMTIP ,ITVTDCCOD ,ITVORIPRV \
 ,ITVPRMDCNTIP ,ITVIAT ,ITVSTAPAF ,ITVTABA ,ITVTABB ,ITVCSTPIS ,ITVCSTCOFINS ,ITVALQPIS \
 ,ITVALQCOFINS ,ITVNCM ,ITVNCMEXC ,ITVNATUREZA ,ITVCSOSN ,ITVCFOP ,ITVRECVASCOD ,ITVPROCODVASILHAME \
 ,ITVQTDETROCA ,PRMCOD ,ITVPRMQTD ,ITVSCAN ,ITVPROPRCOFE ,ITVVLRSER from ITEVDA \
 where TRNDAT>= ? AND TRNDAT<=? and CXANUM=?'

#Perform a query with select statement for table ITEVDA
#without ID field in resultset
sqlSelectAllItevdaNoID = 'select ID ,TRNSEQ ,CXANUM ,TRNDAT ,LOJCOD ,FUNCOD ,PROCOD ,ITVQTDVDA ,ITVVLRUNI , \
ITVVLRACR ,TVVLRDCN ,ITVVLRTOT ,ITVFUNCAP ,ITVFUNPRO ,ITVCOMCAP ,ITVCOMPRO ,ITVCOMVEN ,PRVNUM \
 ,ITVPRCVDA ,ITVBONTIP ,ITVBONFAT ,ITVCOMRED ,ITVCTREST ,ITVPROCOMP ,ITVPRCCST ,ITVPRCCSTMED \
 ,ITVPRCCSTFIS ,ITVTIP ,ITVFUNAUT ,ITVSERPRO ,ITVTRBID ,ITVTRBSIM ,ITVTRBALQ ,ITVTRBRED \
 ,ITVDCNMGC ,ITVTXAENT ,ITVTIPPRC ,ITVVCCOD ,ITVECFTRB ,ITVSEQ ,ITVCOMTIP ,ITVTDCCOD ,ITVORIPRV \
 ,ITVPRMDCNTIP ,ITVIAT ,ITVSTAPAF ,ITVTABA ,ITVTABB ,ITVCSTPIS ,ITVCSTCOFINS ,ITVALQPIS \
 ,ITVALQCOFINS ,ITVNCM ,ITVNCMEXC ,ITVNATUREZA ,ITVCSOSN ,ITVCFOP ,ITVRECVASCOD ,ITVPROCODVASILHAME \
 ,ITVQTDETROCA ,PRMCOD ,ITVPRMQTD ,ITVSCAN ,ITVPROPRCOFE ,ITVVLRSER from ITEVDA'

#Perform a query with select statement for table ITEVDA
#using foreign key as a filter without ID in resultset
sqlSelectItevdaWithFilterNoID = 'select ID ,TRNSEQ ,CXANUM ,TRNDAT ,LOJCOD ,FUNCOD ,PROCOD ,ITVQTDVDA ,ITVVLRUNI , \
ITVVLRACR ,TVVLRDCN ,ITVVLRTOT ,ITVFUNCAP ,ITVFUNPRO ,ITVCOMCAP ,ITVCOMPRO ,ITVCOMVEN ,PRVNUM \
 ,ITVPRCVDA ,ITVBONTIP ,ITVBONFAT ,ITVCOMRED ,ITVCTREST ,ITVPROCOMP ,ITVPRCCST ,ITVPRCCSTMED \
 ,ITVPRCCSTFIS ,ITVTIP ,ITVFUNAUT ,ITVSERPRO ,ITVTRBID ,ITVTRBSIM ,ITVTRBALQ ,ITVTRBRED \
 ,ITVDCNMGC ,ITVTXAENT ,ITVTIPPRC ,ITVVCCOD ,ITVECFTRB ,ITVSEQ ,ITVCOMTIP ,ITVTDCCOD ,ITVORIPRV \
 ,ITVPRMDCNTIP ,ITVIAT ,ITVSTAPAF ,ITVTABA ,ITVTABB ,ITVCSTPIS ,ITVCSTCOFINS ,ITVALQPIS \
 ,ITVALQCOFINS ,ITVNCM ,ITVNCMEXC ,ITVNATUREZA ,ITVCSOSN ,ITVCFOP ,ITVRECVASCOD ,ITVPROCODVASILHAME \
 ,ITVQTDETROCA ,PRMCOD ,ITVPRMQTD ,ITVSCAN ,ITVPROPRCOFE ,ITVVLRSER from ITEVDA \
 where TRNSEQ= ? AND TRNDAT=? AND CXANUM=?'

#Perform a query with select statement for table ITEVDA
#using date field trndat as a filter without ID field in resultset
sqlSelectItevdaWithDateIntervalNoID = 'select ID ,TRNSEQ ,CXANUM ,TRNDAT ,LOJCOD ,FUNCOD ,PROCOD ,ITVQTDVDA ,ITVVLRUNI , \
ITVVLRACR ,TVVLRDCN ,ITVVLRTOT ,ITVFUNCAP ,ITVFUNPRO ,ITVCOMCAP ,ITVCOMPRO ,ITVCOMVEN ,PRVNUM \
 ,ITVPRCVDA ,ITVBONTIP ,ITVBONFAT ,ITVCOMRED ,ITVCTREST ,ITVPROCOMP ,ITVPRCCST ,ITVPRCCSTMED \
 ,ITVPRCCSTFIS ,ITVTIP ,ITVFUNAUT ,ITVSERPRO ,ITVTRBID ,ITVTRBSIM ,ITVTRBALQ ,ITVTRBRED \
 ,ITVDCNMGC ,ITVTXAENT ,ITVTIPPRC ,ITVVCCOD ,ITVECFTRB ,ITVSEQ ,ITVCOMTIP ,ITVTDCCOD ,ITVORIPRV \
 ,ITVPRMDCNTIP ,ITVIAT ,ITVSTAPAF ,ITVTABA ,ITVTABB ,ITVCSTPIS ,ITVCSTCOFINS ,ITVALQPIS \
 ,ITVALQCOFINS ,ITVNCM ,ITVNCMEXC ,ITVNATUREZA ,ITVCSOSN ,ITVCFOP ,ITVRECVASCOD ,ITVPROCODVASILHAME \
 ,ITVQTDETROCA ,PRMCOD ,ITVPRMQTD ,ITVSCAN ,ITVPROPRCOFE ,ITVVLRSER from ITEVDA \
 where TRNDAT>= ? AND TRNDAT<=?'


#Perform a query with select statement for table ITEVDA
#using date field and checkout CXANUM as a filter
#withou ID field in resultset
sqlSelectItevdaWithDateCxanumNoID = 'select ID ,TRNSEQ ,CXANUM ,TRNDAT ,LOJCOD ,FUNCOD ,PROCOD ,ITVQTDVDA ,ITVVLRUNI , \
ITVVLRACR ,TVVLRDCN ,ITVVLRTOT ,ITVFUNCAP ,ITVFUNPRO ,ITVCOMCAP ,ITVCOMPRO ,ITVCOMVEN ,PRVNUM \
 ,ITVPRCVDA ,ITVBONTIP ,ITVBONFAT ,ITVCOMRED ,ITVCTREST ,ITVPROCOMP ,ITVPRCCST ,ITVPRCCSTMED \
 ,ITVPRCCSTFIS ,ITVTIP ,ITVFUNAUT ,ITVSERPRO ,ITVTRBID ,ITVTRBSIM ,ITVTRBALQ ,ITVTRBRED \
 ,ITVDCNMGC ,ITVTXAENT ,ITVTIPPRC ,ITVVCCOD ,ITVECFTRB ,ITVSEQ ,ITVCOMTIP ,ITVTDCCOD ,ITVORIPRV \
 ,ITVPRMDCNTIP ,ITVIAT ,ITVSTAPAF ,ITVTABA ,ITVTABB ,ITVCSTPIS ,ITVCSTCOFINS ,ITVALQPIS \
 ,ITVALQCOFINS ,ITVNCM ,ITVNCMEXC ,ITVNATUREZA ,ITVCSOSN ,ITVCFOP ,ITVRECVASCOD ,ITVPROCODVASILHAME \
 ,ITVQTDETROCA ,PRMCOD ,ITVPRMQTD ,ITVSCAN ,ITVPROPRCOFE ,ITVVLRSER from ITEVDA \
 where TRNDAT>= ? AND TRNDAT<=? and CXANUM=?'










