class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(c1 + c2 for c1, c2 in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]
