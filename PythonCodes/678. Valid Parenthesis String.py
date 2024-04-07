'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
'''

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftMin = 0
        leftMax = 0
        for elem in s:
            if elem == '(':
                leftMin += 1
                leftMax += 1
            if elem == ')':
                leftMin -= 1
                leftMax -= 1
                if leftMax < 0:
                    return False
            if elem == '*':
                leftMin -= 1
                leftMax += 1
            if leftMin < 0:
                leftMin = 0
        if leftMin > 0:
            return False
        return True


        
