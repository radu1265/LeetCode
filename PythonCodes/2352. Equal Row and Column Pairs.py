from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        i, j = 0, 0
        n = len(grid)
        grid_trans = []
        count = 0

        while i < n:
            line = []
            j = 0
            while j < n:
                line.append(grid[j][i])
                j += 1
            grid_trans.append(line)
            i += 1

        for elem in grid:
            for elem_trans in grid_trans:
                if elem == elem_trans:
                    count += 1
        
        return count
        # row_counts = Counter(tuple(row) for row in grid)
        # return sum(Counter(row_counts[tuple(col)] for col in (zip(*grid))))
