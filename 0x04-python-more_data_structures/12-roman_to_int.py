def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = []
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_numerals.get(char, 0)

        if value < prev_value:
            result.append(-value)
        else:
            result.append(value)

        prev_value = value

    return sum(result)
