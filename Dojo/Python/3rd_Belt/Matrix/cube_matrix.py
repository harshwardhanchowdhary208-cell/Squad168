# Problem Statement:
# Given an M x N matrix, print the squares of all elements row by row, 
# followed by the cubes of all elements row by row.
#
# Example 1:
# Input:
# 2 2
# 1 2
# 3 4
# Output:
# 1 4
# 9 16
# 1 8
# 27 64

def process_matrix(m, n, matrix):
    # Print the square of each element row by row
    for row in matrix:
        squares = [str(x ** 2) for x in row]
        print(" ".join(squares))
        
    # Print the cube of each element row by row
    for row in matrix:
        cubes = [str(x ** 3) for x in row]
        print(" ".join(cubes))

# Read input
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
process_matrix(m, n, matrix)
