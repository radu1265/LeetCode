...
You are given a large integer represented as an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order
. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
...
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        increment = 1
        for indx, elem in enumerate(digits):
            if elem + increment > 9:
                digits[indx] = 0
            else:
                digits[indx] += 1
                break
        if digits[-1] == 0:
            digits.append(1)
        digits.reverse()
        return digits
