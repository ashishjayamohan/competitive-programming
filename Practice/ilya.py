n = int(input())
if n>=0:
	print(n)
else:
	n = -n
	if n%10>((n//10)%10):
		ans = str(n)[:-1]
	else:
		ans = str(n)[:-2]+str(n)[-1]
	if ans=='0':
		print(0)
	else:
		print('-'+ans)
