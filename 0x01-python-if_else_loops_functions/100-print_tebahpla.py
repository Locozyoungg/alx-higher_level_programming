#!/usr/bin/python3

for i in range(ord('z'), ord('A') - 1, -1):
    print("{:c}".format(i) if i % 2 == 0 else "{:c}".format(i - 32), end="")
