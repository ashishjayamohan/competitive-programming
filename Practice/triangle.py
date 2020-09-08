t = int(input())
answer = []
for a in range(t):
    line = [int(i) for i in input().split()]
    answer.append(str(line[1]) + " " + str(line[2]) + " " + str(line[2]))
for b in answer:
    print(b)
