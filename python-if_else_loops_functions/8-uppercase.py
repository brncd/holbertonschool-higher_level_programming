def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print(upper_char, end="")
    print("")
