class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not n & (n - 1) and n > 0
