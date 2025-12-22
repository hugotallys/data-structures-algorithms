def multiply(A, B, m=None):
    C = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
                if m is not None:
                    C[i][j] = C[i][j] % m

    return C

def matrix_power_sum(M, n, m):
    if n == 0:
        return [[1, 0], [0, 1]]

    if n == 1:
        return M
    
    M2 = multiply(M, M, m)
        
    if n % 2:
        return multiply(M, matrix_power_sum(M2, n // 2, m), m)

    return matrix_power_sum(M2, n // 2, m)

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    M = [[1, 1], [1, 0]]
    M = matrix_power_sum(M, n, 10)
    fn = M[1][0]

    M = [[1, 1], [1, 0]]
    M = matrix_power_sum(M, n+1, 10)
    fn1 = M[1][0]

    return (fn * fn1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))

