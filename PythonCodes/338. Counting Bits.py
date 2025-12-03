# class Solution:
    # def bit_counter(self, n: int) -> int:
    #     bit_counter = 0
    #     while n:
    #         bit_counter += 1 
    #         n = n & (n - 1)
    #     return bit_counter
    # def countBits(self, n: int) -> List[int]:
    #     out = [self.bit_counter(x) for x in range(n + 1)]
    #     return out

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            
            dp[i] = dp[i - sub] + 1
        
        return dp
