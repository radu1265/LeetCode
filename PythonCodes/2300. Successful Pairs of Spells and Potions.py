class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        m = len(potions) - 1

        for spell in spells:

            low, high = 0, m
            while low != high:
                mid = (low + high) // 2
                if potions[mid] * spell < success:
                    low = mid + 1
                else:
                    high = mid
            if potions[low] * spell >= success:
                pairs.append(m - low + 1)
            else: pairs.append(0)
        return pairs
        
