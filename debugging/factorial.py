#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # décrémentation nécessaire
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Erreur : le factoriel n’est pas défini pour les nombres négatifs.")
            sys.exit(1)
        f = factorial(num)
        print(f)
    except ValueError:
        print("Erreur : l’argument doit être un entier.")
