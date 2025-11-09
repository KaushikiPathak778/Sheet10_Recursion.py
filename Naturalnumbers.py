# Print numbers from 1 to N
# Problem:
# Using recursion, print numbers from 1 to N.
# Input Format:
# A single integer N.
# Output Format:
# Print numbers from 1 to N separated by a space.

def print_numbers(n):
    if n==0:
        return
    print_numbers(n-1)
    print(n,end=' ')
N=int(input())
print_numbers(N)