def makeChange(coins, total):
    if total == 0:
            return 0
    
    n = len(coins)
    ans = []
    i = n - 1
    tmp = total
    coins = sorted(coins)
    while i >= 0:
            while tmp >= coins[i]:
                    tmp -= coins[i]
                    ans.append(coins[i])
            i -= 1
    if tmp != 0:
            return -1

    return len(ans)
