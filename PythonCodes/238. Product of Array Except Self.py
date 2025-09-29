class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod, suf_prod = [], []
        out = []
        for idx, elem in enumerate(nums):
            if idx == 0:
                pre_prod.append(elem)
            else:
                pre_prod.append(pre_prod[idx - 1] * elem)

        for idx, elem in enumerate(nums[::-1]):
            if idx == 0:
                suf_prod.append(elem)
            else:
                suf_prod.append(suf_prod[idx - 1] * elem)
        suf_prod = suf_prod[::-1]

        for idx in range(len(nums)):
            if idx == 0:
                out.append(suf_prod[idx + 1])
            elif idx == len(nums) - 1:
                out.append(pre_prod[idx - 1])
            else:    
                out.append(pre_prod[idx - 1] * suf_prod[idx + 1])
        return out
