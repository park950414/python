def chachong(b):
    counts={}
    for word in b:
        counts[word]=counts.get(word,0)+1
    for word in b:
        if counts[word]==1:
            continue
        else:
            return True
    return False
   
    

a=["1","2","3",'1']
print(chachong(a))
