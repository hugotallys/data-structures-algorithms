"""
Closest pair of points problem.
Given a set of points (x, y) in the plane find the minimum distance between any of them.
"""

from collections import namedtuple
from math import sqrt

Point = namedtuple("Point", ["x", "y"])


def distance(first_point, second_point):
    dx2 = (first_point.x - second_point.x) ** 2
    dy2 = (first_point.y - second_point.y) ** 2
    return sqrt(dx2 + dy2)


def minimum_distance(points):

    l = len(points) - 1

    if l == 0:
        return float("inf")
    if l == 1:
        [first_point, second_point] = points
        return distance(first_point, second_point)

    m = l // 2
    d1 = minimum_distance(points[:m])
    d2 = minimum_distance(points[m:])

    d = min(d1, d2)

    cut = (points[m - 1].x + points[m].x) / 2
    cross_points = list(filter(lambda p: cut - d <= p.x <= cut + d, points))

    cross_points = sorted(cross_points, key=lambda p: p.y)

    cross_d = float("inf")
    for i, cp in enumerate(cross_points):
        for j in range(1, 8):
            if i + j < len(cross_points):
                cross_d = min(cross_d, distance(cp, cross_points[i + j]))
            else:
                break

    return min(d, cross_d)


if __name__ == "__main__":
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    input_points = list(sorted(input_points, key=lambda p: p.x))

    print("{0:.9f}".format(minimum_distance(input_points)))
