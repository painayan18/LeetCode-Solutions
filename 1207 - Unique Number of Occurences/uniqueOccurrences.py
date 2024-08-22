

def main():
    test1 = [1, 2, 2, 1, 1, 3]
    test2 = [1, 2]

    print(unique_occurrences(test1))
    print(unique_occurrences(test2))


def unique_occurrences(arr: [int]) -> bool:
    output = {}

    for i in range(len(arr)):
        if output.get(arr[i]) is not None:
            output[arr[i]] += 1
        else:
            output[arr[i]] = 1

    seen = set()

    for value in output.values():
        if value in seen:
            return False
        else:
            seen.add(value)

    return True


main()
