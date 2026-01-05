'''
  sum everything
  in case of odd negative numbers substratc the closest one to zero
'''

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        closest_to_zero = abs(matrix[0][0])
        matrix_sum = 0
        odd = False
        for line in matrix:
            for elem in line:
                if elem < 0:
                    odd = not odd
                if abs(elem) < closest_to_zero:
                    closest_to_zero = abs(elem)
                matrix_sum += abs(elem)
        if odd:
            matrix_sum -= closest_to_zero * 2 

        return matrix_sum
