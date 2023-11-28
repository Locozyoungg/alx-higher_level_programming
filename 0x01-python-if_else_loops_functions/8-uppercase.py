#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()  # Print a new line after the loop

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
