line = input().split()
k = int(line[0])
r = int(line[1])
for a in range(1, 11):
    if(k*a % 10 == 0 or k*a % 10 == r):
        print(str(a))
        break
