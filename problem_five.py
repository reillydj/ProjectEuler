__author__ = "David Reilly"

"""
    Project Euler
    Problem: 5

    '2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'
"""

def is_divisible(numerator, denominator):

    return numerator % denominator == 0

def check_candidates():

    candidate = 2520

    while 1:
        answer = True
        for i in range(2, 21):
            if not is_divisible(candidate, i):
                ## Candidate must be at least divisible by 10, therefore, increment by 10
                candidate += 10
                answer = False
                break
        if answer:
            return candidate

if __name__ == "__main__":

    candidate = check_candidates()

    print candidate