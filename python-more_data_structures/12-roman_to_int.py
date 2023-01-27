#!/usr/bin/python3
def roman_to_int(roman_string):
    romanum_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string) - 1):
        if romanum_dict[roman_string[i]] < romanum_dict[roman_string[i + 1]]:
            romanum_dict[roman_string[i]] = -romanum_dict[roman_string[i]]
    return sum(romanum_dict[i] for i in roman_string)
