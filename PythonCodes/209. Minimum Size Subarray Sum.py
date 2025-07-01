class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, cur, best = -1, 0, 0
        found = False
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                l += 1
                cur -= nums[l]
                found = True
            if found:
                if best == 0:
                    best = r - l + 1
                else: best = min(best, r - l + 1)
            found = False
        return best
