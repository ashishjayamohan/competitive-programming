t = int(input())
answers = []
for a in range(t):
    n = int(input())
    line = [int(i) for i in input().split()]
    line.sort()
    answer = True
    for b in range(1, len(line)):
        if(line[b] - line[b-1] > 1):
            answer = False
            break
    if(answer):
        answers.append("YES")
    else:
        answers.append("NO")
for b in answers:
    print(b)
