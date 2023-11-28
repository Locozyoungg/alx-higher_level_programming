#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number with correct sign
last_digit = number % 10 if number >= 0 else -(-number % 10)

# Determine the relationship with 5 and 0
if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"

# Print the output
print("Last digit of {} is {} {}".format(number, last_digit, result))
