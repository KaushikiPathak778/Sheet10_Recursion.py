# Problem:
# Using recursion, check whether a string is a palindrome or not.
# Input Format:
# A single string S.
# Output Format:
# Print "Palindrome" if the string is a palindrome, otherwise "Not Palindrome".
# Sample Input:
# madam
# Sample Output:
# Palindrome

def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])
S=input()
if is_palindrome(S):
    print("Palindrome")
else:
    print("Not Palindrome")