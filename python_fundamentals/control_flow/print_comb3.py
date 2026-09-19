#!/usr/bin/env python3
"""Print all unique ascending combinations of two different digits."""
for i in range(10):
    for j in range(10):
        if i < j:
            print("{:d}{:d}".format(i, j), end="")
            if i != 8 or j != 9:
                print(", ", end="")
print()
