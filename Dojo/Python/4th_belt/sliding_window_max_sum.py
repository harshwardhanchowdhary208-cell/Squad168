# Question 7: Sliding Window - Maximum Sum of Size k
# Given an array of n integers and an integer k, find the maximum sum of any
# contiguous subarray of exactly k elements. Aim for an O(n) sliding window.
# Input: two integers n and k, followed by n space-separated integers.

import sys


def maximum_window_sum(values: list[int], k: int) -> int:
    if not 1 <= k <= len(values):
        raise ValueError("k must be between 1 and the array length.")

    window_sum = sum(values[:k])
    maximum = window_sum
    for index in range(k, len(values)):
        window_sum += values[index] - values[index - k]
        maximum = max(maximum, window_sum)
    return maximum


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Input must include the array length and k.")

    size, k = data[:2]
    values = data[2:]
    if size < 0 or len(values) != size:
        raise ValueError(f"Expected a non-negative length and {size} values.")
    print(maximum_window_sum(values, k))


if __name__ == "__main__":
    main()
