# 38. Meeting Rooms (premium) — can one person attend every meeting?
# Run: python 38_meeting_rooms.py
# Time: O(n log n). Space: O(log n).



def canAttendMeetings(intervals):
    intervals.sort()
    return all(a[1] <= b[0] for a, b in zip(intervals, intervals[1:]))



print(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(canAttendMeetings([[7, 10], [2, 4]]))
