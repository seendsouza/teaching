"""
Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."""
def concat_strings(num):
    """
    
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
    """
    for num in range(1,21):
        print(concat_strings(num))
        print(if_elif_else(num))

if __name__ == "__main__":
    Main()
