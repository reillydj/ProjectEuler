__author__ = 'David Reilly'

import time

def yield_multiples(multiple, upper_bound):

    index = multiple

    while index < upper_bound:

        yield index
        index += multiple

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
