#!/usr/bin/python3
alphabet = [chr(num) for num in range(97, 123) if num!=113 and num!=101]
print(''.join(alphabet), end="")
