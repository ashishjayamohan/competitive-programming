n = int(input())
line = [int(i) for i in input().split()]
ref = max(line)
total = 0
for i in line:
    total += ref-i
print(str(total))
