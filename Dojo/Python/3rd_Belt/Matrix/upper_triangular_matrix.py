rows = int(input())

a = True

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(rows):
    for j in range(rows):
        if i > j and matrix[i][j] != 0:
            a = False
            break

if a:
    print("Yes")
else:
    print("No")
