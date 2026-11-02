# Print the text Matrix subtraction result:
# Then print the resulting matrix after subtraction, with each row on a new line and elements separated by a space.
#
# Example 1:
# Input:
# 2 2
# 1 2
# 3 4
# 1 1
# 1 1
#
# Output:
# Matrix subtraction result:
# 0 1
# 2 3

# Read rows and columns
rows, cols = map(int, input().split())

# Only store the first matrix to satisfy the space complexity constraints
matrix1 = []
for _ in range(rows):
    matrix1.append(list(map(int, input().split())))

print("Matrix subtraction result:")

# Process the second matrix row-by-row and print the results immediately
for i in range(rows):
    row2 = list(map(int, input().split()))
    # Calculate and print the subtracted row without storing it in a third matrix
    result_row = [matrix1[i][j] - row2[j] for j in range(cols)]
    print(*result_row)
