t = int(input())
def process(arr):
    odd = False
    even = False
    for j in arr:
        if(j % 2 == 0):
            even = True
        else:
            odd = True
    return odd and even
answer = []
for a in range(t):
    n = int(input())
    line = [int(i) for i in input().split()]
    if(sum(line) % 2 == 1):
        answer.append("YES")
    elif(process(line)):
        answer.append("YES")
    else:
        answer.append("NO")
for b in answer:
    print(b)
