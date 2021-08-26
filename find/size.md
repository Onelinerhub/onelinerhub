# How to find files with specific size

```bash
find . -type f -size +1000c -a -size -5000c
```

- -type f - find only files
- -size +1000c - size of the file should be more then `1000` bytes
- -a - "and" operator
- -size -5000c - size of the file should be less then `5000` bytes
