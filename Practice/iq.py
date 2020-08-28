n = int(input())
line = [int(i) for i in input().split()]
countodd = 0
counteven = 0
lastodd = 0
lasteven = 0
for j in range(len(line)):
    if(line[j] % 2 == 0):
        counteven += 1
        lasteven = j+1
    else:
        countodd += 1
        lastodd = j+1
if(countodd>counteven):
    print(str(lasteven))
else:
    print(str(lastodd))
