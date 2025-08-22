class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num // 2

        if num == 1:
            return True    
            
        while left <= right:
            mid = (left + right) // 2
            power = mid * mid
            if power == num:
                return True
            elif power < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
