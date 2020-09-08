cal = [int(i) for i in input().split()]
line = [int(j) for j in list(input())]
sum = 0
for k in line:
    sum += cal[k-1]
print(sum)
