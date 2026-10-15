import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    rows, columns = data[:2]
    values = data[2:2 + rows * columns]
    matrix = [
        values[index:index + columns]
        for index in range(0, rows * columns, columns)
    ]

    top, bottom = 0, rows - 1
    left, right = 0, columns - 1
    spiral_order = []

    while top <= bottom and left <= right:
        spiral_order.extend(matrix[top][left:right + 1])
        top += 1

        for row in range(top, bottom + 1):
            spiral_order.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            spiral_order.extend(matrix[bottom][left:right + 1][::-1])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                spiral_order.append(matrix[row][left])
            left += 1

    print(*spiral_order)


if __name__ == "__main__":
    main()
