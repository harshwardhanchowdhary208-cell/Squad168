# Question:
# Given an array of integers, move all zeroes to the end while keeping the relative order of non-zero elements.
#
# Input:
# The first line contains an integer n.
# The second line contains n integers.
#
# Output:
# Print the array after moving all zeroes to the end.

from typing import List


def move_zeroes(arr: List[int]) -> List[int]:
    write_index = 0

    for value in arr:
        if value != 0:
            arr[write_index] = value
            write_index += 1

    while write_index < len(arr):
        arr[write_index] = 0
        write_index += 1

    return arr


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = move_zeroes(arr)
    print(" ".join(map(str, result)))
