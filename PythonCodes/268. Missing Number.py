class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        size = len(nums)
        return (size * (size + 1)) // 2 - nums_sum
