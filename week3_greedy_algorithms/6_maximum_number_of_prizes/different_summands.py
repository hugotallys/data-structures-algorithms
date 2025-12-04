import math


def optimal_summands(n):

    sizes = []

    k = int(math.sqrt(2*n))

    for i in range(1, k + 1):
        remaining = n - i
        if remaining > i:
            sizes.append(i)
            n = remaining
        else:
            sizes.append(i + remaining)
            return sizes

    return sizes


if __name__ == "__main__":
    n_input = int(input())
    summands = optimal_summands(n_input)
    print(len(summands))
    print(*summands)
