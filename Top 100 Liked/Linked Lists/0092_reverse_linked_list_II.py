# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node0 = dummy = ListNode(0, head)
        for _ in range(left - 1):
            node0 = node0.next
        pre = None
        curr = node0.next
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        node0.next.next = curr
        node0.next = pre
        return dummy.next

