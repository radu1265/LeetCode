class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            mid_pow_2  = mid * mid
            if mid_pow_2 == x:
                return mid
            elif mid_pow_2 < x:
                left = mid + 1
            else: right = mid - 1
        mid = (left + right) // 2
        return mid
