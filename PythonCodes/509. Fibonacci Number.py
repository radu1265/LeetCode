class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        prev1 = 0
        prev2 = 1
        cur = prev1 + prev2
        for i in range(2, n):
            prev1 = prev2
            prev2 = cur
            cur = prev1 + prev2
        return cur
