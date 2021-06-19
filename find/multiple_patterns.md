# Search for files matching multiple patterns

```bash
find /tmp -name "*a*" -or -name "*b*"
```

- /tmp - base path to search in
- -name "\*a\*" - find everything that contains ```a``` in its name
- -or - check additional following condition
- -name "\*b\*" - find everything that contains ```b``` in its name
