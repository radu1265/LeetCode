class Solution:
    def gcd(self, len1: int, len2: int) -> int:
        while len2:
            len1, len2 = len2, len1 % len2
        return len1

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:self.gcd(len(str1), len(str2))]
        # divs_list = []
        # for dim_segment, _ in enumerate(str1):
        #     dim_segment += 1
        #     divisor = str1[0:dim_segment]
        #     copy_str1 = str1
        #     copy_str1 = copy_str1[dim_segment:]
        #     while copy_str1:
        #         if copy_str1[:dim_segment] == divisor:
        #             copy_str1 = copy_str1[dim_segment:]
        #         else: break
        #     if not copy_str1:
        #         divs_list.append(divisor)
        
        # divs_list = divs_list[::-1]
        # for div in divs_list:
        #     div_size = len(div)
        #     copy_str2 = str2
        #     while copy_str2:
        #         if copy_str2[:div_size] != div:
        #             break
        #         else: copy_str2 = copy_str2[div_size:]
            
        #     if not copy_str2:
        #         return div
        # return ""

                    
