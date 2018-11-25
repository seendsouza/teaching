"""
For a number between 1 and 20,
if the number is divisible by 3, set the string to Fizz
and if it is divisible by 5 add Buzz to the string
if it isn't factorable by 3 or 5, the string becomes the number
print the current string
"""
for num in range(1, 21):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)
