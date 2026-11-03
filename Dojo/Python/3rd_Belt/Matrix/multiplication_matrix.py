# Question: How to multiply two matrices in Python without using NumPy or functions?

# Define matrix A (2 rows x 3 columns)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Define matrix B (3 rows x 2 columns)
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Get the dimensions of the matrices
rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

# Check if multiplication is possible (columns of A must match rows of B)
if cols_A != rows_B:
    print("Matrix multiplication not possible. Columns of A must match rows of B.")
else:
    # Initialize the result matrix with zeros (rows_A x cols_B)
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication using three nested for loops
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    # Print the resulting matrix
    print("Result of Matrix Multiplication:")
    for row in result:
        print(row)
