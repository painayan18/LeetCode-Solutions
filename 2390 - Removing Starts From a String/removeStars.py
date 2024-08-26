def main():
    s1 = "leet**cod*e"
    s2 = "erase*****"

    print("input:", s1, "output:", remove_stars(s1))
    print("input:", s2, "output:", remove_stars(s2))


def remove_stars(s: str) -> str:
    if len(s) == 0:
        return ""

    result = []

    for char in s:
        if char == "*":
            result.pop()
        else:
            result.append(char)

    return ''.join(result)


main()
