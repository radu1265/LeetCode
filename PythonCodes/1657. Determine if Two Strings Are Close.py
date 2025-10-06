from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        w1 = list(word1)
        w2 = list(word2)

        if set(w1) != set(w2):
            return False

        counter1 = Counter(w1)
        counter2 = Counter(w2)

        return Counter(counter1.values()) == Counter(counter2.values())
