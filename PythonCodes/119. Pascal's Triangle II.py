class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        dp = [0] * (rowIndex + 1)
        dp[0] = [1]
        dp[1] = [1, 1]

        for i in range(2, rowIndex + 1):
            aux = []
            aux.append(1)
            for j in range(1, i):
                aux.append(dp[i - 1][j - 1] + dp[i - 1][j])
            aux.append(1)
            dp[i] = aux
        return dp[rowIndex]
