# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            pre, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        mid = middleNode(head)
        head2 = reverseList(mid)

        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

