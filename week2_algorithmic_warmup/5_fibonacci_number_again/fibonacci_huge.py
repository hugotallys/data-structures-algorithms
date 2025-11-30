def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def multiply(A, B, m=None):
    C = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
                if m is not None:
                    C[i][j] = C[i][j] % m

    return C

def matrix_power(M, n, m):
    if n == 1:
        return M
    
    M2 = multiply(M, M, m)
    
    if n % 2:
        return multiply(M, matrix_power(M2, n // 2, m), m)

    return matrix_power(M2, n // 2, m)

def fibonacci_huge(n, m):
    M = [[1, 1], [1, 0]]
    
    M = matrix_power(M, n, m)
    
    return M[1][0]


if __name__ == '__main__':
    n, m = map(int, input().split())
    # print(fibonacci_huge_naive(n, m))
    print(fibonacci_huge(n, m))
