from functools import cmp_to_key


def compare_concatenate(a, b):
    ab = int(str(a) + str(b))
    if ab > (int(str(b) + str(a))):
        return -1
    return 1


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    numbers = sorted(numbers, key=cmp_to_key(compare_concatenate))

    return int("".join(numbers))


if __name__ == "__main__":
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
