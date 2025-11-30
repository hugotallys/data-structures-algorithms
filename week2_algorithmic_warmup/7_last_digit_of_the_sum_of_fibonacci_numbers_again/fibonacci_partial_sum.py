def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

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

def fibonacci_partial_sum(from_, to):
    M = [[1, 1], [1, 0]]
    M = matrix_power_sum(M, to + 2, 10)
    f_to = M[1][0]

    M = [[1, 1], [1, 0]]
    M = matrix_power_sum(M, from_ + 1, 10)
    f_from = M[1][0]

    return (f_to - f_from) % 10

if __name__ == '__main__':
    _input = input() # sys.stdin.read()
    from_, to = map(int, _input.split())
    print(fibonacci_partial_sum(from_, to))
