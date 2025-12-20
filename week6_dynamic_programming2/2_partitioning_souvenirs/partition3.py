"""
Three partition problem.
"""

from sys import stdin


def recursive_partition3(values, cache, s1, s2, s3, target):
    if s1 == s2 == s3 and len(values) == 0:
        return 1

    if s1 > target or s2 > target or s3 > target or len(values) == 0 or cache[s1][s2][s3]:
        return 0

    set1 = recursive_partition3(values[1:], cache, s1 + values[0], s2, s3, target)

    if set1 == 1:
        return 1

    set2 = recursive_partition3(values[1:], cache, s1, s2 + values[0], s3, target)

    if set2 == 1:
        return 1

    set3 = recursive_partition3(values[1:], cache, s1, s2, s3 + values[0], target)

    if set3 == 1:
        return 1

    cache[s1][s2][s3] = 1
    cache[s1][s3][s2] = 1
    cache[s2][s1][s3] = 1
    cache[s2][s3][s1] = 1
    cache[s3][s1][s2] = 1
    cache[s3][s2][s1] = 1

    return 0


def partition3(values):
    total = sum(values)
    if not total % 3:
        total = total // 3
        cache = [
            [[0 for _ in range(total + 1)] for _ in range(total + 1)]
            for _ in range(total + 1)
        ]
        return recursive_partition3(values, cache, 0, 0, 0, total)
    return 0


if __name__ == "__main__":
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    # input_values = [1, 1, 1]

    print(partition3(input_values))
