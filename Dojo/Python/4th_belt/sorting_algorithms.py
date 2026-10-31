# Question 6: Implement the Basic Sorting Algorithms
# Implement selection sort, bubble sort, insertion sort, quick sort, and
# merge sort to sort an integer array in ascending order. Test each with an
# empty array, an already-sorted array, a reverse-sorted array, and an array
# containing duplicates. Do not use a built-in sorting function.
# Input: an integer n, followed by n space-separated integers.

import sys


def selection_sort(values: list[int]) -> list[int]:
    result = values.copy()
    for index in range(len(result)):
        smallest = index
        for candidate in range(index + 1, len(result)):
            if result[candidate] < result[smallest]:
                smallest = candidate
        result[index], result[smallest] = result[smallest], result[index]
    return result


def bubble_sort(values: list[int]) -> list[int]:
    result = values.copy()
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = (
                    result[index + 1],
                    result[index],
                )
                swapped = True
        if not swapped:
            break
    return result


def insertion_sort(values: list[int]) -> list[int]:
    result = values.copy()
    for index in range(1, len(result)):
        value = result[index]
        position = index - 1
        while position >= 0 and result[position] > value:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = value
    return result


def quick_sort(values: list[int]) -> list[int]:
    result = values.copy()

    def sort_range(low: int, high: int) -> None:
        if low >= high:
            return

        pivot = result[high]
        boundary = low
        for index in range(low, high):
            if result[index] <= pivot:
                result[boundary], result[index] = result[index], result[boundary]
                boundary += 1
        result[boundary], result[high] = result[high], result[boundary]
        sort_range(low, boundary - 1)
        sort_range(boundary + 1, high)

    sort_range(0, len(result) - 1)
    return result


def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return values.copy()

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    merged: list[int] = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


SORTING_ALGORITHMS = {
    "Selection sort": selection_sort,
    "Bubble sort": bubble_sort,
    "Insertion sort": insertion_sort,
    "Quick sort": quick_sort,
    "Merge sort": merge_sort,
}


def test_sorting_algorithms() -> None:
    test_cases = [
        [],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 2, 3, 1],
    ]
    for sort in SORTING_ALGORITHMS.values():
        for values in test_cases:
            if sort(values) != selection_sort(values):
                raise AssertionError(
                    f"{sort.__name__} failed for input {values}"
                )


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Input must include the array length.")

    size = data[0]
    if size < 0 or len(data) != size + 1:
        raise ValueError(f"Expected a non-negative length and {size} values.")
    values = data[1:]

    test_sorting_algorithms()
    for name, sort in SORTING_ALGORITHMS.items():
        print(f"{name}:", *sort(values))


if __name__ == "__main__":
    main()
