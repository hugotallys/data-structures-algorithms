from random import randint

def swap(arr, i, j):
    """Swaps arr[i] and arr[j] inplace."""
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition3(array, left, right):
    x = array[right]
    i = left - 1
    k = left - 1
    for j in range(left, right):
        if array[j] < x:
            i = i + 1
            swap(array, i, j)
        if array[j] == x:
            k = max(i, k) + 1
            swap(array, k, j)
    t = max(i, k)
    swap(array, t + 1, right)
    return i + 1, t + 1

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
