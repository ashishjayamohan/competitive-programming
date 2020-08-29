t = int(input())
answer = []
for a in range(t):
    line1 = [int(i) for i in input().split()]
    a = line1[0]
    b = line1[1]
    answer.append(str(min(max(2*b,a),max(2*a,b))**2))
for b in answer:
    print(b)
