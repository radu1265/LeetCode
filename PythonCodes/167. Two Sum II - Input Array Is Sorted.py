# solved in O(N) and O(N log(N))

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            arr_sum = numbers[lo] + numbers[hi]
            if arr_sum == target:
                return [lo + 1, hi + 1]
            elif arr_sum > target:
                hi -= 1
            else:
                lo += 1
        return 0

        
        # for cur in range(len(numbers)):
        #     l = cur + 1
        #     r = len(numbers) - 1
        #     new_target = target - numbers[cur]
        #     while l <= r:
        #         mid = (l + r) // 2
        #         print (mid)
        #         if numbers[mid] == new_target:
        #             return [cur + 1, mid + 1]
        #         if numbers[mid] < new_target:
        #             l = mid + 1
        #         if numbers[mid] > new_target:
        #             r = mid - 1
        # return 0
