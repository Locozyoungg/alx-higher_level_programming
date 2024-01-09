#!/usr/bin/python3
"""
101-stats
"""

import sys

def print_stats(total_size, status_codes):
    """
    Prints the statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing status codes and their counts.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """
    Parses a line and extracts file size and status code.

    Args:
        line (str): Input line.

    Returns:
        tuple: A tuple containing file size (int) and status code (str).
    """
    elements = line.split()
    return int(elements[-1]), elements[-2]

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            size, status = parse_line(line)
            total_size += size
            if status in status_codes:
                status_codes[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

