#!/usr/bin/python3
def roman_to_int(roman_string):
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) is not str:
        return 0
    sum = 0
    for i in range(len(roman_string)):
        if i > 0 and r_dict[roman_string[i]] > r_dict[roman_string[i - 1]]:
            sum += r_dict[roman_string[i]] - 2 * r_dict[roman_string[i - 1]]
        else:
            sum += r_dict[roman_string[i]]
    return sum