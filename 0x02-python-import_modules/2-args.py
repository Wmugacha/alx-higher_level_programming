#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    count = len(sys.argv) - 1
    if (count == 0):
        print("0 arguements.")
    elif (count == 1):
        print("1 arguement:")
    else:
        print("{} arguements:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
