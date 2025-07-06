# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        lastsorted = head
        curr = lastsorted.next

        while curr:
            if curr.val < lastsorted.val:
                tmp = dummy
                while tmp.next and curr.val > tmp.next.val:
                    tmp = tmp.next
                lastsorted.next = curr.next
                curr.next = tmp.next
                tmp.next = curr
            else:
                lastsorted = lastsorted.next
            curr = lastsorted.next

        return dummy.next

