class Solution:
    def countTriples(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, n+1)]
        count = 0
        for i in squares:
            for j in squares:
                if i + j in squares:
                    count += 1
        return count
