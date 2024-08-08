import numpy as np


def fibonacci_sequence(n):
    """
    The Fibonacci sequence is a series of numbers in which each number
    (after the first two) is the sum of the two preceding ones.
    """
    sequence = []
    for i in range(n):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def knapsack_01(weights: list, values: list, capacity: int):
    """
    It involves selecting a subset of items to maximize the total value while staying
    within a specified weight limit.
    0 is excluded and 1 is included

    Args:
    weights : list of weights item
    values: list of value
    capacity: maximum weight capacity

    """
    nums_items = len(values)  # number of value items
    dp = [
        [0 for _ in range(capacity + 1)] for _ in range(nums_items + 1)
    ]  # 2D arrays with item and its weights
    for i in range(1, nums_items + 1):  # loop through the item
        for w in range(1, capacity + 1):  # loop through the weight
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
                # dp[i-1][w] : maximum value without including current item
                # values[i - 1] + dp[i - 1][w - weights[i - 1]]: The value of the current item plus the
                # maximum value obtainable with the remaining capacity after including the current item.
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[nums_items][capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
# print(knapsack_01(weights, values, capacity))


dp = [[0 for _ in range(capacity + 1)] for _ in range(len(values) + 1)]
print(np.matrix(dp))
