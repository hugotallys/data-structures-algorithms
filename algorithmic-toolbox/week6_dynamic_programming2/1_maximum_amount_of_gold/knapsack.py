from sys import stdin


def maximum_gold(capacity, weights):
    n, W = len(weights), capacity

    K = [[0 for _ in range(n + 1)] for _ in range(W + 1)]

    for j in range(1, n + 1):
        for w in range(1, W + 1):
            wj = weights[j - 1]
            if wj > w:
                K[w][j] = K[w][j - 1]
            else:
                K[w][j] = max(K[w][j - 1], K[w - wj][j - 1] + wj)

    return K[W][n]


if __name__ == "__main__":
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))

