
# -*- CODING: UTF-8 -*- 
 
 

FO= open ("PRICE2016.CSV","R") 
LS= 
for LINE in FO: 
LINE=LINE.REPLACE('\N','') 
LS=LINE.SPLIT(",") 
LNS= 
for S in LS: 
LNS+="{}\T".FORMAT(S) 
print (LNS) 
FO.CLOSE() 
