from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        if not digits:
            return []

        long_string = []

        for elem in digits:
            long_string.append(digit_to_char[elem])
            
        rez = list(product(*long_string))

        # change the list so it respects the output format
        output = []
        for elem in rez:
            output.append(''.join(elem))

        return output
