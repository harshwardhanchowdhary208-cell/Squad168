# Challenge #8
# You are given an array of integers and an integer K. Your task is to find all elements whose frequency of occurrence is exactly K.
# 
# Print each qualifying element exactly once, in the order of its first occurrence in the array.
# 
# If no such element exists, print -1.
# 
# Use a hash map (frequency map) to count the occurrences of each element efficiently.
# 
# Input Format:
# - The first line contains an integer N representing the number of elements in the array.
# - The second line contains N space-separated integers representing the array elements.
# - The third line contains an integer K representing the required frequency.

import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    k = int(data[1 + n])
    
    # Step 1: Create a frequency map (hash map) to count occurrences
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
        
    # Step 2: Find qualifying elements in the order of their first occurrence
    result = []
    seen = set()
    
    for num in arr:
        if num not in seen:
            seen.add(num)
            if freq_map[num] == k:
                result.append(num)
                
    # Step 3: Print results or -1 if no elements match the condition
    if result:
        print(*(result))
    else:
        print(-1)

if __name__ == "__main__":
    main()
