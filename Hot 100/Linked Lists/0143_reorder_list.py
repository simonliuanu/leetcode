# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def midNode(head: Optional[ListNode]) -> Optional[ListNode]:
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

        mid = midNode(head)
        head2 = reverseList(mid)

        while head2.next:
          tmp = head.next
          head.next = head2
          head = tmp
          tmp = head2.next
          head2.next = head
          head2 = tmp


# List approach:
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
          return
        vec = list()
        while head:
            vec.append(head)
            head = head.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
              break
            vec[j].next = vec[i]
            j -= 1
        vec[j].next = None
