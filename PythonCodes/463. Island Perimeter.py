class Solution:
    def nr_of_neighbours(self, grid: List[List[int]], l_indx: int, r_indx: int) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        if l_indx + 1 < n and grid[l_indx + 1][r_indx] == 1:
            count += 1
        if r_indx + 1 < m and grid[l_indx][r_indx + 1] == 1:
            count += 1
        if l_indx - 1 >= 0 and grid[l_indx - 1][r_indx] == 1:
            count += 1
        if r_indx - 1 >= 0 and grid[l_indx][r_indx - 1] == 1:
            count += 1
        return count
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for l_indx, line in enumerate(grid):
            for r_indx, elem in enumerate(line):
                if elem == 1:
                    perimeter += 4
                    perimeter -= self.nr_of_neighbours(grid, l_indx, r_indx)
        return perimeter
                
