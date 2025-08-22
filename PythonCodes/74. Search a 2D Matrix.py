class Solution:
    @staticmethod
    def binary_search(target: int, line: List[int]) -> bool:
        left, right = 0, len(line) - 1
        while left <= right:
            mid = (left + right) // 2
            if line[mid] == target:
                return True
            elif line[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_elements = list(zip(*matrix))[0]
        left, right = 0, len(first_elements) - 1
        n = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][n]:
                return Solution.binary_search(target, matrix[mid])
            elif target > matrix[mid][n]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
        return False
