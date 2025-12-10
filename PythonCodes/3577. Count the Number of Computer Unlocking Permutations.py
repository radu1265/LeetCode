class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 ** 9 + 7
        minim = complexity[0]
        count = 1
        for elm in complexity[1:]:
            if minim == elm:
                count += 1
            elif minim > elm:
                return 0
        if count > 1:
            return 0
        
        permutations = 1
        for i in range(1, len(complexity)):
            permutations = (i * permutations) % MOD
        return permutations
