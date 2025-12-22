def merge(arr, p, q, r, inv):
    n1 = q - p + 1
    n2 = r - q
    
    left = arr[p: q + 1]
    right = arr[q + 1: r + 1]
    
    k = p
    i, j = 0, 0
    
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inv[0] += n1 - i
        k += 1
        
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while k < n2:
        arr[k] = right[j]
        j += 1
        k += 1
            
def merge_sort(arr, p, r, inv):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q, inv)
        merge_sort(arr, q+1, r, inv)
        merge(arr, p, q, r, inv)

def inversions(a):
    n_inv = [0]
    merge_sort(a, 0, len(a) - 1, n_inv)
    return n_inv[0]

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions(elements))
