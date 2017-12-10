for i in range(11):
    for j in range(11):
        if i%5==0 and j%5==0:
            print("+ ",end=' ')
        elif i%5==0 and j%5!=0:
            print("- ",end=' ')
        elif i%5!=0 and j%5==0:
            print("| ",end=' ')
        else :
            print("  ",end=' ')
    print("\n")
            
        
   
