line = input().split()
n = int(line[0])
m = int(line[1])
print(str((n**(m-2))%m))
