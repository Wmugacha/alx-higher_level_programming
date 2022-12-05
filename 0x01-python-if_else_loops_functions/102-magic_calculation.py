#!/usr/bin/python3
import dis
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        print(a + b)
        print(a * b -c)
dis.dis(magic_calculation)
