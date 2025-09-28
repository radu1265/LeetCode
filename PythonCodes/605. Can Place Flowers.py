class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        if len(flowerbed) < 3:
            if sum(flowerbed) < 1:
                return n - 1 <= 0
            return False

        st, nd, trd = 0, flowerbed[0], flowerbed[1]
        i = 2

        while i < len(flowerbed):
            if not st and not nd and not trd:
                n -= 1
                st = 1
            else:
                st = nd

            nd = trd
            trd = flowerbed[i]
            i += 1

        if not nd and not trd:
            n -= 1
            
        return n <= 0
