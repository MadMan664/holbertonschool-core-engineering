#!/usr/bin/env python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file, creating it if needed, and return
    the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
