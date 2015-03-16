__author__ = "David Reilly"

"""
    Project Euler
    Problem: 3

    'The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?'

"""

def is_prime(integer):

    candidates = [integer % float(x) for x in xrange(2, int(math.ceil(integer ** 0.5)))]

    return 0 not in candidates

def generate_primes(upper_bound):

    candidate = 1
    while candidate < (upper_bound ** 0.5):
        if is_prime(candidate) and upper_bound % candidate == 0:
            yield candidate
        candidate += 1

def maximum_prime(upper_bound):

    return list(generate_primes(upper_bound))

if __name__ == "__main__":

    print maximum_prime(600851475143)

