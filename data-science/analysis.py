import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
fig = plt.figure()
file = open("total_cases_by_state_territory.csv")
states = []
y_pos = []
br = np.arange(len(states))
confirmed = []
probable = []
for l in file:
    line = l.split(",")
    states.append(line[0])
    if(line[1] != "null\n" and line[1] != "null"):
        y_pos.append(int(line[1]))
    if(line[2] != "null\n" and line[2] != "null"):
        confirmed.append(int(line[2]))
    if(line[3] != "null\n" and line[3] != "null"):
        probable.append(int(line[3]))

ypox = np.arange(0,y_pos[len(y_pos)-1] + 1000,10)
plt.bar(states,y_pos)
plt.yticks(ypox)
plt.xticks(br, states)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()
