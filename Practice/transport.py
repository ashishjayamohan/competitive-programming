line = input().split()
n = int(line[0])
t = int(line[1])
visited = {0}
line = [int(i) for i in input().split()]
current = 1
while(current != t):
    if(current in visited or current > len(line)):
        print("NO")
        break
    else:
        visited.add(current)
        current += line[current - 1]
if(current == t):
    print("YES")
