line = input().split()
k = int(line[0])
n = int(line[1])
w = int(line[2])
x = 0
for i in range(w):
    x += ((i+1)*k)
if(n >= x):
    print("0")
else:
    answer = x-n
    print(str(answer))
