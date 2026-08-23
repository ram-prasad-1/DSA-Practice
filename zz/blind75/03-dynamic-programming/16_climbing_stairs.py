# 16. Climbing Stairs — Fibonacci in disguise
# Run: python 16_climbing_stairs.py
# Time: O(n). Space: O(1).



def climbStairs(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b



print(climbStairs(2))
print(climbStairs(5))
