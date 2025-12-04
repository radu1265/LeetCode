class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = nums[1]
        for idx in range(3, n + 1):
            dp[idx] += max(nums[idx - 1] + dp[idx - 2], nums[idx - 1] + dp[idx - 3])
        return max(dp[n - 1], dp[n])
        
