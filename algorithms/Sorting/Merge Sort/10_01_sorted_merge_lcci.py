class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if A[m] > B[n]:
                A[m + n + 1] = A[m]
                m -= 1
            else:
                A[m + n + 1] = B[n]
                n -= 1
        while m >= 0:
            A[m + n + 1] = A[m]
            m -= 1
        while n >= 0:
            A[m + n + 1] = B[n]
            n -= 1

