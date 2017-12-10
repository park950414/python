string=input("请输入一段字符:")
counts={}
for i in range(len(string)):
    counts[string[i]]=counts.get(string[i],0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=1)
for i in range (10):
    word,count=items[i]
    print("{:<10}{:>5}".format(word,count))
