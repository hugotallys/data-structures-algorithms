"""
Quicksort algorithm implementation.
"""

def swap(arr, i, j):
    """Swaps arr[i] and arr[j] inplace."""
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(arr, p, r):
    """
    Rearranges arr[p...r] returning an index q such that:
    p   <= k <= q-1 -> arr[k] <= arr[r]
    q+1 <= k <= r   -> arr[k] >  arr[r]
    q   == k        -> arr[k] == arr[r]
    """
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            swap(arr, i, j)
    swap(arr, i + 1, r)
    return i + 1

def quicksort(arr, p, r):
    """
    Sort the array inplace in O(n*n) (worst scenario).
    """
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, q+1, r)

if __name__ == "__main__":
    numbers = [2, 8, 7, 1, 3, 5, 6, 4]
    print(f"Numbers = {numbers}")
    quicksort(numbers, 0, len(numbers)-1)
    print(f"Sorted Numbers = {numbers}")
