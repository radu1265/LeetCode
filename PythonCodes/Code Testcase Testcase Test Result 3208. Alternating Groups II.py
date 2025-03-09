class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        print(colors)
        change = colors[0]
        nr_changes = 1
        nr_cycles = 0
        for i in range(1, len(colors)):
            if change != colors[i]:
                nr_changes += 1
                if nr_changes == k:
                    nr_cycles += 1
                    nr_changes -= 1
                change = colors[i]
            else:
                nr_changes = 1
        return nr_cycles
