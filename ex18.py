"""
This one is like the script with argv, this is like argv parameter but for functions.
This `*args` tells python to take all arguments to the function and then put them in args as a list.
It's not normally used too often unless specifically needed.
"""
def print_two(*argss):
    arg1, arg2 = argss
    print(f"arg1 : {arg1}, arg2 : {arg2}")

# Ok, that's *args is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
    print(f"arg1 : {arg1}, arg2 : {arg2}")

# This just takes one argument.
def print_one(arg1):
   print(f"arg1 : {arg1}")

# This one takes no arguments.
def print_none():
    print("I got nothing")
    
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


"""
Functions do three things:
* They name pieces of code the way variables name string and number.
* They take arguments the way your script take argv.
* Using 1 and 2, they let you make your own "mini-scripts" or "tiny-commands".
"""
