# 05. Interval — sort first, then sweep or greedily pick by end time
# Run: python 05_interval.py



import heapq



# 35. Insert Interval — skip, merge, then append the rest
# O(n) time, O(n) space for output
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



# 36. Merge Intervals
# O(n log n) time, O(n) space
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



# 37. Non-overlapping Intervals — greedy by earliest end time (activity selection)
# O(n log n) time, O(log n) space for the sort
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



# 38. Meeting Rooms (premium) — can one person attend all?
# O(n log n) time, O(log n) space
def canAttendMeetings(intervals):
    intervals.sort()
    return all(a[1] <= b[0] for a, b in zip(intervals, intervals[1:]))


print(canAttendMeetings([[0, 30], [5, 10]]), canAttendMeetings([[7, 10], [2, 4]]))



# 39. Meeting Rooms II (premium) — min-heap of end times = rooms in use
# O(n log n) time, O(n) space
def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort()
    heap = []
    for s, e in intervals:
        if heap and heap[0] <= s:
            heapq.heapreplace(heap, e)
        else:
            heapq.heappush(heap, e)
    return len(heap)


print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
