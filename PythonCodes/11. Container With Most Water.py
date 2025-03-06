class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxim = 0
        while left < right:
            if maxim < min(height[left], height[right]) * (right -left):
                maxim = min(height[left], height[right]) * (right -left)
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
        return maxim
