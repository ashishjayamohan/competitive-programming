for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans1=0
    ans2=0
    m=max(arr)+1
    arr.sort()
    s=set(arr)
    for i in arr:
        if ans1==i:
            ans1+=1
        elif ans2==i:
            ans2+=1
    print(ans2+ans1)
