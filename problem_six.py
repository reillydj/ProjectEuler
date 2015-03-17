__author__ = "David Reilly"

"""
    Project Euler
    Problem: 6

    'The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.'
"""

import numpy as np

def sum_of_squares():

    ## Use numpy to vectorize operations
    numbers = np.arange(1, 101)

    square_of_sum = np.sum(numbers) ** 2
    numbers **= 2
    sum_of_square = np.sum(numbers)

    return square_of_sum - sum_of_square

if __name__ == "__main__":

    answer = sum_of_squares()
    print answer