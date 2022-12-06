#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    """program that prints the result of the addition of all arguments"""

    total = 0

    for i in range(len(sys.argv) -1):
        total += int(sys.argv[i + 1])
    print("{:d}".format(total))
