n=int(input())
l=[0]+list(map(int,input().split()))
a,j = 0,0
for i in range(1,n+1):
	if l[i]>l[i-1] :
		j+=1
	else:
		a=max(a,j)
		j=1
	a=max(a,j)
print(a)
