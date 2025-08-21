# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        oldest_bad = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                oldest_bad = mid
                right = mid - 1
            else: left = mid + 1
        return oldest_bad
