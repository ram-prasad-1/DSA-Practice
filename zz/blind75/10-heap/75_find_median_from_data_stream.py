# 75. Find Median from Data Stream
# Run: python 75_find_median_from_data_stream.py
# Time: O(log n) per addNum, O(1) per findMedian. Space: O(n).



import heapq



# lo is a max-heap (negated) of the smaller half, hi a min-heap of the larger half
class MedianFinder:
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num):
        heapq.heappush(self.lo, -heapq.heappushpop(self.hi, num))
        if len(self.lo) > len(self.hi):
            heapq.heappush(self.hi, -heapq.heappop(self.lo))

    def findMedian(self):
        if len(self.hi) > len(self.lo):
            return float(self.hi[0])
        return (self.hi[0] - self.lo[0]) / 2



mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
