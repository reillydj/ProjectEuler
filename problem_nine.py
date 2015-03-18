__author__ = "David Reilly"

"""
    Project Euler
    Problem: 9

    'A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.'

"""
import numpy as np

def pythagorean_grid_search():

    for a in range(1, 1000):
        for b in range(1, a):
            if np.sqrt(a ** 2 + b ** 2).is_integer():
                if a + b + np.sqrt(a ** 2 + b ** 2) == 1000:
                    return a * b * np.sqrt(a ** 2 + b ** 2)

if __name__ == "__main__":

    triple = pythagorean_grid_search()
    print triple