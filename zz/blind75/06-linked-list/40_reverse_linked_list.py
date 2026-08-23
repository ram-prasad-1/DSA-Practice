# 40. Reverse a Linked List — walk forward, flipping each next pointer
# Run: python 40_reverse_linked_list.py
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



def reverseList(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev



print(to_list(reverseList(build([1, 2, 3, 4, 5]))))
print(to_list(reverseList(build([]))))
