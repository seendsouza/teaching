"""
A collection of loops for practice
"""

# For Loops

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



# Recursion

# 
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
