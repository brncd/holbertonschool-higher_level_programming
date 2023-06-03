#!/usr/bin/python3
def print_last_digit(number):
    last_digit = (abs(number) % 10) * -1 if number < 0 else abs(number) % 10
    print(last_digit)
    return last_digit
