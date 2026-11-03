# Question: Check if two matrices are equal.
# Two matrices are equal if they have the same dimensions and every corresponding element is identical.


def read_matrix():
    m, n = map(int, input().split())
    matrix = []

    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix, m, n


matrix1, m1, n1 = read_matrix()
matrix2, m2, n2 = read_matrix()

if m1 != m2 or n1 != n2:
    print("Not Equal")
else:
    # Compare the nested lists directly to check element-by-element equality
    if matrix1 == matrix2:
        print("Equal")
    else:
        print("Not Equal")
