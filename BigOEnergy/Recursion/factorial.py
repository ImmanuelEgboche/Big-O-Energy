# Recursive implementation of n! (n-factorial) calculation

def factorial(n):
    # Base case: n= 0 or n = 1
    if n <= 1:
        return 1
    
    return n * factorial(n-1)