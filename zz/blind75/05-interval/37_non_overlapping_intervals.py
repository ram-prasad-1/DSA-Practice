# 37. Non-overlapping Intervals — greedy by earliest end time (activity selection)
# Run: python 37_non_overlapping_intervals.py
# Time: O(n log n). Space: O(log n) for the sort.



def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end, removed = float('-inf'), 0
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            removed += 1
    return removed



print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
