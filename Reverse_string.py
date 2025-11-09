# Reverse a string using recursion
# Problem:
# Write a recursive function to reverse a string.
# Input Format:
# A single string S.
# Output Format:
# Print the reversed string.
# Sample Input:
# hello
# Sample Output:
# olleh

def reverse_string(s):
    if len(s)<=1:
        return s
    return reverse_string(s[1:])+s[0]
S=input()
print(reverse_string(S))