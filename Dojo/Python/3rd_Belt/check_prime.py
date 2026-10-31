# Question: Count of only prime elements in an array.
# Note: '0' and '1' are not prime.
# Input format: The first line will contain an array of size 6, consisting of integers arr[i].
# Output format: Print a single integer, which is the count of prime numbers in the array.
# Constraints: 0 <= arr[i] <= 10^6

a = list(map(int, input().split()))
d = 0

for i in a:
    if i < 2:
        continue  # 0 and 1 are not prime, skip them
    
    is_prime = True
    c = 2
    # Efficiently check for factors up to the square root of i
    while c * c <= i:
        if i % c == 0:
            is_prime = False
            break
        c += 1
        
    if is_prime:
        d += 1

print(d)
