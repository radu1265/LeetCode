class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def b_search(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            result = len(nums)

            while left <= right:
                middle = (left + right) // 2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    result = middle
                    right = middle - 1
            return result
        neg = b_search(nums, 0)
        pos = len(nums) - b_search(nums, 1)
        return max(neg, pos)

class Solution:
  def maximumCount(self, nums: List[int]) -> int:
      pos, neg = 0, 0
      for elem in nums:
          if elem < 0:
              neg += 1
          elif elem > 0:
              pos += 1
      return max(neg,pos)
