# Lab 1

import time

# Define a python function that will print the first 100 factorial numbers 1!, 2!, ...., 100!
# Using recursion:
def print_factorial_recursion(n):
    # Check boundary conditions.
    if (n < 0):
        return -1
    
    if n == 0:
        print(1)
        return 1
    else:
        result = n*(print_factorial_recursion(n-1))
        print(result)
        return result

# Define a python function that will print the first 100 factorial numbers 1!, 2!, ...., 100!
# Using iteration (optimized):
def print_factorial_iteration(n):
    # Check boundary conditions.
    if (n < 0):
        return -1

    result = 1
    for i in range(1, n+1):
        result*=i
        print(result)
    return result

# Find out the maximum number possible on your system. Provide reasons.
# When recursion is used -> 997 (RecursionError: maximum recursion depth exceeded in comparison).
def print_max_factorial_recursion():
    n = 0

    while True:
        print_factorial_recursion(n)
        print(n)
        n += 1

# Find out the maximum number possible on your system. Provide reasons.
# When iteration is used -> maximum number is very large or does not exist.
def print_max_factorial_iteration():
    num = 1

    while True:
        print_factorial_iteration(num)
        print(num)
        num += 1

# t1 = time.time()
# print_factorial_recursion(100)
# t2 = time.time()
# print(t2-t1)

# t3 = time.time()
# print_factorial_iteration(100)
# t4 = time.time()
# print(t4-t3)

# print_max_factorial_recursion()
# print_max_factorial_iteration()
