def majority_element_naive(elements):
    count = {}
    for e in elements:
        if e not in count:
            count[e] = 1
        else:
            count[e] += 1
    max_count = max(count.values())

    if max_count > len(elements) / 2:
        return 1

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
