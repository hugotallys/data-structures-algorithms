from sys import stdin


def min_refills(distance, tank, stops):
    refills = [0]
    return recursive_min_refills(distance, tank, stops, refills)


def recursive_min_refills(distance, tank, stops, refills):
    if len(stops) == 0:
        if distance <= tank:
            return refills[0]
        return -1

    stops = [0] + stops + [distance]

    s, station = None, None
    for s, station in enumerate(stops):
        if stops[s] > tank:
            refills[0] += 1
            s, station = s - 1, stops[s - 1]
            break

    if station == 0:
        return -1

    for i in range(s, len(stops)):
        stops[i] -= station

    return recursive_min_refills(stops[-1], tank, stops[s + 1 : -1], refills)


if __name__ == "__main__":
    d, m, _, *stops = map(int, stdin.read().split())
    # d, m, stops = 600, 200, [100, 200, 300, 400]
    print(min_refills(d, m, stops))
