# 26. Jump Game — greedy furthest reach
# Run: python 26_jump_game.py
# Time: O(n). Space: O(1).



def canJump(nums):
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True



print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
