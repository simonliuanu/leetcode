# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def getMid(head):
            # this is where I made the mistake using slow = fast = head (think the reason)
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(left, right):
            dummy = ListNode()
            cur = dummy

            while left and right:
                if left.val > right.val:
                    cur.next = right
                    right = right.next
                else:
                    cur.next = left
                    left = left.next
                cur = cur.next

            cur.next = left if left else right
            return dummy.next

        mid = getMid(head)
        r = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(r)

        return merge(left, right)

