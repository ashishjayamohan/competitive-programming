t = int(input())
answer = []
for a in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    k = int(line[2])
    count = 0
    if(k%2==1):
        count -= (b*(k//2))
        count += (a*((k//2) + 1))
    else:
        count -= b*(k//2)
        count += a*(k//2)
    answer.append(count)
for b in answer:
    print(str(int(b)))
