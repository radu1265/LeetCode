class Solution:
    def largestGoodInteger(self, num: str) -> str:
        matrix = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']
        for elem in matrix:
            if elem in num:
                return elem
        return ''
