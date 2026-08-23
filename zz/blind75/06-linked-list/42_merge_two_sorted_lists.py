# 42. Merge Two Sorted Lists — dummy head keeps the first append case uniform
# Run: python 42_merge_two_sorted_lists.py
# Time: O(n + m). Space: O(1).



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
print(to_list(mergeTwoLists(build([]), build([0]))))
