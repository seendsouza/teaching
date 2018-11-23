"""
Write a program that prints the ibers from 1 to 20. But for multiples of three print “Fizz” instead of the iber and for the multiples of five print “Buzz”. For ibers which are multiples of both three and five print “FizzBuzz”."""
def concat_strings(i,num_1,num_2):
    """
    See fizzbuzz_concat_strings.py for an explanation.
    """
    string = ""
    if i % num_1 == 0:
        string = string + "Fizz"
    if i % num_2 == 0:
        string = string + "Buzz"
    if i % num_1 != 0 and i % num_2 != 0:
        string = string + str(i)
    return(string)

def if_elif_else(i,num_1,num_2):
    """
    See fizzbuzz_if_elif_else.py for an explanation.
    """
    if i % num_1 == 0 and i % num_2 == 0:
        return('FizzBuzz')
    elif i % num_1 == 0:
            return('Fizz')
    elif i % num_2 == 0:
        return('Buzz')
    else:
        return(i)
def Main():
    """
    The main function for running FizzBuzz
    """
    for i in range(1,21):
        print(concat_strings(i))
        print(if_elif_else(i))

# This just means that it will only execute when you run this program. It will not run if imported into another program, but the previous functions will be improted..
if __name__ == "__main__":
    Main()
