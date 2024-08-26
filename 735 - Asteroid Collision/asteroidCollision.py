def main():
    asteroids1 = [5, 10, -5]
    asteroids2 = [8, -8]
    asteroids3 = [10, 2, -5]
    asteroids4 = [-2, -1, 1, 2]

    print("input:", asteroids1, "output: ", asteroid_collision(asteroids1))
    print("input:", asteroids2, "output: ", asteroid_collision(asteroids2))
    print("input:", asteroids3, "output: ", asteroid_collision(asteroids3))
    print("input:", asteroids4, "output: ", asteroid_collision(asteroids4))


def asteroid_collision(asteroids: [int]) -> [int]:
    result = []

    for a in asteroids:

        while result and a < 0 < result[-1]:
            if -a > result[-1]:
                result.pop()
                continue
            elif -a == result[-1]:
                result.pop()
            break
        else:
            result.append(a)

    return result


main()
