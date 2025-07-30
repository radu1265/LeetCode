class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxim = 0
        max_ind = []
        aux_ind = []
        for i, elem in enumerate(nums):
            if elem > maxim:
                maxim = elem
                max_ind = [i, i]
            elif elem == maxim:
                if i == max_ind[1] + 1:
                    max_ind[1] = i
                else:
                    if not aux_ind:
                        aux_ind = [i, i]
                    else:
                        if i == aux_ind[1] + 1:
                            aux_ind[1] = i
                        else:
                            aux_ind.clear()
                            aux_ind = [i, i]
            if aux_ind and aux_ind[1] - aux_ind[0] > max_ind[1] - max_ind[0]:
                max_ind = list(aux_ind)
                aux_ind.clear()
        return max_ind[1] - max_ind[0] + 1
