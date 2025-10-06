class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for elem in arr:
            if elem in d:
                d[elem] += 1
            else:
                d.update({elem:1})
        occurrencces = d.values()
        if len(occurrencces) == len(set(occurrencces)):
            return True
        return False
