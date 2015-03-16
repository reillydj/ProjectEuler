__author__ = 'David Reilly'

import time

"""
    Project Euler
    Problem: 1

    'If we list all the natural numbers below 10 that are multiples of 3 or 5,
        we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.'

    sum_multiples_generator() solves this using a generator function to reduce space complexity

    sum_multiples_list_comprehension() solves this using a list comprehension

    sum_multiples_generator() is approx. 7x faster than sum_multiples_list_comprehension()
"""

## Generator to be used in sum_multiples_generator()
def yield_multiples(multiple, upper_bound):

    index = multiple

    while index < upper_bound:

        yield index
        index += multiple

## Use a generator function to reduce space complexity
def sum_multiples_generator(list_of_multiples, upper_bound):

    all_multiples = [list(yield_multiples(x, upper_bound)) for x in list_of_multiples]
    flattened = reduce(lambda x, y: x + y, all_multiples)
    uniques = set(flattened)
    sum_of_multiples = sum(uniques)

    return sum_of_multiples

def sum_multiples_list_comprehension(list_of_multiples, upper_bound):

    return sum([x for x in range(upper_bound) if (0 in [x % y for y in list_of_multiples])])

if __name__ == '__main__':

    ## Solution using generator function (Faster Solution)
    start_time = time.time()
    sums_one = sum_multiples_generator([3, 5], 10000000)
    print "Generator Solution Took ", time.time() - start_time, " Seconds"
    print sums_one

    ## Solution using List Comprehension
    start_time = time.time()
    sums_two = sum_multiples_list_comprehension([3, 5], 10000000)
    print "List Comprehension Solution Took ", time.time() - start_time, " Seconds"
    print sums_two
