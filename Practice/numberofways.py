n = int(input())
line = [int(i) for i in input().split()]
cnt = [0 for j in range(100000000)]
s = sum(line)
if(s % 3 != 0):
    print("0")
else:
    s /= 3
    ss = 0
    for i in range(n-1, -1, -1):
        ss += line[i]
        if(ss == s):
            cnt[i] = 1
    for j in range(n-2, -1, -1):
        cnt[j] += cnt[j+1]
    ans = 0
    for k in range(n-2):
        ss += line[k]
        if(ss == s):
            ans += cnt[k+2]
    print(ans)
