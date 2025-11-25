class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        n, count = 0, 1
        while count <= k + 1:
            n = n * 10 + 1
            if n % k == 0 and n >= k:
                return count
            count += 1
        return -1
