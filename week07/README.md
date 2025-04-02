# 10



### Notes
- `import re`
- `re.search()` is the standard function
- `search(pattern, string [, flags])`

# 11
### Notes
- `search` is closest to grep, but it takes an input string and is not a line-based filter tool, instead it returns a `match` object.
- `match` is search but only finds matches at beginning of input string
- `fullmatch` only matches when whole input matches the regular expression.

### Useful Match atrributes
- `match.span()` the starting and ending index of match
- `match.group(0)` finds the part of the input that matched the regular expression
- `match.group(1)` will return the first capture group, `group(2)` will grab the second and so on.


### Flags
- `re.IGNORECASE` - ignores case
- `re.DOTALL` - the wildcard character '.' will include newlines

### Python raw strings
- we often specify the regex by using the raw string notation for example
`regex_str = r".*"`, this allows us to avoid the clashing behaviour of \ in regex and how python also handles escaped characters. You can read about this in the documentation: https://docs.python.org/3/library/re.html 