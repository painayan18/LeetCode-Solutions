class Solution:
    def pivot_index(self, nums: [int]) -> int:
        left, right = 0, sum(nums)

        for index, num in enumerate(nums):
            right -= num

            if left == right:
                return index

            left += num

        return -1
