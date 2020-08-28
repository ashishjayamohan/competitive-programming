def isComp(n):
    if (n==1):
        return False
    elif (n==2):
        return False;
    else:
        for x in range(2,n):
            if(n % x==0):
                return True
        return False
n = int(input())
saver = 0
saver2 = 0
for i in range(n):
    if(isComp(i) == True and isComp(n-i) == True):
            saver = i
            saver2 = n-i
            break
print(str(saver) + " " + str(saver2))
