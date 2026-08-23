# 74. Top K Frequent Elements — bucket sort by frequency avoids the log factor of a heap
# Run: python 74_top_k_frequent_elements.py
# Time: O(n). Space: O(n). Heap alternative: O(n log k) time, O(n) space.



from collections import Counter



def topKFrequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, c in count.items():
        buckets[c].append(num)
    res = []
    for c in range(len(nums), 0, -1):
        for num in buckets[c]:
            res.append(num)
            if len(res) == k:
                return res
    return res



print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))
