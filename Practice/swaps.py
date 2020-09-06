t = int(input())
answer = []
for c in range(t):
    line = input().split()
    n = int(line[0])
    k = int(line[1])
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    best = 0
    sum = 0
    for j in a:
        sum += j
    if(sum > best):
        best = sum
    for i in range(k):
        temp = b[n-i-1]
        b[n-i-1] = a[i]
        a[i] = temp
        sum = 0
        for j in a:
            sum += j
        if(sum > best):
            best = sum
    answer.append(best)
for l in answer:
    print(str(l))
