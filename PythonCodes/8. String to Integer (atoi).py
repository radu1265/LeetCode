class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if len(s) == 0:
            return 0
        sign = not s[0] == '-'
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        s = s.lstrip('0')
        if len(s) == 0:
            return 0
        for idx in range(len(s)):
            if not s[idx].isdigit():
                s = s[:idx]
                break
        if not s:
            return 0

        number = int(s) if sign else int('-' + s)
        if number > 2**31 - 1:
            number = 2**31 - 1
        elif number < -2**31:
            number = -2**31
        return number
