ans = 0
n = int(input())
a = []
h = []
for j in range(n):
    line = [int(i) for i in input().split()]
    h.append(line[0])
    a.append(line[1])
for i in range(n):
    for j in range(n):
        if(i != j and h[i] == a[j]):
            ans += 1
print(str(ans))
