import math

def argmin(arr):
    return min(range(len(arr)), key=arr.__getitem__)

def compute_operations(n):
    if n == 1:
        return [1]
    
    n = n + 1
    n_ops = [0 for _ in range(n)]
    i_ops = [-1, -1]
    
    n_ops[1] = 0
    
    for i in range(2, n):
        cost = [n_ops[i-1] + 1, math.inf, math.inf]
        
        if i % 2 == 0:
            cost[1] = n_ops[i // 2] + 1
        if i % 3 == 0:
            cost[2] = n_ops[i // 3] + 1
        
        least_cost = argmin(cost)
        n_ops[i] = cost[least_cost]
        i_ops.append(least_cost)
    
    result = []
    
    while i > 1:
        result.append(i)
        
        if i_ops[i] == 0:
            i = i - 1
        elif i_ops[i] == 1:
            i = i // 2
        else:
            i = i // 3

    result.append(1)
    
    result = list(reversed(result))
    
    return result


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
