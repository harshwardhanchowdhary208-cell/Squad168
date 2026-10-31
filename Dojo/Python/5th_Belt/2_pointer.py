# Level 5 - Blue Belt
# Two-pointer technique: find the pair whose sum is closest to the target.
# The input array is sorted before applying the standard two-pointer strategy.


def find_closest_pair(arr, target):
    arr = sorted(arr)
    left, right = 0, len(arr) - 1
    best_pair = (arr[0], arr[-1]) if arr else (None, None)
    min_diff = float('inf')
    best_sum = None

    while left < right:
        current_sum = arr[left] + arr[right]
        current_diff = abs(current_sum - target)

        if current_diff < min_diff:
            min_diff = current_diff
            best_pair = (arr[left], arr[right])
            best_sum = current_sum
        elif current_diff == min_diff and best_sum is not None and current_sum < best_sum:
            best_pair = (arr[left], arr[right])
            best_sum = current_sum

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            break

    return best_pair


def solve():
    data = input().strip().split()
    if not data:
        return

    n, target = map(int, data[:2])
    arr = list(map(int, input().split()[:n]))
    pair = find_closest_pair(arr, target)
    print(pair[0], pair[1])


if __name__ == "__main__":
    solve()
