from collections import namedtuple
from sys import stdin

Segment = namedtuple("Segment", "start end")


def leftmost_segment(segments):
    min_i = 0
    min_value = segments[min_i].start
    for i, value in enumerate(segments):
        if value.start <= min_value:
            min_i, min_value = i, value.start
    return min_i


def neighbors(seg, segments):
    query_seg = segments[seg]
    neighbors_segs = []
    for i, s in enumerate(segments):
        if query_seg.start <= s.start <= query_seg.end:
            neighbors_segs.append(i)
    return neighbors_segs


def recursive_points(segments, points):
    if len(segments) == 0:
        return points
    left_seg = leftmost_segment(segments)
    L = neighbors(left_seg, segments)
    end_min = min(map(lambda x: segments[x].end, L))
    points.append(end_min)
    for l in L:
        if segments[l].start <= end_min <= segments[l].end:
            segments[l] = None
    segments = list(filter(lambda x: x is not None, segments))
    return recursive_points(segments, points)


def optimal_points(segments):
    return recursive_points(segments, [])


if __name__ == "__main__":
    _input = stdin.read()
    n, *data = map(int, _input.split())
    input_segments = list(
        map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2]))
    )
    # input_segments = [(1, 3), (2, 5), (3, 6)]
    # input_segments = [(4, 7), (1, 3), (2, 5), (5, 6)]
    # input_segments = list(map(lambda x: Segment(x[0], x[1]), input_segments))
    result = optimal_points(input_segments)
    print(len(result))
    print(*result)
