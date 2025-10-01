class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        restBottles = 0

        while numBottles:
            aux = numBottles
            numBottles = (numBottles + restBottles) // numExchange
            restBottles = (aux + restBottles) % numExchange
            count += numBottles
        return count
        
