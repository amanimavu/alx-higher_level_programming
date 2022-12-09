#!/usr/bin/python3

'''
    This program maps roman numerals to their
    equivalent arabic numerals
    It work by splitting the string containing the
    roman number into the "building blocks" of the
    number
    Using dictionaries to find the equivalent
    arabic number value

    For example:
    roman_string = "XXXIX"
    arabic_number = roman_to_int(roman_string)
    print(arabic_number)
    >>>> 39
'''


def roman_to_int(roman_string):
    special = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    numeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result, i = 0, 0
    while i < len(roman_string):
        if i <= len(roman_string) - 2:
            if (roman_string[i] + roman_string[i+1]) in special:
                result += special[roman_string[i] + roman_string[i+1]]
                i += 2
                continue
        result += numeral[roman_string[i]]
        i += 1

    return result
