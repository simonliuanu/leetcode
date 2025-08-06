# Segment Tree solution:
class SegTree:
    def __init__(self, a: List[int]):
        n = len(a)
        self.tree = [0] * (2 << (n - 1).bit_length())
        self._build(a, 1, 0, n - 1)

    def _build(self, a: List[int], idx: int, l: int, r: int) -> None:
        if l == r:
            self.tree[idx] = a[l]
            return
        m = (l + r) >> 1
        self._build(a, idx * 2, l, m)
        self._build(a, idx * 2 + 1, m + 1, r)
        self._maintain(idx)

    def _maintain(self, idx: int) -> None:
        self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def _search(self, idx: int, l: int, r: int, x: int) -> Optional[int]:
        if self.tree[idx] < x:
            return -1
        if l == r:
            self.tree[idx] = -1
            return l # this return could be any positive value?
        m = (l + r) >> 1
        ret = self._search(idx * 2, l, m, x)
        if ret < 0:
            ret = self._search(idx * 2 + 1, m + 1, r, x)
        self._maintain(idx)
        return ret

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegTree(baskets)
        ans = 0
        for i in fruits:
            if st._search(1, 0, len(baskets) - 1, i) < 0:
                ans += 1
        return ans
