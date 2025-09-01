#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Args:
        n (int): The number for which the factorial is calculated.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of n. If n == 0, returns 1.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    # Check that an argument was provided
    if len(sys.argv) < 2:
        print("Usage: ./factorial_recursive.py <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: factorial is not defined for negative numbers.")
            sys.exit(1)
        result = factorial(num)
        print(result)
    except ValueError:
        print("Error: argument must be an integer.")
