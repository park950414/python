def isPrime(n):
    try :
        n=eval(n)
        if n==1 or n==2:
            return True
        for i in range (2,n-1):
            if n%(i+1)==0:
                return False
                break
            else:
                continue
        return True
    except:
        return ("输入数据异常.")

n=input("请输入一个整数:")
print(isPrime(n))
      
        
            
        
