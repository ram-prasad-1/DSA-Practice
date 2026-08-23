# 45. Reorder List — split at the midpoint, reverse the second half, then weave
# Run: python 45_reorder_list.py
# Time: O(n). Space: O(1).



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

nodes = build([1, 2, 3, 4])
reorderList(nodes)
print(to_list(nodes))
