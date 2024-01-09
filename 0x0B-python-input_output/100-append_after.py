#!/usr/bin/python3
"""
100-append_after
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for.
        new_string (str): The line of text to insert after each occurrence of the search string.
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()

if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

