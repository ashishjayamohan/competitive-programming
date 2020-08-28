n = int(input())
total = 0
counter = 0
line = [int(i) for i in input().split()]
for j in line:
    total += j
    counter += 1
print(str(total/counter))
