class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        count = 0
        length = len(chars)
        while i < length:
            if chars[i] == chars[j]:
                count += 1
                i += 1
            else:
                if count > 1:
                    chars[j + 1:i] = list(str(count))
                    j = i - count + 1 + len(list(str(count)))
                    i = j
                else:
                    j = i
                count = 0
                length = len(chars)
        if count > 1:
            chars[j + 1:] = list(str(count))    
        return length
