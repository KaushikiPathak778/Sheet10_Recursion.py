# Sum of first N natural numbers
# Problem:
# Write a recursive function to find the sum of the first N natural numbers.
# Input Format:
# A single integer N.
# Output Format:
# Print the sum of the first N natural numbers.

def recursive_sum(n):
    if n==1:
        return 1
    else:
        return n+recursive_sum(n-1)
N=int(input())
print(recursive_sum(N)) 
 