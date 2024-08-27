def main():
    senate1 = "RD"
    senate2 = "RDD"

    print("Input:", senate1, ", output:", predict_party_victory(senate1))
    print("Input:", senate2, ", output:", predict_party_victory(senate2))


def predict_party_victory(senate: str) -> str:
    from collections import deque

    radiant = deque()
    dire = deque()

    for index, senator in enumerate(senate):
        if senator == "R":
            radiant.append(index)
        else:
            dire.append(index)

    q_len = len(senate)

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()

        if r < d:
            radiant.append(r + q_len)
        else:
            dire.append(d + q_len)

    return "Radiant" if radiant else "Dire"


main()
