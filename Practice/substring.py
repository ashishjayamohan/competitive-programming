t = int(input())
answer = []
for a in range(t):
    fin = ""
    line = list(input())
    fin += line[0]
    for b in range(1,len(line)-1,2):
        fin += line[b]
    fin += line[len(line)-1]
    answer.append(fin)
for c in answer:
    print(c)
