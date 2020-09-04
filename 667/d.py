t = int(input())
def sumdig(arr, s):
    sum = 0
    for a in arr:
        sum+=int(a)
    if(sum<=s):
        return True
    else:
        return False
answer = []
for a in range(t):
    line = input().split()
    n = int(line[0])
    copn = n
    s = int(line[1])
    copx = list(str(n))
    if(sumdig(copx,s)):
        answer.append(0)
    else:
        while(sumdig(copx,s)!=True):
            copn += 1
            copx = list(str(copn))
        answer.append(copn-n)
for b in answer:
    print(str(b))
