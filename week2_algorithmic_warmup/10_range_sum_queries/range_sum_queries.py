def range_sum(arr, queries):
    result = []
    for l, r in queries:
        result.append(sum(arr[l:r+1]))
    return result

arr = [2, -1, 7, 2, -3, -2, 4]
result = range_sum(
    arr, [(1, 3), (2, 5)]
)

print(arr)
print("Range sum queries:")
print(result)
