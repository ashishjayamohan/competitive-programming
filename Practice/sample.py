total = int(input())
def splitcoin(vals, lim, total):
    if(total == 0):
        return 1
    elif(lim <= 0 or total < 0):
        return 0
    else:
        return splitcoin(vals, lim - 1, total) + splitcoin(vals, lim, total - vals[lim-1])
vals = [1, 5, 10, 25]
lim = 4
print(splitcoin(vals, lim, total))
