# dummy solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        dummy = ListNode(next = head)
        curr = head
        while curr:
            l += 1
            curr = curr.next
        curr = dummy
        for _ in range(l - n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

# double pointers solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = dummy = ListNode(0, head)
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
