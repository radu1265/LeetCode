from itertools import combinations
class Solution:
    def is_power_of_2 (self, n:int) -> bool:
        return (n>0) and (n & (n-1) == 0)

    def rearrange_even_last(self, num):
        digits = list(str(num))
        results = set()
        
        for perm in permutations(digits):
            if perm[0] != '0' and int(perm[-1]) % 2 == 0:
                results.add(int("".join(perm)))
        
        return sorted(results)

    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1: return True
        if n <= 0: return False
        even = self.rearrange_even_last(n)
        for elem in even:
            if self.is_power_of_2(elem):
                return True
        return False
