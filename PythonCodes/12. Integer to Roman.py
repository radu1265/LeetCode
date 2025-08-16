class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1 : 'I',
            4 : 'IV',
            5 : 'V',
            9 : 'IX',
            10 : 'X',
            40 : 'XL',
            50 : 'L',
            90 : 'XC',
            100 : 'C',
            400 : 'CD',
            500 : 'D',
            900 : 'CM',
            1000 : 'M'
        }
        roman = ''
        count = 0
        for key in reversed(sorted(roman_dict.keys())):
            count = num // key
            roman = roman + roman_dict[key] * count
            num = num % key
        return roman
