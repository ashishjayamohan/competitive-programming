t = int(input())
answer = []
for a in range(t):
    counterodd = 0
    countereven = 0
    n = int(input())
    line = [int(i) for i in input().split()]
    for j in range(n):
        if(j%2==1 and line[j]%2==0):
            counterodd += 1
        elif(j%2==0 and line[j]%2==1):
            countereven += 1
    if(countereven != counterodd):
        answer.append(-1)
    else:
        answer.append(counterodd)

for b in answer:
    print(str(b))
