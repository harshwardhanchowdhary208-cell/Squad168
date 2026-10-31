# Question 3: Frequency Map and Duplicate Detection
# Given an array of integers, print each distinct value and its frequency in
# the order the value first appears. Then print the values that occur more
# than once.
# Input: an integer n, followed by n space-separated integers.

import sys


def frequencies_and_duplicates(
    values: list[int],
) -> tuple[dict[int, int], list[int]]:
    frequencies: dict[int, int] = {}
    for value in values:
        frequencies[value] = frequencies.get(value, 0) + 1
    duplicates = [
        value for value, count in frequencies.items() if count > 1
    ]
    return frequencies, duplicates


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Input must include the array length.")

    size = data[0]
    if size < 0 or len(data) != size + 1:
        raise ValueError(f"Expected a non-negative length and {size} values.")
    frequencies, duplicates = frequencies_and_duplicates(data[1:])
    for value, count in frequencies.items():
        print(f"{value}: {count}")
    print("Duplicates:", *duplicates)


if __name__ == "__main__":
    main()
