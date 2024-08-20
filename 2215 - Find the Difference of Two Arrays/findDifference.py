class Solution:
    def findDifference(self, nums1: [int], nums2: [int]) -> [[int]]:
        out1, out2 = [], []

        for i in nums1:
            if i not in nums2 and i not in out1:
                out1.append(i)

        for j in nums2:
            if j not in nums1 and j not in out2:
                out2.append(j)

        return [out1, out2]

