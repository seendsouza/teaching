"""
A collection of loops for practice
"""

# For Loops

print("For Loops")

# Prints each letter in the string "banana"
for x in "banana":
  print(x)

# Prints each member of the list (fruits)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Prints each member of the list until "banana" is printed
# It then breaks out of the loop, so "cherry" is not printed
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Since numbers start at 0, prints 0 to (6-1) or 0 to 5 (number of numbers printed is 6)
for x in range(6):
    print(x)

# Prints 2 to 5
for x in range(2, 6):
  print(x)

# Prints 2 to 30 and increments by 3 each time instead of 1
for x in range(2, 30, 3):
  print(x)

# When done, it will print "Finally finished!"
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Adjective and fruit list
adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# For every adjective, it prints every fruit in the list above after it
for x in adjective:
  for y in fruits:
    print(x, y) 

# While Loops

print("\n\nWhile Loops")

true_variable = True

# These are infinite loops because true_variable is always true (until you set it to be false)
# Infinite loops are usually bad because they run forever
# If they store data (not like this one) in memory or on drive, this will be infinitely adding data to the computer (which could lead to RAM overflow or running out of disk space)
"""
while true_variable == True:
    print("I'm in an infinite loop")

while true_variable:
    print("I'm in an infinite loop again")
"""

x = -5
while x < 0:
    x+=1
    print("I'm incrementing by 1 and I'm at {}".format(x))

# Recursion

print("\n\nRecursion")

# Uses itself 
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

tri_recursion(6)
# Explanation with 6 as an example:
# k = 6
# k > 0, so result is 6 + 5 + 4 + 3 + 2 + 1 + 0 = 21
# That is the last result, but what about the previous results?
# Remember that recursion uses itself, so everytime it calls itself, it needs to execute the whole function
# The result is only when k is 1 because when k = 0, k !> 0 and therefore the function does not print anything, but returns the result as 0 (because of the else statement)
# I like to think of it as going backwards from there, so result = 1 + 0 = 1 and it is printed and returned
# Then you have the next k, which is 2, so 2 + 1 = 3
# Then you have the next k, which is 3, so 3 + 3 = 6
# Then you have the next k, which is 4, so 4 + 6 = 10
# Then you have the next k, which is 5, so 5 + 10 = 15
# Then you have the next k, which is 6, so 6 + 15 = 21
# It prints the numbers: 1, 3, 6, 10, 15, 21 as a result

