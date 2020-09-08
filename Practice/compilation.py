n= int(input())
line1 = set([int(i) for i in input().split()])
line2 = set([int(i) for i in input().split()])
line3 = set([int(i) for i in input().split()])
first = []
second = []
for i in line1:
    if(i not in line2):
        first.append(str(i))
for j in line2:
    if(j not in line3):
        second.append(str(j))
print(" ".join(first))
print(" ".join(second))
