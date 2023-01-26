#!/usr/bin/python3
def roman_to_int(roman_string):
    romanum_dict = {'I': "1", 'V': "5", 'X': "10", 'L': "50", 'C': "100", 'D': "500", 'M': "1000"}
    numers = {i: int(j) for i, j in romanum_dict.items()}
    return sum(numers[i] for i in roman_string)
