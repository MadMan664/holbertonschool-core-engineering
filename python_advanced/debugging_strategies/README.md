# Python - Debugging Strategies

Six debugging labs. Each script was run first to reproduce the problem,
then fixed at its root cause.

| File | Symptom | Root cause | Fix |
|------|---------|------------|-----|
| `0-reading.py` | `TypeError: unsupported operand type(s) for +=: 'int' and 'str'` | readings arrive as strings and were added to an int | convert each reading with `int()` |
| `1-print.py` | prints `2` instead of `3` | `reading_is_ok` used `<` instead of `>=` | compare with `>=` |
| `2-pdb.py` | prints `60.0` instead of `70.0` | the loop summed `raw` instead of the adjusted score | sum `adjusted` |
| `3-data.py` | prints `-286.2` | `parse_discount_rate` returned `10.0` instead of `0.10` | divide the percent by 100 at the source |
| `4-logging.py` | average `15.0` instead of `20.0` | the counter was incremented for invalid records too | count only valid records |
| `5-defensive.py` | crash on a non-numeric token | input assumed to be valid | validate input and raise clear `ValueError` messages |

The scripts are numbered because names such as `logging.py` or `pdb.py`
shadow the standard library modules of the same name.

## Run

./0-reading.py
./1-print.py
./2-pdb.py
./3-data.py
./4-logging.py
./5-defensive.py

