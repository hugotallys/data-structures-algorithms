def lcs2(first_sequence, second_sequence):

    l1 = len(first_sequence)
    l2 = len(second_sequence)

    lcs = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]

    for i in range(1, l2 + 1):
        for j in range(1, l1 + 1):
            if first_sequence[j - 1] == second_sequence[i - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs[l2][l1]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))

