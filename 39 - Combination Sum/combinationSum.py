def main():
    # test1
    candidates1, target1 = [2, 3, 6, 7], 7
    print(combination_sum(candidates1, target1))
    # expected: [[2,2,3],[7]]

    # test2
    candidates2, target2 = [2, 3, 5], 8
    print(combination_sum(candidates2, target2))
    # expected: [[2,2,2,2],[2,3,3],[3,5]]

    # test3 = 0
    candidates3, target3 = [2], 1
    print(combination_sum(candidates3, target3))
    # expected: []


def combination_sum(candidates: [int], target: int) -> [[int]]:
    result = []

    def dfs(i, current, total):
        if total == target:
            result.append(current.copy())
            return
        if i >= len(candidates) or total > target:
            return

        current.append(candidates[i])

        # decision left
        dfs(i, current, total + candidates[i])
        current.pop()

        # decision right
        dfs(i + 1, current, total)

    dfs(0, [], 0)
    return result


main()
