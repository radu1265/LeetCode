class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p_needle = 0
        p1, p2 = 0, 0
            
        while p1 < len(haystack) and p2 < len(haystack):
            if haystack[p2] == needle[p_needle]:
                if p_needle == len(needle) - 1:
                    return p1
                p_needle += 1
                p2 += 1
            else:
                p1 += 1
                p2 = p1
                p_needle = 0
        return -1
