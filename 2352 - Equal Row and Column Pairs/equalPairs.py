from collections import defaultdict


def main():
    # test input 1
    grid1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    # result = 1

    # test input 2
    grid2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    # result = 3

    print(equal_pairs(grid1))
    print(equal_pairs(grid2))


def equal_pairs(grid: [[int]]) -> int:

    rows = defaultdict(int)
    pair_counter = 0

    for row in grid:
        rows[str(row)] += 1

    for i in range(len(grid)):
        col = []
        for j in range(len(grid)):
            col.append(grid[j][i])

        pair_counter += rows[str(col)]

    return pair_counter


main()
