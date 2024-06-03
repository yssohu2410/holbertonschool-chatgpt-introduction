#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer n recursively.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given integer n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)

