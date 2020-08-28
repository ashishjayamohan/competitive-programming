line = [int(i) for i in input().split("+")]
line.sort()
answer = ""
for x in range(len(line)):
    if(x!=len(line)-1):
        answer += str(line[x]) + "+"
    else:
        answer+=str(line[x])
print(answer)
