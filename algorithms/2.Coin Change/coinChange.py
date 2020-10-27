# 322. Coin Change
# https://leetcode.com/problems/coin-change/

# Time Limit Exceeded if amount is around 100
def checkCoins(coins, amount) -> int:
    minCoins = amount
    if amount == 0:
        return 0
    if amount in coins:
        return 1
    else:
        for i in range(0, len(coins)):
            if coins[i] <= amount:
                numCoins = 1 + checkCoins(coins, amount - coins[i])
                if numCoins < minCoins:
                    minCoins = numCoins
        return minCoins

# Dynamic approach 1
def checkCoins(coins, amount) -> int:
    dp = [float('inf')]*(amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1 

# Dynamic approach 2
def checkCoins(coins, amount) -> int:
    dp = [0] + [float('inf')]*(amount + 1)
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    
    return dp[-1] if dp[-1] != float('inf') else -1

#using BFS
def checkCoins(coins, amount) -> int:
    if amount == 0:
        return 0
    value1 = [0]
    value2 = []
    visited = [False]*(amount+1)
    visited[0] = True
    count = 0

    while value1:
        count += 1
        for v in value1:
            for coin in coins:
                newval = v + coin
                if newval == amount:
                    return count
                elif newval > amount:
                    continue
                elif not visited[newval]:
                    visited[newval] = True
                    value2.append(newval)
        value1, value2 = value2, []
    return -1
    
# another using BFS
def checkCoins(coins, amount) -> int:
    level = seen = {0}
    number = 0
    while level:
        if amount in level:
            return number
        level = {a+c for a in level for c in coins if a + c <= amount} - seen
        seen |= level
        number += 1
    return -1

# Greedy algorithm 
def checkCoins_test(coins, amount) -> int:
    res = []
    n = len(coins)
    coins.sort()
    i = n - 1

    while i >= 0:
        while amount >= coins[i]:
            amount -= coins[i]
            res.append(coins[i])
        i -= 1
    return -1 if amount != 0 else len(res)


if __name__ == "__main__":
    coins = [2]
    amount = 3
    print(checkCoins_test(coins, amount))
    
                  