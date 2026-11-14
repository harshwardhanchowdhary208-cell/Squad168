s = input().strip()

palindromes = []
n = len(s)

# Generate all possible substrings
for i in range(n):
    for j in range(i + 1, n + 1):
        sub = s[i:j]
        # Check if the substring reads the same backward
        if sub == sub[::-1]:
            palindromes.append(sub)

# Print all palindromic substrings separated by spaces
print(" ".join(palindromes))

# Print the total count on the next line
print(len(palindromes))
