#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    add = add(a, b)
    sub = sub(a, b)
    mul = mul(a, b)
    div = div(a, b)
    print(f"{a} + {b} = {add}")
    print(f"{a} - {b} = {sub}")
    print(f"{a} * {b} = {mul}")
    print(f"{a} / {b} = {div}")
