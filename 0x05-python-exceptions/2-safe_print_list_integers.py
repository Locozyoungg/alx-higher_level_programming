#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers
    """
    count = 0
    for i in range(x):
        try:
            value = my_list[i]
            print("{:d}".format(value), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
