# Python - File Handling

Functions that read, write and append text files (UTF-8) using the
`with` statement.

## Files

| File | Description |
|------|-------------|
| `read_file.py` | `read_file(filename="")` prints the content of a text file to stdout |
| `write_file.py` | `write_file(filename="", text="")` writes text to a file (creates or overwrites it) and returns the number of characters written |
| `append_write.py` | `append_write(filename="", text="")` appends text to a file (creates it if missing) and returns the number of characters added |

## Requirements

- Ubuntu 20.04 LTS, python3 (3.8.5)
- pycodestyle 2.7.*
- All files are executable and end with a new line
- No module imports

## Usage

```python
#!/usr/bin/env python3
write_file = __import__('write_file').write_file

print(write_file("my_first_file.txt", "This School is so cool!\n"))
```
