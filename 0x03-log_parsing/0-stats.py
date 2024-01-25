#!/usr/bin/python3
"""
File: 0-stats.py

Log parsing
"""
import sys
from collections import Counter
import re


def reporter(file_size, status_codes):
    """
    Prepares a report.

    parameters:
    - file_size (int): Size of a file.
    - status_codes (int): Status of a request.
    """
    print(f"File size: {file_size}")
    sorted_status_codes = sorted(status_codes)
    status_code_counted = Counter(sorted_status_codes)
    for status, count in status_code_counted.items():
        print(f"{status}: {count}")


def log_parser():
    """
    Reads stdin line by line and computes metrics.
    """
    file_size = 0
    status_codes = []
    count = 0

    log_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] '
                             r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

    for line in sys.stdin:
        try:
            if log_pattern.match(line):
                if count < 10:
                    file_size += int(line.split()[-1])
                    status_codes.append(int(line.split()[-2]))
                    count += 1

                if count == 10:
                    reporter(file_size, status_codes)
                    count = 0
                    status_codes.clear()
            else:
                continue
        except KeyboardInterrupt as e:
            reporter(file_size, status_codes)
            count = 0
            status_codes.clear()


if __name__ == '__main__':
    log_parser()
