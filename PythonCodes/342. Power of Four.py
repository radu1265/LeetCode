class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        count = 0
        if not (n & (n - 1)) and n:
            while n:
                n >>= 1
                count += 1
        if count % 2:
            return True
        return False
