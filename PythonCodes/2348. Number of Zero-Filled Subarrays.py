class Solution:
    def gaussian_sum(self, n:int) -> int:
        return (n * ( n + 1)) // 2
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = 0
        zero_count = 0
        for elem in nums:
            if elem != 0:
                zeros += self.gaussian_sum(zero_count)
                zero_count = 0
            else:
                zero_count += 1
        zeros += self.gaussian_sum(zero_count)
        return zeros
