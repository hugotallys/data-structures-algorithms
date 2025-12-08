import math


def change(money, coins):
    minimum_coins = [0 for _ in range(money + 1)]
    for m in range(1, money + 1):
        minimum_coins[m] = math.inf
        for i, coin_i in enumerate(coins):
            if m >= coins[i]:
                if minimum_coins[m - coins[i]] + 1 < minimum_coins[m]:
                    minimum_coins[m] = minimum_coins[m - coins[i]] + 1
    return minimum_coins[money]


if __name__ == "__main__":
    m = int(input())
    print(change(m, [1, 8, 20]))
