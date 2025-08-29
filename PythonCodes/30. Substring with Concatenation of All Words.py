class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []
        
        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(0, total_len, word_len):
                word = s[i + j : i + j + word_len]
                if word not in word_count:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_count[word]:
                    break
            else:
                res.append(i)

        return res
