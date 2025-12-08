"""
Quicksort algorithm implementation.
"""

def swap(arr, i, j):
    """Swaps arr[i] and arr[j] inplace."""
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition3(arr, p, r):
    """
    Rearranges arr[p...r] returning indexes q, s such that:
    p   <= k <= q-1 -> arr[k] < arr[r]
    s+1 <= k <= r   -> arr[k] >  arr[r]
    q   <= k <= s   -> arr[k] == arr[r]
    """
    x = arr[r]
    i = p - 1
    k = p - 1
    for j in range(p, r):
        if arr[j] < x:
            i = i + 1
            swap(arr, i, j)
        if arr[j] == x:
            k = max(i, k) + 1
            swap(arr, k, j)
    t = max(i, k)
    swap(arr, t + 1, r)
    return i + 1, t + 1

def quicksort(arr, p, r):
    """
    Sort the array inplace in O(n*n) (worst scenario).
    """
    if p < r:
        q, s = partition3(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, s+1, r)

if __name__ == "__main__":
    numbers = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11, 11, 11, 11, 11, 11, 11]
    print(f"Numbers = {numbers}")
    quicksort(numbers, 0, len(numbers)-1)
    print(f"Sorted Numbers = {numbers}")
