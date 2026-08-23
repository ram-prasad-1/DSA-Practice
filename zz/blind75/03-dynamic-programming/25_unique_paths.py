# 25. Unique Paths — pure combinatorics: choose which of the m+n-2 moves go down
# Run: python 25_unique_paths.py
# Time: O(min(m, n)). Space: O(1).



from math import comb



def uniquePaths(m, n):
    return comb(m + n - 2, m - 1)



# DP alternative — Time: O(m*n). Space: O(n).
def uniquePathsDp(m, n):
    row = [1] * n
    for _ in range(m - 1):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]



print(uniquePaths(3, 7))
print(uniquePathsDp(3, 7))
