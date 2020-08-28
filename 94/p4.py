t = int(input())
answers = []
for a in range(t):
    counter = 0
    saver = 0
    saver2 = 0
    n = int(input())
    line = [int(b) for b in input().split()]
    final = {}
    for c in range(len(line)):
        final.update({line[c]:final[line[c]].append(c)})
    print(final)
for bl in answers:
    print(bl)
