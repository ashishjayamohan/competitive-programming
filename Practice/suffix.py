from collections import deque

n,m=map(int,input().split())
s=list(map(int,input().split()))

ans=deque([0])

dif=[False for i in range(10**5+1)]

for i in range(n-1,-1,-1):
    if not dif[s[i]]:
        ans.appendleft(ans[0]+1)
        dif[s[i]]=True
    else:
        ans.appendleft(ans[0])
print('\n'.join([str(ans[int(input())-1]) for _ in range(m)]))
