class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        count = 0
        if not (n & (n - 1)) and n:
            while n:
                n >>= 1
                count += 1
        if count % 2:
            return True
        return False
'''
faster O(1) instead of O(log4X)
n & (n - 1) checks if number is power of 2
n & 0xAAAAAAAA checks if this is power of 2 (needs the first check)
0xAAAAAAAA = 10101010101010101010101010101010
works for 32 bits integers
return (n != 0 and 
          ((n & (n - 1)) == 0) and 
            not(n & 0xAAAAAAAA))
'''
