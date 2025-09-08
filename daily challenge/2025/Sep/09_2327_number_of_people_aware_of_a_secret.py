# self solution:
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 1_000_000_007
        arr = [0] * forget
        arr[0] = 1
        for _ in range(n - 1):
            tmp = sum(arr[delay - 1:forget - 1]) % MOD
            arr[1:forget] = arr[0:forget - 1]
            arr[0] = tmp
        return sum(arr) % MOD
