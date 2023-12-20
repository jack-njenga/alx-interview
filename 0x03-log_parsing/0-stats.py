#!/usr/bin/env python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import sys


if __name__ == "__main__":
    
    for line in sys.stdin:
        words = line.split(" ")
        code = float(words[-2])
        if (code in [200, 301, 400, 401, 403, 404, 405, 500]):
            code = int(code)
            print(code)
        else:
            continue