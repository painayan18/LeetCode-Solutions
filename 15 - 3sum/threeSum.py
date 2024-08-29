def main():
    test1 = [-1, 0, 1, 2, -1, -4]
    test2 = [0, 1, 1]
    test3 = [0, 0, 0]

    print(three_sum(test1))
    print(three_sum(test2))
    print(three_sum(test3))


def three_sum(nums: [int]) -> [[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # move left pointer past duplicated
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # move right pointer past duplicates
                while left < right < (len(nums) - 1)\
                        and nums[right] == nums[right + 1]:
                    right -= 1

    return result


main()
