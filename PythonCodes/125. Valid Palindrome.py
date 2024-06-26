'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~ `'''
        for ele in s:
            if ele in punc:
                s = s.replace(ele,"")
        return s == s[::-1]
