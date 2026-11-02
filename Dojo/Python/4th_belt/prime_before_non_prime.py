# Challenge #9
# You are given an array of integers. Your task is to rearrange the array such that 
# all prime numbers appear at the beginning and all non-prime numbers appear at the end, 
# while preserving their original order.
#
# Input Format:
# - The first line contains an integer N representing the number of elements in the array.
# - The second line contains N space-separated integers representing the array elements.
#
# Output Format:
# - Print the rearranged array where all prime numbers appear first, 
#   followed by non-prime numbers, while maintaining their original order.

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

N = int(input())
arr = list(map(int, input().split()))

# Separate the numbers into primes and non-primes to preserve relative order
primes = [x for x in arr if is_prime(x)]
non_primes = [x for x in arr if not is_prime(x)]

# Combine both lists and print the result as space-separated integers
result = primes + non_primes
print(*(result))
