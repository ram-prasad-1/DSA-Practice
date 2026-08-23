# 06. Linked List — pointer rewiring, dummy heads, and fast/slow runners
# Run: python 06_linked_list.py



import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(vals):
    dummy = tail = ListNode()
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out



# 40. Reverse a Linked List
# O(n) time, O(1) space
def reverseList(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


print(to_list(reverseList(build([1, 2, 3, 4, 5]))))



# 41. Linked List Cycle — Floyd's tortoise and hare
# O(n) time, O(1) space
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


looped = build([3, 2, 0, -4])
looped.next.next.next.next = looped.next
print(hasCycle(build([1, 2])), hasCycle(looped))



# 42. Merge Two Sorted Lists
# O(n + m) time, O(1) space
def mergeTwoLists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


print(to_list(mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))



# 43. Merge K Sorted Lists — index i in the tuple breaks ties so nodes are never compared
# O(N log k) time, O(k) space
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



# 44. Remove Nth Node From End of List — gap of n between the runners
# O(n) time (one pass), O(1) space
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow, fast = slow.next, fast.next
    slow.next = slow.next.next
    return dummy.next


print(to_list(removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)))



# 45. Reorder List — split at the midpoint, reverse the second half, then weave
# O(n) time, O(1) space
def reorderList(head):
    if not head or not head.next:
        return
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    second, slow.next = slow.next, None

    prev = None
    while second:
        second.next, prev, second = prev, second, second.next

    first, second = head, prev
    while second:
        nxt1, nxt2 = first.next, second.next
        first.next, second.next = second, nxt1
        first, second = nxt1, nxt2


nodes = build([1, 2, 3, 4, 5])
reorderList(nodes)
print(to_list(nodes))
