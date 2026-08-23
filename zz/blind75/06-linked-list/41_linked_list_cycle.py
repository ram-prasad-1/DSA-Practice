# 41. Linked List Cycle — Floyd's tortoise and hare
# Run: python 41_linked_list_cycle.py
# Time: O(n). Space: O(1).



class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head



def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False



looped = build([3, 2, 0, -4])
looped.next.next.next.next = looped.next
print(hasCycle(looped))
print(hasCycle(build([1, 2])))
