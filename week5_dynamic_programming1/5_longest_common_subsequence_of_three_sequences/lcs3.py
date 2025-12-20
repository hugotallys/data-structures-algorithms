def lcs3(first_sequence, second_sequence, third_sequence):

    l1 = len(first_sequence)
    l2 = len(second_sequence)
    l3 = len(third_sequence)

    lcs = [[[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)] for _ in range(l3 + 1)]

    for k in range(1, l3 + 1):
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                first = first_sequence[j - 1]
                second = second_sequence[i - 1]
                third = third_sequence[k - 1]

                if first == second == third:
                    lcs[k][i][j] = lcs[k - 1][i - 1][j - 1] + 1
                else:
                    lcs[k][i][j] = max(
                        lcs[k - 1][i][j], lcs[k][i - 1][j], lcs[k][i][j - 1]
                    )

    return lcs[l3][l2][l1]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
