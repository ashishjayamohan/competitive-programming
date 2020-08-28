def floor(n):
    return int(n // 1)
n = int(input())
ans = []
for i in range(n):
    num = int(input())
    if(num == 2):
        ans.append(0)
    elif(num%2 == 0):
        ansnum = floor((num-1)/2)
        ans.append(ansnum)
    else:
        ansnum = floor(num/2)
        ans.append(ansnum)
for l in ans:
    print(l)
