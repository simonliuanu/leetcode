class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        last = head
        cur = head.next

        while cur:
            if cur.val < last.val:
                tmp = dummy
                while tmp.next and cur.val > tmp.next.val:
                    tmp = tmp.next
                last.next = cur.next
                cur.next = tmp.next
                tmp.next = cur
            else:
                last = last.next
            cur = last.next

        return dummy.next


