#!/usr/bin/python3
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Determines if a given data set represents a
        valid UTF-8 encoding.
    """
    i = 0
    while i < len(data):
        if data[i] >> 7 == 0:
            i += 1
        elif data[i] >> 5 == 0b110:
            if i + 1 < len(data) and data[i + 1] >> 6 == 0b10:
                i += 2
            else:
                return False
        elif data[i] >> 4 == 0b1110:
            if i + 2 < len(data) and data[i + 1] >> 6 == 0b10 and \
                    data[i + 2] >> 6 == 0b10:
                i += 3
            else:
                return False
        elif data[i] >> 3 == 0b11110:
            if i + 3 < len(data) and data[i + 1] >> 6 == 0b10 and \
                    data[i + 2] >> 6 == 0b10 and data[i + 3] >> 6 == 0b10:
                i += 4
            else:
                return False
        else:
            return False
    return True
