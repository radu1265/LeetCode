'''
  Given an integer x, return true if x is a 
palindrome , and false otherwise.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        aux = x
        inter = 0
        if x < 0:
            return False
        while aux :
            rev = rev * 10 + aux % 10
            aux = aux // 10
            inter +=1
        if x == rev:
            return True
        return False
        # return str(x) == str(x)[::-1]
