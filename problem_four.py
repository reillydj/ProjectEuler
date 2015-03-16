__author__ = "David Reilly"

"""
    Project Euler
    Problem: 4

    'A palindromic number reads the same both ways.

    The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3 digit numbers.'
"""

def is_palindrome(integer):

    string_rep = str(integer)
    list_of_strings = list(string_rep)

    return "".join(reversed(list_of_strings)) == string_rep

def generate_products():

    set_of_products = set()

    for left in xrange(100, 1000):
        for right in xrange(100, 1000):
            if left * right in set_of_products:
                continue
            set_of_products.add(left * right)
            yield left * right, left, right

def find_palindromes():

    palindromes = list(candidate for candidate in generate_products() if is_palindrome(candidate[0]))

    return max(palindromes)

if __name__ == "__main__":

    print is_palindrome(10101)

    print find_palindromes()