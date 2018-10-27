"""
Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."""
def concat_strings(num):
    """
    See fizzbuzz_concat_strings.py for an explanation.
    """
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    return(string)

def if_elif_else(num):
    """
    See fizzbuzz_if_elif_else.py for an explanation.
    """
    if num % 3 == 0 and num % 5 == 0:
        return('FizzBuzz')
    elif num % 3 == 0:
            return('Fizz')
    elif num % 5 == 0:
        return('Buzz')
    else:
        return(num)
def Main():
    """
    The main function for running FizzBuzz
    """
    for num in range(1,21):
        print(concat_strings(num))
        print(if_elif_else(num))

# This just means that it will only execute when you run this program. It will not run if imported into another program, but the previous functions will be improted..
if __name__ == "__main__":
    Main()
