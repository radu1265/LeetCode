class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        zeros, max_len = 0, 0
        while right < len(nums):
            if zeros <= k:
                if not nums[right]:
                    zeros += 1
                right += 1

            if zeros > k:
                if not nums[left]:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len
