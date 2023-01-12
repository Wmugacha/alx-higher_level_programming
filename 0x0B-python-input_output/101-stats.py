#!/usr/bin/python3
"""
   Module of a script that reads stdin line by line and computes metrics.

"""


import sys

line_count = 0
total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    for line in sys.stdin:
        line_count += 1
        fields = line.strip().split(" ")
        status_code = int(fields[-2])
        file_size = int(fields[-1])
        total_size += file_size
        status_codes[status_code] += 1

        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
            print()
except KeyboardInterrupt:
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
