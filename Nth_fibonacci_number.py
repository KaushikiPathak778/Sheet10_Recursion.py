# Problem:
# Write a recursive function to find the Nth Fibonacci number.
# Input Format:
# A single integer N.
# Output Format:
# Print the Nth Fibonacci number.

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
N=int(input())
print(fib(N))