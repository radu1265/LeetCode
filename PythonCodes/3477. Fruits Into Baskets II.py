class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        i = 0
        for fruit in fruits:
            while i < len(baskets):
                if fruit <= baskets[i]:
                    baskets.pop(i)
                    break
                i += 1
            i = 0
        return len(baskets)
