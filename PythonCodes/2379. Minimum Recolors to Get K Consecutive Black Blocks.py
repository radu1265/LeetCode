class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_white = 0
        for i in range(k):
            if blocks[i] == 'W':
                count_white += 1
        minim = count_white
        for b in range(k, len(blocks)):
            if blocks[b] == 'W':
                if blocks[b - k] == 'B':
                    count_white += 1
            else:
                if blocks[b - k] == 'W':
                    count_white -= 1
            minim = min(minim, count_white)
        return 0 if minim < 0 else minim
