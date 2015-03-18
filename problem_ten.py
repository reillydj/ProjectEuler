__author__ = "David Reilly"

"""
    Project Euler
    Problem: 10

    'The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.'
"""

import math

def quicker_is_prime(integer):

    if integer == 2:
        return True

    for candidate in xrange(2, int(math.ceil(integer ** 0.5)) + 1):

        if integer % float(candidate) == 0:
            return False

    return True

def generate_primes(upper_bound, prime_checker):

    candidate = 2
    while candidate < upper_bound:
        if prime_checker(candidate):
            print candidate
            yield candidate
        candidate += 1

def sum_primes(upper_bound, prime_checker):

    return sum(generate_primes(upper_bound, prime_checker))

if __name__ == '__main__':

    sumz = sum_primes(2000000, quicker_is_prime)
    print sumz