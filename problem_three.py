__author__ = "David Reilly"

"""
    Project Euler
    Problem: 3

    'The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?'

"""

import math
import time

def is_prime(integer):

    candidates = [integer % float(x) for x in xrange(2, int(math.ceil(integer ** 0.5)))]

    return 0 not in candidates

def quicker_is_prime(integer):

    for candidate in xrange(2, int(math.ceil(integer ** 0.5))):

        if integer % float(candidate) == 0:
            return False

    return True

def generate_primes(upper_bound, prime_checker):

    candidate = 1
    while candidate < (upper_bound ** 0.5):
        if prime_checker(candidate) and upper_bound % candidate == 0:
            yield candidate
        candidate += 1

def maximum_prime(upper_bound, prime_checker):

    return list(generate_primes(upper_bound, prime_checker))

if __name__ == "__main__":


    ## Solution using quicker prime_checker
    start_time = time.time()
    print maximum_prime(600851475143, is_prime)
    print "Slow is_prime Solution Took ", time.time() - start_time, " Seconds"

    ## Solution using slower prime_checker
    start_time = time.time()
    print maximum_prime(600851475143, quicker_is_prime)
    print "quicker_is_prime Solution Took ", time.time() - start_time, " Seconds"


