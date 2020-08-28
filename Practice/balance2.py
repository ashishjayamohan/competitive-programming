a=int(input())
for i in range(a):
	b=int(input())
	if b%4==0:
		print("YES")
		c = []
		for j in range(2, b+1, 2):
			c.append(j)
		k=1
		for j in range(b//2-1):
			c.append(k)
			k+=2
		c.append(sum(c[:b//2+1])-sum(c[b//2+1:])-2)
		print(*c)
	else:
		print("NO")
