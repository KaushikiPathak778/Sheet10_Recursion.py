# Problem:
# Find the sum of the digits of a given number using recursion.
# Input Format:
# A single integer N.
# Output Format:
# Print the sum of its digits.
# Sample Input:
# 1234
# Sample Output:
# 10

def sum_of_digits(n):
    if n==0:
        return 0
    return n%10+sum_of_digits(n//10)
N=int(input())
print(sum_of_digits(N))