"""
qwertyuiop
asdfghjkl;
zxcvbnm,./
"""
line = list("qwertyuiopasdfghjkl;zxcvbnm,./")
inp = input()
shift = 0
if(inp == "R"):
    shift = -1
else:
    shift = 1
inp = list(input())
answer = ""
for j in inp:
    ind = line.index(j)
    ind += shift
    answer += line[ind]
print(answer)
