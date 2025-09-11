class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ('AEIOUaeiou')
        vowels_in_list = [x for x in s if x in vowels]
        vowels_in_list.sort()
        
        res = []
        indx_vowels = 0
        for elem in s:
            if elem in vowels:
                res.append(vowels_in_list[indx_vowels])
                indx_vowels += 1
            else: res.append(elem)
        return ''.join(res)
