scores = {"Q":9, "R":5, "B":3, "N":3, "P":1}
white = 0
black = 0
for i in range(8):
    line = list(input())
    for j in line:
        if(j != "." and (j in scores or j.upper() in scores)):
            if(j.islower()):
                black += scores[j.upper()]
            else:
                white += scores[j]
if(white>black):
    print("White")
elif(white==black):
    print("Draw")
else:
    print("Black")
