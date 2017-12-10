import jieba
txt=open("红楼梦.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
excludes={"什么","一个","我们",'那里','如今','你们','这里','说道','知道','起来','姑娘'}
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=1)
for i in range (5):
    word,count=items[i]
    print("{:<10}{:>5}".format(word,count))
    
