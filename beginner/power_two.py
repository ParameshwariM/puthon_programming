def powerTwo(r):
    if (r==0):
        return False
    while (r!=1):
            if (r%2!=0):
                return False
            r=r//2
             
    return True
num=int(input(""))

if(powerTwo(num)):
    print('Yes')
else:
    print('No')
