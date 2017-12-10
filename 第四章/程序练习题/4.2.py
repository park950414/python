string=input("请输入一个字符串:")
n=len(string)
count_eng,count_num,count_space,count_other=0,0,0,0
for i in range (n):
    if (string[i-1]>='a'and string[i-1]<='z') or (string[i-1]>='A' and string[i-1]<='Z'):
        count_eng+=1
    elif string[i-1]>='0' and string[i-1]<='9':
        count_num+=1      
    elif string[i-1]==" ":
        count_space+=1  
    else :
        count_other+=1 
print("其中英文字符的个数为{},数字的个数为{},空格的个数为{},其他字符的个数为{}".format(count_eng,count_num,count_space,count_other))
