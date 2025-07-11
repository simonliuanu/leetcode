# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        evenHead = head.next
        odd = oddHead = head
        even = odd.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return oddHead


