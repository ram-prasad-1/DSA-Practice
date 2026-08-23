# 02. Best Time to Buy and Sell Stock — max profit from one buy and one later sell
# Run: python 02_best_time_to_buy_and_sell_stock.py
# Time: O(n). Space: O(1).



def maxProfit(prices):
    best, low = 0, float('inf')
    for p in prices:
        low = min(low, p)
        best = max(best, p - low)
    return best



print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
