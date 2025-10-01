class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0
        max_avg, elem_sum = 0, 0
        while j < k:
            elem_sum += nums[j]
            j += 1
        
        max_avg = elem_sum / k
        
        while j < len(nums):
            elem_sum = elem_sum + nums[j] - nums[i]
            max_avg = max(max_avg, elem_sum / k)
            j += 1
            i += 1

        return max_avg
