class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
        }
        prev = 0
        total = 0
        
        for elem in s:
            if prev < romanDict[elem]:
                total -= prev
            else:
                total += prev
            prev = romanDict[elem]
        return total + prev
