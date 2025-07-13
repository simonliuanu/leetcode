# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# self solution:
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        while head:
            ans += pow(2, cnt - 1) * head.val
            cnt -= 1
            head = head.next

        return ans

# smarter solution(official):
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans
