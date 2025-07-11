class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = ""
        negative = num < 0
        num = abs(num)
        while num > 0:
            ans = str(num % 7) + ans
            num //= 7
        return "-" + ans if negative else ans

