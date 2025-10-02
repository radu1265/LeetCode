class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        have_zero = False
        left, right = 0, 0
        max_count = 0

        while right < len(nums):
            if nums[right]:
                right += 1
                continue
            if left <= right:
                if not have_zero:
                    have_zero = True
                    right += 1
                else:
                    max_count = max(max_count, right - left - 1)
                    if not nums[left]:
                        have_zero = False
                    left += 1

            else: right += 1
        max_count = max(max_count, right - left - 1)

        if max_count == len(nums) or (have_zero and max_count == len(nums) - 1):
            return len(nums) - 1
        return max_count
