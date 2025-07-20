class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_strack = []
        current = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                num_stack.append(k)
                str_strack.append(current)
                current = ""
                k = 0
            elif c == ']':
                r = num_stack.pop()
                prev = str_strack.pop()
                current = prev + r * current
            else:
                current += c

        return current
