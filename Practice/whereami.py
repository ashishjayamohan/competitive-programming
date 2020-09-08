file = open("whereami.in")
def checksubs(string, n):
    coll = {""}
    ans = True
    for i in range(len(string)-n):
        if(string[i:i+n-1] in coll):
            ans = False
            break
        else:
            coll.add(string[i:i+n-1])
    return ans
n = file.readline()
line = file.readline()
num = 1
ans = checksubs(line, num)
while(ans == False):
    num += 1
    ans = checksubs(line, num)
file1 = open("whereami.out", "w")
file1.write(str(num)+"\n")
