class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum, post_sum = [], []
        for idx, elem in enumerate(nums):
            if not idx:
                pre_sum.append(elem)
            else:
                pre_sum.append(elem + pre_sum[idx - 1])

        for idx, elem in enumerate(nums[::-1]):
            if not idx:
                post_sum.append(elem)
            else:
                post_sum.append(elem + post_sum[idx - 1])
        idx = 0
        for i, j in zip(pre_sum, post_sum[::-1]):
            if i == j:
                return idx
            idx += 1
        return -1

