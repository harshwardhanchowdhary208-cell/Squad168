# Question 2: Prefix and Suffix Sums
# Given an array of n integers, print its prefix-sum array and suffix-sum
# array. A prefix sum at index i is the sum from index 0 through i; a suffix
# sum at index i is the sum from index i through n - 1.
# Input: an integer n, followed by n space-separated integers.
# Output: prefix sums on the first line and suffix sums on the second line.

import sys


def prefix_and_suffix_sums(values: list[int]) -> tuple[list[int], list[int]]:
    prefix: list[int] = []
    running_sum = 0
    for value in values:
        running_sum += value
        prefix.append(running_sum)

    suffix = [0] * len(values)
    running_sum = 0
    for index in range(len(values) - 1, -1, -1):
        running_sum += values[index]
        suffix[index] = running_sum
    return prefix, suffix


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Input must include the array length.")

    size = data[0]
    if size < 0 or len(data) != size + 1:
        raise ValueError(f"Expected a non-negative length and {size} values.")
    prefix, suffix = prefix_and_suffix_sums(data[1:])
    print(*prefix)
    print(*suffix)


if __name__ == "__main__":
    main()
