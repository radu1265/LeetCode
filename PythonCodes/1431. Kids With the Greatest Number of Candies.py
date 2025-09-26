class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        biggest = max(candies)
        return [candie + extraCandies >= biggest for candie in candies]
