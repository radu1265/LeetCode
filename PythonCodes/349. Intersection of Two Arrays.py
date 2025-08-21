class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # rez = []
        # for elem in nums1:
        #     if elem in nums2 and elem not in rez:
        #         rez.append(elem)
        # return rez
        # O(n x m)

        # return list({x for x in nums1 if x in nums2})
        # O(n x m)

        return list((set(nums1) & set(nums2)))
        # O(n + m)
