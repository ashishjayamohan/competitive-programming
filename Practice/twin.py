numCoins = int(input())
coins = [int(i) for i in input().split()]
coins.sort(reverse=True)
nec = sum(coins)/2
total = 0
ind = 0
while(total <= nec):
    total += coins[ind]
    ind += 1
print(str(ind))
