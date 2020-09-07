line = [int(i) for i in input().split()]
ans = True
for a in range(line[0]):
    cur = input().split()
    for b in cur:
        if(b!='B' and b!='W'):
            ans=False
if(ans):
    print("#Black&White")
else:
    print("#Color")
