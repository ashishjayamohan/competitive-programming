n = int(input())
m = 0
c = 0
for a in range(n):
    line = input().split()
    if(int(line[0]) > int(line[1])):
        m += 1
    elif(int(line[1]) > int(line[0])):
        c += 1
if(m > c):
    print("Mishka")
elif(c > m):
    print("Chris")
else:
    print("Friendship is magic!^^")
