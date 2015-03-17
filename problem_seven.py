__author__ = "David Reilly"

"""
    Project Euler
    Problem: 7

    'By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?'
"""
import math

def is_prime(integer):

    if integer == 2:
        return True
    for candidate in xrange(2, int(math.ceil(integer ** 0.5)) + 1):

        if integer % float(candidate) == 0:
            return False

    return True

def generate_primes(nth_prime):

    index = 1
    number = 2
    while index <= nth_prime:
        print number, is_prime(number), index
        if is_prime(number):
            index += 1
            number += 1
        else:
            number += 1

    return number

if __name__ == "__main__":

    prime = generate_primes(10001)
    print prime
