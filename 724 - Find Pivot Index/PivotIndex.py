class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            if nums[0] == 0:
                return 1
            elif nums[1] == 0:
                return 0
            return -1

        for i in range(len(nums)):
            if i == 0 and sum(nums[1:]) == 0:
                return 0
            if sum(nums[i+1:]) == sum(nums[:i+1]):
                return 1

        return -1
