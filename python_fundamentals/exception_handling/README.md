# Python - Exception Handling

Handling runtime errors defensively: `try`/`except` with specific
exception types, `else`/`finally` blocks, and raising exceptions
explicitly. Focuses on writing functions that fail safely and
predictably instead of crashing on bad input.

## Tasks

0. `safe_print_list.py` - print x elements of a list, stopping
   gracefully if x exceeds the list's length.
1. `safe_print_integer.py` - print an integer via `{:d}`.format(),
   returning True/False instead of using type().
2. `safe_print_list_integers.py` - print only the integers in a list,
   skipping non-integer elements.
3. `safe_print_division.py` - divide two integers, always reporting
   the result via `finally`.
4. `raise_exception.py` - raise a `TypeError` explicitly.
5. `raise_exception_msg.py` - raise a `NameError` with a custom
   message.
