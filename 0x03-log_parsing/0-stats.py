#!/usr/bin/python3
"""
File: 0-stats.py

Log parsing
"""
import sys
from collections import Counter
import re


file_size = 0
status_codes = []
count = 0

log_pattern = re.compile(
    r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

for line in sys.stdin:
    if log_pattern.match(line):
        if count < 10:
            file_size += int(line.split()[-1])
            status_codes.append(int(line.split()[-2]))
            count += 1

        if count == 10:
            print(f"File size: {file_size}")
            sorted_status_codes = sorted(status_codes)
            status_code_counted = Counter(sorted_status_codes)
            for status, count in status_code_counted.items():
                print(f"{status}: {count}")
            count = 0
            status_codes.clear()
    else:
        continue
