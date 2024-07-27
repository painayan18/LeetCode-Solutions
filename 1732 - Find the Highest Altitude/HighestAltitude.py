class Solution:
    def largestAltitude(self, gain: [int]) -> int:
        alt = 0
        gain_i = 0
        gain.append(0)  # make space at the end of the list
        # will later get replaced by last altitude, since first
        # gain is replaced by first alt.

        for i in range(len(gain)):
            gain_i = gain[i]
            gain[i] = alt
            alt += gain_i

        return max(gain)
