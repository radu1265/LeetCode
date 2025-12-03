class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        for idx in range(n):
            if idx < 2:
                dp[idx] = cost[idx]
            else: dp[idx] = min(dp[idx - 1] + cost[idx], dp[idx - 2] + cost[idx])
        return min(dp[n - 1], dp[n - 2])
