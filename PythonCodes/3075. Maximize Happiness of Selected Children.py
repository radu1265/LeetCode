class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        sum_happy = 0
        children_selected = 0
        for elem in happiness[::-1]:
            if k == 0: break
            if elem - children_selected <= 0: break
            sum_happy += elem - children_selected
            children_selected += 1
            k -= 1
        return sum_happy

        
