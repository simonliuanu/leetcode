# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA, lenB = 0, 0

        pA = headA
        while pA:
            lenA = lenA + 1
            pA = pA.next
        pB = headB
        while pB:
            lenB = lenB + 1
            pB = pB.next

        pA, pB = headA, headB
        if lenA > lenB:
            pB = headB
            for i in range(lenA - lenB):
                pA = pA.next
        else:
            pA = headA
            for i in range(lenB - lenA):
                pB = pB.next

        while pA:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next

        return None

# Optimisation (double pointers)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA
