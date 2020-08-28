n = input()
line = [~int(i) for i in input().split()]
answer = 1
for j in line:
    temp = answer & j
    answer = temp
if(answer == 1):
    print("EASY")
else:
    print("HARD")
