"""
DISCLAIMER: DO NOT DO FIZZBUZZ THIS WAY
THIS IS ONLY FOR TEACHING PURPOSES
"""
from fizzbuzz import if_elif_else, concat_strings

def check_integer(min_counter, max_counter, increment_value, num_1, num_2):
    """
    Check to see if the integer input parameters of the main function are integers or not
    """
    if type(min_counter) is int and type(max_counter) is int and type(increment_value) is int:
        return True
    else:
        return False

def check_method(method):
    """
    Check if the method paramter in the main function is valid.

    Keyword Arguments:
    """
    if method == "concatstrings" or method == "ifelifelse":
        return True
    else:
        return False


def print_fizzbuzz(value, method):
    """
    Print either fizz, buzz, fizzbuzz, or the value using the chosen method
    """
    if method == "ifelifelse":
        if_elif_else(value)
    else:
        concat_strings(value)

def Main(min_counter, max_counter, increment_value, num_1, num_2, method):
    """
    Check for some numbers

    Keyword Arguments:
    min_counter --
    max_counter --
    increment_value --
    num_1 --
    num_2 --
    method -- the way FizzBuzz is done
    """
    if not check_integer(min_counter, max_counter, increment_value, num_1, num_2):
        print("The input parameters are not integers.")
    elif not check_method:
        print("Invalid method name.")
    elif max_counter < min_counter:
        print("Your maximum counter is smaller than your minimum counter.")
    else:
        counter = min_counter
        while counter < max_counter:
            print_fizzbuzz(counter, method, num_1, num_2)
            counter += increment_value

if __name__ == "__main__":
    # Valid
    Main(1, 21, 1,3,5,"ifelifelse")
    # Invalid
    # Main()

