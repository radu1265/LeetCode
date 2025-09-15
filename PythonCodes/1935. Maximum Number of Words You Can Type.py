class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words_to_type = text.split()
        count = 0
        for word in words_to_type:
            for letter in brokenLetters:
                if letter in word:
                    count += 1
                    break
        return len(words_to_type) - count
