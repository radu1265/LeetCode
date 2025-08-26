class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area_m, area = 0, 0
        diag_m, diag = 0, 0

        for elem in dimensions:
            diag = elem[0] ** 2 + elem[1] ** 2
            area = elem[0] * elem[1]
            if diag > diag_m:
                diag_m = diag
                area_m = area
            elif diag == diag_m:
                if area > area_m:
                    area_m = area
        return area_m
