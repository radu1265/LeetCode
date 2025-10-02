class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        cur_altitude = 0

        for g in gain:
            cur_altitude += g
            max_altitude = max(max_altitude, cur_altitude)
        return max_altitude
