# permutation solution, slow:
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        digits.sort()
        length = len(digits)
        nums = []
        path = []
        used = [False for _ in range(length)]

        def dfs():
            if len(path) == length:
                nums.append(reduce(lambda acc, d: acc * 10 + d, path, 0))
            for i in range(length):
                if used[i] or (digits[i] == 0 and not path):
                    continue
                if i > 0 and digits[i] == digits[i - 1] and not used[i - 1]:
                    continue
                path.append(digits[i])
                used[i] = True
                dfs()
                path.pop()
                used[i] = False

        dfs()
        for num in nums:
            if num & (num - 1) == 0:
                return True
        return False

# log(m) for m is digits of n:
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sig = ''.join(sorted(str(n)))
        pow_of_sig = [''.join(sorted(str(1 << k))) for k in range(31)]
        return sig in pow_of_sig
