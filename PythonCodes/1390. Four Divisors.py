class Solution:
    def hasFourDivisors(self, num: int) -> int:

        div = 0
        num_sum = num + 1
        i = 2
        if math.sqrt(num) % 1 == 0: return 0
        
        while (i ** 2) < num:
            if num % i == 0:
                if div == 0:
                    div = i
                else: return 0

            i += 1
        if div == 0: return 0

        num_sum += div + num // div
        return num_sum

    def sumFourDivisors(self, nums: List[int]) -> int:
        final_sum = 0
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = self.hasFourDivisors(num)
            final_sum += dic[num]

        return final_sum
