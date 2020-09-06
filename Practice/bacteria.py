num = int(input())
ans = [int(i) for i in bin(num)[2:]]
sum = 0
for i in ans:
    sum += i
print(str(sum))
