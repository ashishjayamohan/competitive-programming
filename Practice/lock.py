n = int(input())
a = [int(i) for i in list(input())]
b = [int(i) for i in list(input())]
count = 0
for i in range(n):
    count += min(abs(a[i]-b[i]), 10 - abs(a[i]-b[i]))
print(count)
