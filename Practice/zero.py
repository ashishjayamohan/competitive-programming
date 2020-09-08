t = int(input())
answer = []
for a in range(t):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    line = input().split()
    a = int(line[0])
    b = int(line[1])

    if(2*a <= b):
        answer.append((x+y)*a)
    elif(2*a>b):
        answer.append(y*b+(x-y)*a)
for b in answer:
    print(str(b))
