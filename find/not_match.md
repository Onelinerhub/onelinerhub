# Search for files not matching specific pattern

```bash
find /tmp -type f -not -name "*test*"
```

- /tmp - base path to search in
- -type f - locate only files (skip directories)
- -not - will revert next rule
- -name "\*test\*" - match all files containing ```test``` in their names (thus exclude them from results)
