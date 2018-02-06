import numpy as np

import numba
from numba import jit

@jit
def largestPrime(n):
    i = 2
    while i * i <= n:
        while n%i == 0:
            n = n / i
        i += 1
    return n

@jit
def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    # Print all prime numbers
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes

@jit
def factors(n):
    return np.asarray([x for x in range(2, n//2+1) if n%x == 0])

@jit
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

@jit
def lcm(x, y):
    lcm = (x * y) / gcd(x,y)
    return lcm

@jit
def check_palindrome(x):
    truth = False
    x = str(x)
    l = len(x)
    if l == 2:
        if x[0] == x[1]:
            return True
        else:
            return False
    if l == 1:
        return True

    if x[0] == x[-1] and l > 2:
        return check_palindrome(x[1:-1])



