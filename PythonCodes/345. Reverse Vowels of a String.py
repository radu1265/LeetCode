class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
            if s[l] in vowels and s[r] in vowels and l != r:
                # s = s[:l] + s[r] + s[l + 1:r] + s[l] + s[r + 1:] used for solving without converting str to list
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
