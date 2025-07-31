# self solution:
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        def validate(n, original, derived):
            for i in range(n - 1):
                original[i + 1] = original[i] ^ derived[i]
            return True if original[0] == original[n - 1] ^ derived[n - 1] else False

        n = len(derived)
        return validate(n, [0] * n, derived) or validate(n, [1] + [0] * (n - 1), derived)
