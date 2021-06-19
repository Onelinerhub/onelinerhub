# How to search in directory non-recursively (skip subdirectories)

```bash
find /tmp -maxdepth 1
```

- /tmp - base path to search in
- -maxdepth 1 - will not go into subdirectories
