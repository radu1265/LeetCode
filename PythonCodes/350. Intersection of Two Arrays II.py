class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [x for x in nums1 if x in nums2 and not nums2.remove(x)]
