# Problem:
# Write a recursive function to find the factorial of a number.
# Input Format:
# A single integer N.
# Output Format:
# Print the factorial of N.
# Sample Input:
# 5
# Sample Output:
# 120

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
N=int(input())
print(fact(N))