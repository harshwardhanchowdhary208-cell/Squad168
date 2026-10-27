word = "CODE"
rows = 3
cols = 10

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1:
            print("*", end=" ")
        elif j == 0 or j == cols - 1:
            print("*", end=" ")
        elif 3 <= j <= 6:
            print(word[j - 3], end=" ")
        else:
            print(" ", end=" ")
    print()