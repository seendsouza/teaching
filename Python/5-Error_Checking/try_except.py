# x = 1
try:
    print(x)
except SyntaxError:
    print("there was an error")
except NameError as e:
    print("make a variable called x." + str(e))
