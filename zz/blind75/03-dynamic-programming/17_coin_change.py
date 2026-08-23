# 17. Coin Change — fewest coins to make amount
# Run: python 17_coin_change.py
# Time: O(amount * len(coins)). Space: O(amount).



def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[amount] == float('inf') else dp[amount]



print(coinChange([1, 2, 5], 11))
print(coinChange([2], 3))
