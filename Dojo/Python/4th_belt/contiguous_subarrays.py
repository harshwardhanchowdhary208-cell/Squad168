# Question 1: Print All Contiguous Subarrays
# Given an array of n integers, print every contiguous subarray, one per line.
# Keep the elements in their original order.
# Input: an integer n, followed by n space-separated integers.

import sys


def contiguous_subarrays(values: list[int]) -> None:
    for start in range(len(values)):
        for end in range(start + 1, len(values) + 1):
            print(*values[start:end])


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Input must include the array length.")

    size = data[0]
    if size < 0 or len(data) != size + 1:
        raise ValueError(f"Expected a non-negative length and {size} values.")
    contiguous_subarrays(data[1:])


if __name__ == "__main__":
    main()
