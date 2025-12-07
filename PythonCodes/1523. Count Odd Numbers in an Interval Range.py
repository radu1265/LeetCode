class Solution:
    def countOdds(self, low: int, high: int) -> int:
        numbers = (high - low + 1) // 2
        if low % 2 == 0:
            return numbers
        if low % 2 and high % 2:
            return numbers + 1
        return numbers
