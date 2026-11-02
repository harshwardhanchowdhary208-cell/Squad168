# Challenge #7: Find the first repeating element in the array.
#
# You are given an array of integers. Your task is to find the first repeating element in the array.
# An element is considered repeating if it appears more than once, and the first repeating element 
# is the one whose first occurrence appears earliest in the array.
#
# Input Format:
# - The first line contains an integer N (1 <= N <= 1000), representing the number of elements in the array.
# - The second line contains N space-separated integers representing the array elements.
#
# Output Format:
# - Print the first repeating element in the array.
# - If no repeating element exists, print -1.

def find_first_repeating():
    # Read input values
    N = int(input())
    arr = list(map(int, input().split()))
    
    # Step 1: Count the frequency of each element
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
        
    # Step 2: Find the first element from left to right that appears more than once
    for num in arr:
        if frequency[num] > 1:
            print(num)
            return
            
    # If no repeating element is found, print -1
    print(-1)

if __name__ == "__main__":
    find_first_repeating()
