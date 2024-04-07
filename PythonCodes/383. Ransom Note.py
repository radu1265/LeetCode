'''
Given two strings ransomNote and magazine, return true
  if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dic = {}
        for elem in ransomNote:
            if elem in ransom_dic:
                ransom_dic[elem] += 1
            else:
                ransom_dic[elem] = 1
        for elem in magazine:
            if elem in ransom_dic:
                ransom_dic[elem] -=1
        for key, value in ransom_dic.items():
            if value > 0:
                return False
        return True
