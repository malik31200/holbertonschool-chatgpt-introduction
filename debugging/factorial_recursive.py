#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number recursively.

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

if __name__ == "__main__":
    # Vérifie qu'un argument est passé
    if len(sys.argv) < 2:
        print("Usage: ./factorial_recursive.py <number>")
        sys.exit(1)

    # Convertit l’argument en entier et calcule le factoriel
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Erreur: le factoriel n’est pas défini pour les nombres négatifs.")
            sys.exit(1)
        f = factorial(num)
        print(f)
    except ValueError:
        print("Erreur: l’argument doit être un entier.")
