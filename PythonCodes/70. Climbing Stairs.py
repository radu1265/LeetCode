class Solution:
    def climbStairs(self, n: int) -> int:

        if n > 0 and n < 4:
            return n
        
        prev1 = 2
        prev2 = 3
        cur = 0
        for i in range(4, n + 1):
            cur = prev1 + prev2
            prev1 = prev2
            prev2 = cur
        return cur
