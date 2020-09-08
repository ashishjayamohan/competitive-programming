"""
ID: ashishj2
LANG: PYTHON3
TASK: fact4
"""
file = open("fact4.in")
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)
num = int(file.readline())
fin = str(factorial(num))
out = open("fact4.out", "w")
fin2 = list(fin[::-1])
for i in fin2:
    if(i!= "0"):
        out.write(i+"\n")
        break
