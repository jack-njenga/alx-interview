#!/usr/bin/python3
"""
Write a method that determines if a given data set represents
a valid UTF-8 encoding.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Returns: True if data is a valid UTF-8 encoding, else return False
        - A character in UTF-8 can be 1 to 4 bytes long
        - The data set can contain multiple characters
        - The data will be represented by a list of integers
        - Each integer represents 1 byte of data, therefore
          you only need to handle the 8 least significant
          bits of each integer
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) == 0b10:
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
