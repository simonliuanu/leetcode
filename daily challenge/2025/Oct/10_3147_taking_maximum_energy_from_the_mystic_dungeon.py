# O(n^2), time out:
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -inf
        for i in range(len(energy)):
            tmp = 0
            j = i
            while j < len(energy):
                tmp += energy[j]
                j += k
            ans = max(ans, tmp)
        return ans

# O(n):
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - 1, -1, -1):
            if i + k < len(energy):
                energy[i] += energy[i + k]
        return max(energy)
