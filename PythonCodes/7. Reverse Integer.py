class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = not flag
            x *= -1
        rev = int(str(x)[::-1])
        if rev.bit_length() >= 32:
            return 0
        if flag: return rev * (-1)
        return rev
