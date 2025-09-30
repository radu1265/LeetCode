class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, medium = nums[0], inf
        for elem in nums[1:]:
            if small >= elem:
                small = elem
            elif medium >= elem:
                medium = elem
            else: return True
        return False
