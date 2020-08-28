num = int(input())
line = list(input())
a = 0
d = 0
for i in line:
    if(i == "D"):
        d += 1
    else:
        a += 1
if(a > d):
    print("Anton")
elif(d > a):
    print("Danik")
else:
    print("Friendship")
