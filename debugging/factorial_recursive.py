#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Function description:
        This function computes the factorial of a given
        non-negative integer using recursion.

    Parameters:
        n (int): The number for which the factorial is calculated.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of n. If n == 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
