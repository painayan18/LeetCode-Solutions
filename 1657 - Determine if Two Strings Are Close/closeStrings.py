def main():
    print(close_strings("abc", "bca"))
    print(close_strings("a", "aa"))
    print(close_strings("cabbba", "abbccc"))


def close_strings(word1: str, word2: str) -> bool:

    # if the letters in the words are not the same
    # return false
    if set(word1) != set(word2):
        return False

    freq1 = {}
    freq2 = {}

    for char in word1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in word2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    sorted1 = sorted(freq1.values())
    sorted2 = sorted(freq2.values())

    return sorted1 == sorted2


main()
