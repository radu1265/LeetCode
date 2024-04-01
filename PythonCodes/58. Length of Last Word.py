'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring
 consisting of non-space characters only.

 Stupid Solution
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        aux = s[::-1]
        index = 0
        if ' ' not in aux:
            return len(aux)
        for indx, elem in enumerate(aux):
            if elem == ' ':
                continue
            else:
                index = indx
                break
        aux = aux[index:]
        if ' ' not in aux:
            return len(aux)
        return len(aux[:aux.find(' ')])
