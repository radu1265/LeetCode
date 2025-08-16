class Solution:
    def maximum69Number (self, num: int) -> int:
        x = list(str(num))
        for indx, elem in enumerate(x):
            if elem == '6':
                x[indx] = '9'
                return int(''.join(map(str, x)))
        return num
        
