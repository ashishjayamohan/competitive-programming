t = int(input())
def ceildiv(a, b):
    return -(-a // b)
answer = []
for a in range(t):
    answer.append(int(ceildiv(int(input()),2)))
for b in answer:
    print(str(b))
