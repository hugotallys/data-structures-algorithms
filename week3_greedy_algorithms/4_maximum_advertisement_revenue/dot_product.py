def max_dot_product(first_sequence, second_sequence):
    first_sequence = sorted(first_sequence)
    second_sequence = sorted(second_sequence)

    max_product = 0
    for f, s in zip(first_sequence, second_sequence):
        max_product += f * s

    return max_product


if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
