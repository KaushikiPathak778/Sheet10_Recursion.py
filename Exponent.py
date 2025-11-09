# Problem:
# Write a recursive function to find x raised to the power n.
# Input Format:
# Two integers x and n are separated by a space.
# Output Format:
# Print the value of xⁿ.
# Sample Input:
# 2 5
# Sample Output:
# 32

def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)
x,n=map(int,input().split())
print(power(x,n))