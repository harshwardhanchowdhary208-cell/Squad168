# Challenge #6
# Develop a program that determines whether a given string can be 
# transformed into a palindrome by rotating it. A palindrome is a 
# string that reads the same forward and backward, such as "radar" or "level". 
# Rotation involves moving characters from one end of the string to the 
# other without changing their order otherwise. For example, rotating 
# "abcde" once to the right gives "eabcd".
#
# Input format:
# - A single line of input containing the string s. The string will consist 
#   of lowercase and/or uppercase letters and/or digits, with a length of 
#   at least 1 character and not exceeding 10,000 characters.
#
# Output format:
# - The program should output "Yes, the rotated string is a palindrome." 
#   if there exists a rotation of the input string such that it forms a palindrome.
# - Otherwise, the program should output "No, the rotated string is not a palindrome."

import sys
from collections import Counter

def main():
    # Read the input string
    s = sys.stdin.read().strip()
    if not s:
        return

    # Fact: A palindrome can have at most one character with an odd frequency.
    # Since rotation doesn't change character counts, any valid string must satisfy this.
    char_counts = Counter(s)
    odd_counts = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    if odd_counts > 1:
        print("No, the rotated string is not a palindrome.")
        return

    n = len(s)
    double_s = s + s
    
    # Check all possible rotations of length n
    for i in range(n):
        rotation = double_s[i:i+n]
        if rotation == rotation[::-1]:
            print("Yes, the rotated string is a palindrome.")
            return

    print("No, the rotated string is not a palindrome.")

if __name__ == "__main__":
    main()
