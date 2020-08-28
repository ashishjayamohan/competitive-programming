def isGood(year):
    lint = list(str(year))
    lint2 = set(lint)
    if(len(lint2) == len(lint)):
        return True
    else:
        return False
year = int(input()) + 1
while(isGood(year) == False):
    year += 1
print(str(year))
