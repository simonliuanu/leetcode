"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Hashmap solution:
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        mp = {}
        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)
            curr = curr.next
        return mp[head]

# O(1) solution:
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur = head
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        odd = oddHead = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        return evenHead

