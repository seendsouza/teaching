# For a number from 1 to 20, if the remainder of the number divided by 3 and 5 is 0, print FizzBuzz.
# if it's just a remainder of the number divided by 3, print Fizz
# if it's just a remainder of the number divided by 5, print Buzz
# if it's any other number, print the number
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
