# Print numbers from N to 1
# Problem:
# Using recursion, print numbers from N to 1.
# Input Format:
# A single integer N.
# Output Format:
# Print numbers from N to 1 separated by a space.

def print_reverse(n):
    if n==0:
        return
    print(n,end=' ')
    print_reverse(n-1)
N=int(input())
print_reverse(N)