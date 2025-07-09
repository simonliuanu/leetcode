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
