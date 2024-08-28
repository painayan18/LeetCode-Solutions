def main():
    pass


def insert(intervals: [[int]], new_interval: [int]) -> [[int]]:

    result = []
    i = 0
    n = len(intervals)

    # add all lesser intervals
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # merge overlapping
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


main()
