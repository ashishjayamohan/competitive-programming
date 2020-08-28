number = int(input())
x = 0
y = 0
z = 0
for i in range(number):
    line = input().split()
    x += int(line[0])
    y += int(line[1])
    z += int(line[2])
if(x==0 and y==0 and z==0):
    print("YES")
else:
    print("NO")
