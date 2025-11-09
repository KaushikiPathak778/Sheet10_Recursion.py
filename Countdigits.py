# Problem:
# Write a recursive function to count the digits in a number.
# Input Format:
# A single integer N.
# Output Format:
# Print the number of digits.

def count_digits(n):
    if n==0:
        return 0
    return 1+count_digits(n//10)
N=int(input())
if N==0:
    print(1)
else:
    print(count_digits(abs(N)))  