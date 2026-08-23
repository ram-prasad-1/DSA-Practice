# 35. Insert Interval — skip what ends before, merge what overlaps, append the rest
# Run: python 35_insert_interval.py
# Time: O(n). Space: O(n) for the output.



def insert(intervals, newInterval):
    res = []
    s, e = newInterval
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < s:
        res.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= e:
        s = min(s, intervals[i][0])
        e = max(e, intervals[i][1])
        i += 1
    res.append([s, e])
    res.extend(intervals[i:])
    return res



print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
