# Question 5: Dutch National Flag
# Given an array containing only 0, 1, and 2, rearrange it in-place so that
# all zeroes come first, followed by ones, followed by twos. Do not use a
# built-in sorting function.
# Input: an integer n, followed by n values, each either 0, 1, or 2.

import sys


def dutch_national_flag(values: list[int]) -> list[int]:
    if any(value not in (0, 1, 2) for value in values):
        raise ValueError("Every array value must be 0, 1, or 2.")

    low = current = 0
    high = len(values) - 1
    while current <= high:
        if values[current] == 0:
            values[low], values[current] = values[current], values[low]
            low += 1
            current += 1
        elif values[current] == 1:
            current += 1
        else:
            values[current], values[high] = values[high], values[current]
            high -= 1
    return values


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Input must include the array length.")

    size = data[0]
    if size < 0 or len(data) != size + 1:
        raise ValueError(f"Expected a non-negative length and {size} values.")
    print(*dutch_national_flag(data[1:]))


if __name__ == "__main__":
    main()
