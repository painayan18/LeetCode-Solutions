def main():
    test1 = [1, 2, 3, 4]
    test2 = [-1, 1, 0, -3, 3]

    print(product_except_self(test1))
    print(product_except_self(test2))


def product_except_self(nums: [int]) -> [int]:
    result = [1] * len(nums)

    # multiply pre-fixes
    prefix = 1
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]

    # multiply post-fixes
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


main()
