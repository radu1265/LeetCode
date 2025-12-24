class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort()
        count = 0
        for box in capacity[::-1]:
            apples -= box
            count += 1
            if apples <= 0:
                break
        return count
        
