n = int(input())
cap = 0
currentBlank = 0
for i in range(n):
    line = input().split()
    off = int(line[0])
    on = int(line[1])
    currentBlank -= off
    currentBlank += on
    if(currentBlank > cap):
        cap = currentBlank
print(str(cap))
