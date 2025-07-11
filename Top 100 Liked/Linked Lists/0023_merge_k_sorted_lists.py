# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# initial merge solution:
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeList(l, r):
            dummy = ListNode()
            cur = dummy
            while l and r:
                if l.val < r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            cur.next = l if l else r
            return dummy.next

        merged = lists[0]
        for i in range(1, len(lists)):
            merged = mergeList(merged, lists[i])
        return merged

# optimisation:
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeList(l, r):
            dummy = ListNode()
            cur = dummy
            while l and r:
                if l.val < r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            cur.next = l if l else r
            return dummy.next

        def helper(l, r):
            if l == r:
                return lists[l]
            mid = (l + r) >> 1
            left = helper(l, mid)
            right = helper(mid + 1, r)

            return mergeList(left, right)

        return helper(0, len(lists) - 1)
