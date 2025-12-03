class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        dp = [0] * numRows
        dp[0] = [1]
        dp[1] = [1, 1]

        for i in range(2, numRows):
            aux = []
            aux.append(1)
            for j in range(1, i):
                aux.append(dp[i - 1][j] + dp[i - 1][j - 1])
            aux.append(1)
            dp[i] = aux
        return dp
