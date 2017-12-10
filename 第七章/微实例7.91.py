fo=open("C:\\Users\\park\\Desktop\\python\\第七章\\price2016.csv","r")
ls=[]
for line in fo:
    line=line[-1].replace("\n","")
    ls=line.split(",")
    lns=""
    for s in ls:
        lns+="{}\t".format(s)
    print(lns)
fo.close()
