# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# self solution (stupid but workable):
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev

        n1 = n2 = 0

        l1 = reverseList(l1)
        l2 = reverseList(l2)

        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next

        n = n1 + n2

        l3 = None

        if n == 0: return ListNode(0)
        while n != 0:
            tmp = ListNode(n % 10)
            n //= 10
            tmp.next = l3
            l3 = tmp

        return reverseList(l3)

# a smarter solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        p, q = l1, l2
        carry = 0

        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p: p = p.next
            if q: q = q.next

        return dummy.next

