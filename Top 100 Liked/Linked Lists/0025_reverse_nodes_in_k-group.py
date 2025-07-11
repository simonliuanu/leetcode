# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        dummy = ListNode(0, head)
        node0 = dummy
        while n >= k:
            n -= k
            pre = None
            start = node0.next
            curr = start
            for _ in range(k):
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp
            node0.next.next = curr
            node0.next = pre
            node0 = start
        return dummy.next

