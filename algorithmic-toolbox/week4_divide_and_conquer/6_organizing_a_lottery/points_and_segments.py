from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

def points_cover(starts, ends, points):
    assert len(starts) == len(ends)
    result = [0] * len(points)
    
    points = sorted(
        [(p, i) for i, p in enumerate(points)], key=lambda x: x[0]
    )
    
    starts = [(s, -1) for s in starts]
    ends = [(e, 1) for e in ends]
    
    count = 0
    segments = sorted(starts + ends, key=lambda x: x[0], reverse=True)
    
    for point, i in points:
        s = 0
        while len(segments) !=  0 and segments[-1][0] <= point:
            count += segments[s][1]
            s = s + 1
            segments.pop()
        result[i] = count
    
    return result

if __name__ == '__main__':
    # data = list(map(int, stdin.read().split()))
    # n, m = data[0], data[1]
    # input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    # input_points = data[2 * n + 2:]
    
    input_starts = [0, 1, 3]
    input_ends = [3, 3, 8]
    input_points = [-1, 3, 8]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
