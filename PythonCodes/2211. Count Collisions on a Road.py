class Solution:
    def countCollisions(self, directions: str) -> int:
        rights = 0
        collisions = 0
        stopped = False
        for elem in directions:
            if elem == "S":
                stopped = True
            if elem == "R":
                rights += 1
            elif rights or stopped:
                if elem == "L":
                    collisions += rights + 1
                    stopped = True
                else:
                    collisions += rights
                rights = 0
        return collisions
