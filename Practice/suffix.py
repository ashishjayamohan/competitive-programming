line = input().split()
answer = []
n = int(line[0])
m = int(line[1])
line = input().split()
for j in range(m):
    x = int(input())
    cur = set(line[x-1:])
    answer.append(len(cur))

for b in answer:
    print(str(b))
