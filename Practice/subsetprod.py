T = int(input())
while T:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    negs0 = a[-5] * a[-4] * a[-3] * a[-2] * a[-1]
    negs2 = a[0] * a[1] * a[-1] * a[-2] * a[-3]
    negs4 = a[0] * a[1] * a[2] * a[3] * a[-1]
    print(max(negs0, negs2, negs4))
    T -= 1
