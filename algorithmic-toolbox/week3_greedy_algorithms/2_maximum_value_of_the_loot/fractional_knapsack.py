from sys import stdin


def best_item(w, v, w_):
    idx, best = 0, 0
    for i, (wi, vi) in enumerate(zip(w, v)):
        if ((vi / wi) > best) and w_[i]:
            idx = i
            best = vi / wi

    w_[idx] = 0

    return idx, best


def optimal_value(capacity, weights, values):
    value = 0.0

    weights_ = list(weights)  # [w for w in weights]

    while capacity > 0:
        pick, pick_value = best_item(weights, values, weights_)
        if weights[pick] <= capacity:
            capacity -= weights[pick]
            value += weights[pick] * pick_value
        else:
            value += capacity * pick_value
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))

    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]

    opt_value = optimal_value(capacity, weights, values)
    print(f"{opt_value:.4f}")
