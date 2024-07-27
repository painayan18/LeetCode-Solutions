class Solution:
    def longestSubarray(self, nums: [int]) -> int:
        left = right = 0
        maxOnes = 0
        zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            maxOnes = max(maxOnes, right - left + 1 - zeroes)

        if maxOnes == (len(nums)):
            return maxOnes - 1

        return maxOnes
