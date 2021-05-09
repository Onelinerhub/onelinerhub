# Remove blank lines

```bash
grep -v -e '^$' file.txt
```

- -v - will invert search results
- -e - will ask grep to use regex
- '^$' - regex to match empty strings
- file.txt - file to search in
