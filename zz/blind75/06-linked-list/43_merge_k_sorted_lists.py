# 43. Merge K Sorted Lists — heap of list heads
# Run: python 43_merge_k_sorted_lists.py
# Time: O(N log k) for N total nodes across k lists. Space: O(k).



import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out



# index i in the tuple breaks ties so nodes are never compared
def mergeKLists(lists):
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = tail = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next



print(to_list(mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])))
print(to_list(mergeKLists([])))
