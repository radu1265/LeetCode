class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        out1 = [x for x in set1 if x not in set2]
        out2 = [x for x in set2 if x not in set1]

        return [out1, out2]

