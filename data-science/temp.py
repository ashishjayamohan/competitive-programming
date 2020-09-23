import matplotlib.pyplot as plt
y = []
x = []
file = open("GlobalTemperatures.csv")
for lines in file:
    line = lines.split(",")
    if(line[0] > "1900"):
        x.append(line[0])
    if(line[1] != "."):
        y.append(line[1])
plt.bar(x,y)
plt.show()
