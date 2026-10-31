def diagonal_sum(matrix):
    n = len(matrix)
    total_sum = 0
    
    for i in range(n):
        # Add primary diagonal element
        total_sum += matrix[i][i]
        
        # Add secondary diagonal element only if it's not the center element
        if i != n - 1 - i:
            total_sum += matrix[i][n - 1 - i]
            
    return total_sum

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(diagonal_sum(matrix))  
# Output: 25 (1+5+9 + 3+7 -> 5 is only counted once)
