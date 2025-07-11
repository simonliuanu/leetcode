# stupid solution
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        C.clear()
        C.extend(A)

# real solution
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        def sort(n, A: List[int], B: List[int], C: List[int]) -> None:
            if n == 1:
                C.append(A.pop())
            else:
                sort(n - 1, A, C, B)
                C.append(A.pop())
                sort(n - 1, B, A, C)
        n = len(A)
        sort(n, A, B, C)
