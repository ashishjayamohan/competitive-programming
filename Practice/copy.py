t = int(input())
answer = []
for a in range(t):
    n = int(input())
    line = set([int(i) for i in input().split()])
    answer.append(len(line))
for b in answer:
    print(str(b))
