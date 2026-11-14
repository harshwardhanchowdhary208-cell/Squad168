N = int(input())
arr = list(map(int, input().split()))

# Store elements in a set for O(1) lookup time
num_set = set(arr)

# Start checking from the smallest positive integer, 1
smallest_missing = 1
while smallest_missing in num_set:
    smallest_missing += 1

print(smallest_missing)
