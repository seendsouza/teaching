"""
DISCLAIMER: DO NOT DO FIZZBUZZ THIS WAY
THIS IS ONLY FOR TEACHING PURPOSES
"""
from fizzbuzz import if_elif_else, concat_strings

def check_integer(min_counter, max_counter, increment_value, fizz_num, buzz_num):
    """
    Check to see if the integer input parameters of the main function are integers or not
    """
    if type(min_counter) is int and type(max_counter) is int and type(increment_value) is int:
        return True
    else:
        return False

def check_method(method):
    """
    Check if the method paramater in the main function is valid.

    Keyword Arguments:
    """
    if method == "concatstrings" or method == "ifelifelse":
        return True
    else:
        return False


def print_fizzbuzz(value, method,fizz_num,buzz_num):
    """
    Print either fizz, buzz, fizzbuzz, or the value using the chosen method
    """
    if method == "ifelifelse":
        print(if_elif_else(value,fizz_num,buzz_num))
    else:
        print(concat_strings(value,fizz_num,buzz_num))

def Main(min_counter, max_counter, increment_value, fizz_num, buzz_num, method):
    """
    Check for some numbers

    Keyword Arguments:
    min_counter -- the initial value of the counter
    max_counter -- the maximum value of the counter, before it exits the loop (n-1)
    increment_value -- the value of the counter
    fizz_num -- the number where it prints Fizz when the remainder is 0
    buzz_num -- the number where it prints Buzz when the remainder is 0
    method -- the way FizzBuzz is done
    """
    if not check_integer(min_counter, max_counter, increment_value, fizz_num, buzz_num):
        print("The input parameters are not integers.")
    elif not check_method:
        print("Invalid method name.")
    elif max_counter < min_counter:
        print("Your maximum counter is smaller than your minimum counter.")
    else:
        counter = min_counter
        while counter < max_counter:
            print_fizzbuzz(counter, method, fizz_num, buzz_num)
            counter += increment_value

if __name__ == "__main__":
    #Main(1, 21, 1,3,5,"ifelifelse")
    Main(1,21,1,3,5,"concatstrings")
