class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, cur, best = 0, 0, 0
        for r in range(1,len(s)):
            if s[r] in s[l:r]:
                best = max(best, r - l)
                while s[r] in s[l:r]:
                    l += 1
        best = max(best, len(s) - l)    
        return best
