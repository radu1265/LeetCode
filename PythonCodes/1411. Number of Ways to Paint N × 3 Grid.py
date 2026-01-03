class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 12
        clrs_2 = 6
        clrs_3 = 6
        i = 1
        while i < n:
            i += 1
            clrs_2_aux = clrs_2
            clrs_3_aux = clrs_3
            clrs_3 = clrs_3_aux * 2 + clrs_2_aux * 2
            clrs_2 = clrs_3_aux * 2 + clrs_2_aux * 3
        return (clrs_2 + clrs_3) % MOD
