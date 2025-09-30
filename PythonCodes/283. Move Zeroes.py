class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
            i += 1

        # left = 0

        # for idx, right in enumerate(nums):
        #     if right != 0:
        #         nums[left], nums[idx] = nums[idx], nums[left]
        #         left += 1
        
