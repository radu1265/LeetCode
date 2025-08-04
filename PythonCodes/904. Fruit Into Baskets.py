class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f1, f2 = [fruits[0], 1], [-1, 0]
        f_max = 0
        i = 1
        j = 0           

        while i < len(fruits):
            if fruits[i] == f1[0]:
                f1[1] += 1
            elif f2[0] == -1 or fruits[i] == f2[0]:
                if f2[0] == -1:
                    f2[0] = fruits[i]
                    f2[1] = 1
                else:
                    f2[1] += 1

            else:
                f_max = max(f_max, f1[1] + f2[1])

                while f1[1] != 0 and f2[1] != 0:
                    if fruits[j] == f1[0]:
                        f1[1] -= 1
                    elif fruits[j] == f2[0]:
                        f2[1] -= 1
                    j += 1
                    
                if f1[1] == 0:
                    f1[0] = fruits[i]
                    f1[1] = 1
                if f2[1] == 0:
                    f2[0] = fruits[i]
                    f2[1] = 1
            i += 1
        f_max = max(f_max, f1[1] + f2[1])
        return f_max
