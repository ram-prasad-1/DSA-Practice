# 44. Remove Nth Node From End of List — hold a gap of n between the runners
# Run: python 44_remove_nth_node_from_end.py
# Time: O(n) in one pass. Space: O(1).



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
print(to_list(removeNthFromEnd(build([1, 2]), 2)))
