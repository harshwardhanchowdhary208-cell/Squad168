# Question 4: Maximum-Sum Subarray (Kadane's Algorithm)
# Given an array containing positive, negative, or zero values, find the
# contiguous subarray with the largest sum. Print the maximum sum. If multiple
# subarrays have that sum, any one of them is acceptable.
# Input: an integer n (n >= 1), followed by n space-separated integers.

import sys


def maximum_subarray(values: list[int]) -> tuple[int, list[int]]:
    if not values:
        raise ValueError("The array must contain at least one integer.")

    best_sum = current_sum = values[0]
    best_start = best_end = current_start = 0

    for index in range(1, len(values)):
        value = values[index]
        if current_sum + value < value:
            current_sum = value
            current_start = index
        else:
            current_sum += value

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = index

    return best_sum, values[best_start : best_end + 1]


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Input must include the array length.")

    size = data[0]
    if size < 1 or len(data) != size + 1:
        raise ValueError(f"Expected a positive length and {size} values.")
    maximum_sum, _subarray = maximum_subarray(data[1:])
    print(maximum_sum)


if __name__ == "__main__":
    main()
