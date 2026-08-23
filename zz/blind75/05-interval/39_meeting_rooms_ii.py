# 39. Meeting Rooms II (premium) — min-heap of end times = rooms currently in use
# Run: python 39_meeting_rooms_ii.py
# Time: O(n log n). Space: O(n).



import heapq



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
print(minMeetingRooms([[7, 10], [2, 4]]))
