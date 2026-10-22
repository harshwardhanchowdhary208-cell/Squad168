# Question 8: Sliding Window - Longest Subarray Within a Limit
# Given an array of non-negative integers and a limit L, find the length of
# the longest contiguous subarray whose sum is at most L. Aim for an O(n)
# sliding-window solution.
# Input: an integer n and a non-negative integer L, followed by n
# space-separated non-negative integers.

import sys


def longest_subarray_with_sum_at_most(
    values: list[int], limit: int
) -> int:
    if limit < 0:
        raise ValueError("The limit must be non-negative.")
    if any(value < 0 for value in values):
        raise ValueError("Every array value must be non-negative.")

    left = 0
    window_sum = 0
    longest = 0
    for right, value in enumerate(values):
        window_sum += value
        while window_sum > limit:
            window_sum -= values[left]
            left += 1
        longest = max(longest, right - left + 1)
    return longest


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Input must include the array length and limit.")

    size, limit = data[:2]
    values = data[2:]
    if size < 0 or len(values) != size:
        raise ValueError(f"Expected a non-negative length and {size} values.")
    print(longest_subarray_with_sum_at_most(values, limit))


if __name__ == "__main__":
    main()
