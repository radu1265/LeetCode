class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        partitions = 0
        for elem in nums[:-1]:
            left += elem
            right -= elem
            if (left - right) % 2 == 0:
                partitions += 1
        return partitions
