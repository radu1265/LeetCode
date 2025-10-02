class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_count, count = 0, 0
        i, j = 0, 0

        while j < k:
            if s[j] in vowels:
                max_count += 1
            j += 1

        if max_count == k:
            return max_count

        count = max_count

        while j < len(s):
            if s[i] in vowels:
                count -= 1
            if s[j] in vowels:
                count += 1
            if count == k:
                return count
            if count > max_count:
                max_count = count
            j += 1
            i += 1
            
        return max_count
