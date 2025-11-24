class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        out = 0
        arr = []
        for elem in nums:
            out = out << 1
            out += elem
            arr.append(out % 5 == 0)
        return arr
