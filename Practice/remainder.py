t = int(input())
answer = []
for a in range(t):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    n = int(line[2])
    if(n- n%x + y<= n):
        answer.append(str(n-n%x+y))
    else:
        answer.append(str(n-n%x-(x-y)))
for b in answer:
    print(str(b))
