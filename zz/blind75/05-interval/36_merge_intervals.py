# 36. Merge Intervals — sort, then extend the last interval while it overlaps
# Run: python 36_merge_intervals.py
# Time: O(n log n). Space: O(n).



def merge(intervals):
    intervals.sort()
    res = []
    for s, e in intervals:
        if res and s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)
        else:
            res.append([s, e])
    return res



print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))
