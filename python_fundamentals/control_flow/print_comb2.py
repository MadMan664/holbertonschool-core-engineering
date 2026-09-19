#!/usr/bin/env python3
"""Print numbers 00 to 99, comma-space separated."""
for i in range(100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
