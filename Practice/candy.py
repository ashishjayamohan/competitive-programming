def process(n):
    answer = 15.3
    counter = 1
    cur = 1
    while(answer % 1 != 0):
        counter += 2**cur
        answer = n/counter
        cur += 1
    return answer

t = int(input())
answers = []
for a in range(t):
    n = int(input())
    answers.append(str(int(process(n))))
for b in answers:
    print(b)
