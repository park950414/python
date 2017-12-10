def tianzige(n):
    for i in range(n):
        for j in range(n):
            if i%5==0 and j%5==0:
                print("+ ",end=' ')
            elif i%5==0 and j%5!=0:
                print("- ",end=' ')
            elif i%5!=0 and j%5==0:
                print("| ",end=' ')
            else :
                print("  ",end=' ')
        print("\n")
            
        
def main(n):
    tianzige(5*n+1)


n=eval(input("请输入每行格子个数:"))
main(n)
