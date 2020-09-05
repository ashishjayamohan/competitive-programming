n = int(input())
line = [int(i) for i in input().split()]
one = []
two = []
three = []
for j in range(len(line)):
    if(line[j] == 1):
        one.append(j+1)
    elif(line[j] == 2):
        two.append(j+1)
    else:
        three.append(j+1)
ans = min(len(one),len(two),len(three))
print(str(ans))
if(ans != 0):
    for i in range(ans):
        print(str(one[i]) + " " + str(two[i]) + " " + str(three[i]))
