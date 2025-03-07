class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def get_prime(n: int) -> bool:
            if n <= 1: return False
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
            
        fst, snd = -1 , -1
        output = [-1, -1]
        minim = float('inf')
        for i in range(left, right + 1):
            if get_prime(i):
                if fst == -1:
                    fst = i
                elif snd == -1:
                    snd = i
                    if minim > snd - fst:
                        minim = snd - fst
                        output = [fst, snd]
                    fst = snd
                    snd = -1
            if minim <= 2:
                return output
        return output
