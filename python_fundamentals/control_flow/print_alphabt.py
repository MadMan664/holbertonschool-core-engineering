#!/usr/bin/env python3
"""Print the lowercase alphabet except q and e."""
result = ""
for i in range(97, 123):
    c = chr(i)
    if c not in "qe":
        result += c
print("{}".format(result), end="")
