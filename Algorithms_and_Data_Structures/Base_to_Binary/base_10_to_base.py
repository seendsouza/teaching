from collections import deque
import sys

"""
         answer remainder
12 / 2 = 6      0
6 / 2  = 3      0
3 / 2  = 1      1
1 / 2  = 0      1
Reverse stack
1100

Works for numbers >= 0
"""

def base_10_to_binary(base, base_10):
    stack = deque()
    while base_10 != 0:
        bin_char = base_10 % base 
        stack.append(bin_char)
        base_10 = (base_10 - bin_char) / base
    if len(stack) == 0:
        stack.append(0)
    return stack

def stack_to_str(stack):
    string = str()
    while not len(stack) == 0:
        string += str(int(stack.pop()))
    return string

if __name__ == "__main__":
    base, base_10 = input().split()
    stack = base_10_to_binary(int(base), int(base_10))
    print(stack_to_str(stack))
