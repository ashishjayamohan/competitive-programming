t = int(input())
answer = []
for a in range(t):
    n = int(input())
    line = [int(i) for i in input().split()]
    answer.append(max(line)+min(line))
for b in answer:
    print(str(b))
