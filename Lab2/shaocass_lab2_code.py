# Lab 2

import random
import time

# Define a python function newton_raphson() to compute square root of 12345.
# You may use 100 (or another number of your choice for convergence) as initial guess x_0.
# x_(n+1) = x_n - (f(x_n)/f'(x_n))
# f(x) = x^2 ; f'(x) = 2x
def newton_raphson(n):
    x_0 = 100
    root = x_0 - (((x_0*x_0)-n)/(2*x_0))

    while (abs(root-x_0) >= 0.5):
        x_0 = root
        root = x_0 - (((x_0*x_0)-n)/(2*x_0))

    return root

# Now define a randomized version which will make a random guess of the initial approximation.
def newton_raphson_randomized(n):
    x_0 = random.uniform(1, n)
    root = x_0 - (((x_0*x_0)-n)/(2*x_0))

    while (abs(root-x_0) >= 0.5):
        x_0 = root
        root = x_0 - (((x_0*x_0)-n)/(2*x_0))

    return root

# Compare accuracy and runtime performance.
t1 = time.time()
print(newton_raphson(12345))
t2 = time.time()
print(t2-t1)

t3 = time.time()
print(newton_raphson_randomized(12345))
t4 = time.time()
print(t4-t3)
