# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        node0 = dummy
        while node0.next and node0.next.next:
            node1 = node0.next
            node2 = node1.next
            node0.next = node2
            node1.next = node2.next
            node2.next = node1
            node0 = node1

        return dummy.next

