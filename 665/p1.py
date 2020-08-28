n = int(input())
answers = []
for a in range(n):
    line = input().split()
    ans = 0
    n = int(line[0])
    k = int(line[1])
    if(n < k):
        answers.append(k-n)
    elif(n%2 == k%2):
        answers.append(0)
    else:
        answers.append(1)
for b in answers:
    print(b)
